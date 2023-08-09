# Lesson 02 - Path Parameters

## Lesson documentation

http://127.0.0.1:8000/docs

## Testing lesson examples

### 0. Run uvicorn  

```shell
uvicorn fastapi_tutorial.l02_path_parameters.main:app --reload
```

### 1. Untyped parameter

```shell
curl 127.0.0.1:8000/items/foo
```

### 2. Typed Parameter

Example with an int parameter:  

#### 2.1. valid integer parameter

```shell
curl 127.0.0.1:8000/things/123
```

#### 2.2. invalid string parameter

```shell
curl 127.0.0.1:8000/things/foo
```

#### 2.3. invalid float parameter

```shell
curl 127.0.0.1:8000/things/3.1
```

### 3. Predefined parameter values

Possible values for this example:
1. alexnet
2. resnet
3. lenet

#### 3.1. valid alexnet parameter

```shell
curl 127.0.0.1:8000/models/alexnet
```

```shell
curl 127.0.0.1:8000/models/resnet
```

#### 3.2. invalid unspecified parameter value

```shell
curl 127.0.0.1:8000/models/aleatory
```

### 4. Path parameter containing a Path

#### 4.1. relative path
```shell
curl 127.0.0.1:8000/files/jon/doe/some_file.txt
```

#### 4.2. absolute path
```shell
curl 127.0.0.1:8000/files//home/jon/doe/some_file.txt
```