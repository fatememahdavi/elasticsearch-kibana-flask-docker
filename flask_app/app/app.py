from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from datetime import datetime


es = Elasticsearch(["http://elasticsearch:9200/"])

app = Flask(__name__)


@app.route("/")
def app_root():
    return "Welcome to the flask API with elasticsearch backend. Try /health endpoint"


@app.route("/elastic/<user_id>", methods=["POST"])
def add_update_doc(user_id):
    args = request.json
    try:
        doc = {
            "username": args["username"],
            "phone_number": args["phone_number"],
            "address": args["address"],
            "email": args["email"],
            "date": datetime.now(),
        }
        # for more information: https://elasticsearch-py.readthedocs.io/en/v8.5.3/
        res = es.index(
            index="test-index", doc_type="test-type", id=user_id, document=doc
        )
        es.indices.refresh(index="test-index")
        return (
            {"message": "successful", "data": res},
            200,
            {"content-type": "application/json"},
        )
    except Exception as e:
        return {"message": "failed"}, 500, {"content-type": "application/json"}


@app.route("/elastic/<user_id>", methods=["DELETE"])
def delete_doc(user_id):
    try:
        # for more information: https://elasticsearch-py.readthedocs.io/en/v8.5.3/
        res = es.delete(index="test-index", doc_type="test-type", id=user_id)
        es.indices.refresh(index="test-index")
        return (
            {"message": "successful", "data": res},
            200,
            {"content-type": "application/json"},
        )
    except Exception as e:
        return {"message": "failed"}, 500, {"content-type": "application/json"}


@app.route("/elastic/<keyword>", methods=["GET"])
def search_in_address(keyword):
    try:
        # for more information: https://elasticsearch-py.readthedocs.io/en/v8.5.3/
        data = es.search(
            index="test-index",
            query={"match": {"address": {"query": "arg", "fuzziness": 2}}},
        )
        res = []
        for hit in data['hits']['hits']:
            res.append(hit)
        return (
            {"message": "successful", "data": res},
            200,
            {"content-type": "application/json"},
        )
    except Exception as e:
        return {"message": "failed"}, 500, {"content-type": "application/json"}


@app.route("/elastic/info")
def es_details():
    return jsonify(es.info())


@app.route("/elastic/health")
def es_health():
    return jsonify(es.cluster.health())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
