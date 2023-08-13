# Lesson 04 - Request Body

## Start uvicorn server
```shell
uvicorn fastapi_tutorial.l04_request_body.main:app --reload
```

## Lesson documentation

http://127.0.0.1:8000/docs

## Testing lesson examples

### 1. Full regular request
```shell
curl --request 'POST' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"name": "soap", "description": "furfles item", "price": 10.5, "tax": 15.3}' '127.0.0.1:8000/items/'
```

### 2. Invocation only with required Body Parameters
```shell
curl --request 'POST' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"name": "poison", "price": 11}' '127.0.0.1:8000/items/'
```

### 3. Request missing required parameter - failure
```shell
curl --request 'POST' --header  'Content-Type: application/json' --header 'accept: application/json' --data '{"name": "sabao"}' '127.0.0.1:8000/items/'
```

### 4. Request Body + Path Parameter
```shell
curl --request 'PUT' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"name": "carglass", "price": 100}' '127.0.0.1:8000/items/100'
```

### 5. Request Body + Path Parameter + Query Parameter
```shell
curl --request 'PUT' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"name": "carglass", "price": 120}' '127.0.0.1:8000/items/p12?q=tcheca'
```