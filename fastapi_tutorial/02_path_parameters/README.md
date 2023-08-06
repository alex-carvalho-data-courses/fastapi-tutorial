# Lesson 02 - Path Parameters

## Lesson documentation

http://127.0.0.1:8000/docs

## Testing lesson examples

### Run uvicorn  

```shell
uvicorn fastapi_tutorial.02_path_parameters.main:app --reload
```

### 1. Invoking Path Operation with untyped parameter

```shell
curl 127.0.0.1:8000/items/foo
```

### 2. Invoking Path Operation with typed parameter

Example with an int parameter:  

#### 2.1. valid integer parameter

```shell
curl 127.0.0.1:8000/things/123
```

### 2.2. invalid string parameter

```shell
curl 127.0.0.1:8000/things/foo
```

### 2.3. invalid float parameter

```shell
curl 127.0.0.1:8000/things/3.1
```