# Elasticsearch in Flask
Python | Flask | Elasticsearch | Kibana | Docker

## Usage

 - install docker-compose:
```
 pip install docker-compose
```
 - build and run your app:
```
 docker-compose up
```
## kibana interface
 - go to `http://{DOCKER_MACHINE_IP}:5061`:

<img src="./doc/kibana_interface.png" width="100%"/>


## APIs
- elasticsearch info and healthy:
```
[GET] {baseUrl}/elastic/info
[GET] {baseUrl}/elastic/health
```
- Add or update a doc:
```
[POST] {baseUrl}/elastic/<user_id>
body:
{
    "username": "test",
    "phone_number":"000000000",
    "address":"test",
    "email": "test@test.com"
}
```
- Delete a doc:
```
[DELETE] {baseUrl}/elastic/<user_id>
```

- Search a keyword in user address field:
```
[GET] {baseUrl}/elastic/<Keyword>
```