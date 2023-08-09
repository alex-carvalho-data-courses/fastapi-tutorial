# <img src="img/fastapi.png" alt="FastAPI" width="30" style="vertical-align: middle;"> | FastAPI official Tutorial #

## What is this repository for? ##

### Quick summary

Project to follow the [Official FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/).  


## How do I get set up? ##

### Summary of set up

Python Poetry project.  
Just install it with poetry, and poetry will take care of all dependencies.  

### Dependencies

- python ^3.11
- poetry

### Configuration

Install poetry project:  
```shell
poetry install
```

### Database configuration

CHANGE_ME  

### How to run tests

#### Manual tests

Every lesson will have a `main.py` script that can run on uvicorn and be accessed by curl.  

##### Running uvicorn server

Pattern:  
```shell
uvicorn <main module>:<FastAPI object> --reload
```

Example:  
```shell
uvicorn fastapi_tutorial.l01_first_steps.main:app --reload
```

##### Invoking *path_operation* with curl

Pattern:
```shell
curl [-X method] <url>:8000[<path>]
```

Examples:  
```shell
curl 127.0.0.1:8000
```

```shell
curl -X POST 127.0.0.1:8000/items/12
```
### Deployment instructions

CHANGE_ME  


## Documentation ##

### Swagger UI docs
http://127.0.0.1:8000/docs 

### ReDoc docs
http://127.0.0.1:8000/redoc


## OpenAPI schema ##

http://127.0.0.1:8000/openapi.json


## Who do I talk to? ##

### Repo owner or admin

[alex carvalho](mailto:allex.carvalho@gmail.com)
