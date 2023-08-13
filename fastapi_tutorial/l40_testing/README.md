# Lesson 40 - Testing #  

## 1. Start uvicorn server  
```shell
uvicorn fastapi_tutorial.l40_testing.main:app --reload
```

## 2. API documentation  
http://127.0.0.1:8000/docs

## 3. Invoking a dummy operation to be tested
```shell
curl '127.0.0.1:8000/'
```

## 4. Get Item Path Operation 

### 4.1. Get Item - Failure: Missing X-Token
```shell
curl '127.0.0.1:8000/items/foo'
```

### 4.2. Get Item - Success: Valid X-Token - Existent Item
```shell
curl --header 'X-Token: coneofsilence' '127.0.0.1:8000/items/foo'
```

### 4.3. Get Item - Failure: Invalid X-Token
```shell
curl --header 'X-Token: wherever' '127.0.0.1:8000/items/foo'
```

### 4.4. Get Item - Failure: Missing item
```shell
curl --header 'X-Token: coneofsilence' '127.0.0.1:8000/items/pamonha'
```

## 5. Post Item Path Operation

### 5.1. Post Item - Failure: Missing Token Header
```shell
curl --request 'POST' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"id": "pamonha", "title": "Pamonha", "description": "pamonha quentinha"}' '127.0.0.1:8000/items/'
```

### 5.2. Post Item - Failure: Invalid Token Header
```shell
curl --request 'POST' --header 'X-Token: something' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"id": "pamonha", "title": "Pamonha", "description": "pamonha quentinha"}' '127.0.0.1:8000/items/'
```

### 5.3. Post Item - Failure: Already existent Item
```shell
curl --request 'POST' --header 'X-Token: coneofsilence' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"id": "foo", "title": "Foo", "description": "Foo Fighters"}' '127.0.0.1:8000/items/'
```

### 5.4. Get Item - Failure: Missing Item
```shell
curl --header 'X-Token: coneofsilence' '127.0.0.1:8000/items/pamonha'
```

### 5.5. Post Item - Success: Create Item
```shell
curl --request 'POST' --header 'X-Token: coneofsilence' --header 'Content-Type: application/json' --header 'accept: application/json' --data '{"id": "pamonha", "title": "Pamonha", "description": "pamonha quentinha"}' '127.0.0.1:8000/items/'
```

### 5.6. Get Item - Success: Get Recently created Item
```shell
curl --header 'X-Token: coneofsilence' '127.0.0.1:8000/items/pamonha'
```

## 6. Run automated tests
```shell
poetry run pytest tests/l40_testing
```
or use the IDE UI.  
