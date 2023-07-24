# fastapi_dynamic_routes

fastapi_dynamic_routes is a Python library that provides a dynamic routes includer for FastAPI. It allows you to register routes dynamically and keep your codebase clean and organized.

## Installation

You can install fastapi_dynamic_routes using pip:

```bash
pip install fastapi_dynamic_routes
```


## Usage

```python
from fastapi import FastAPI
from fastapi_dynamic_routes import Routers

app = FastAPI()

URLS = [
    'path.to.APIRouter.instantiate',
    '...'
]

routers = Routers(app, URLS, '/v1/api/')()
```