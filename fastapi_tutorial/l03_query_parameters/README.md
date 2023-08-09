# Lesson 03 - Query Parameters

## Start uvicorn server

```shell
uvicorn fastapi_tutorial.l03_query_parameters.main:app --reload
```

## Lessons API  documentation

http://127.0.0.1:8000/docs

## Testing lesson examples

### 1. Request omitting parameters and using the defaults
```shell
curl 127.0.0.1:8000/items/
```

### 2. Request with query parameters
```shell
curl "127.0.0.1:8000/items/?limit=2&skip=1"
```

### 3. Optional query parameter

#### 3.1. With optional parameter
```shell
curl 127.0.0.1:8000/elements/lero-lero/?q=something
```

#### 3.2. Without optional parameter
```shell
curl 127.0.0.1:8000/elements/pa-pum
```

### 4. Boolean Query parameter  

#### 4.1. True values: 1
```shell
curl "127.0.0.1:8000/members/123?q=something&short=1"
```

#### 4.2. True values: True
```shell
curl "127.0.0.1:8000/members/456?short=True"
```

#### 4.3. True values: true
```shell
curl "127.0.0.1:8000/members/123?short=true"
```

#### 4.4. True values: TRUE
```shell
curl "127.0.0.1:8000/members/123?short=TRUE"
```

#### 4.5. True value: TrUe
```shell
curl "127.0.0.1:8000/members/123?short=TrUe"
```

#### 4.6. True value: on
```shell
curl "127.0.0.1:8000/members/123?short=on"
```

#### 4.7. True value: yes
```shell
curl "127.0.0.1:8000/members/123?short=yes"
```

#### 4.8. True value: y
```shell
curl "127.0.0.1:8000/members/123?short=y"
```

#### 4.9 Failure value: yeap
```shell
curl "127.0.0.1:8000/members/123?short=yeap"
```

### 5. Multiple Path and Query Parameters
```shell
curl "127.0.0.1:8000/users/10/items/81230?q=some-query-param&short=y"
```

### 6. Required Query Parameter

#### 6.1. Missing required Query Parameter
```shell
curl "127.0.0.1:8000/components/123"
```

#### 6.2. Passing required Query Parameter
```shell
curl "127.0.0.1:8000/components/123?needy=soooonedy"
```