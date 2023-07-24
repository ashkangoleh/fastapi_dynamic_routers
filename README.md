# fastapi_dynamic_routers

fastapi_dynamic_routers is a Python library that provides a dynamic routes includer for FastAPI. It allows you to register routes dynamically and keep your codebase clean and organized.

## Installation

You can install fastapi_dynamic_routers using pip:

```bash
pip install fastapi_dynamic_routers
```


## Usage

```python
from fastapi import FastAPI
from fastapi_dynamic_routers import Routers

app = FastAPI()

URLS = [
    'path.to.APIRouter.instantiate',
    '...'
]

routers = Routers(app, URLS, '/v1/api/')()
```