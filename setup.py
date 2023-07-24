# setup.py
from setuptools import setup, find_packages

setup(
    name='fastapi_dynamic_routers',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
    ],
    author='Ashkan Goleh Pour',
    author_email='ashkangoleh@gmail.com',
    description='A dynamic routes includer for FastAPI',
    long_description=(
        "fastapi_dynamic_routers is a Python library that simplifies the management of routes in FastAPI applications. "
        "It provides a clean and efficient way to register routes dynamically, enabling you to keep your codebase "
        "organized and maintainable, even as your application grows.\n\n"
        "Key Features:\n"
        "- Simplicity: The library comes with a straightforward implementation that seamlessly integrates with your FastAPI application.\n"
        "- Ease of Use: With just a few lines of code, you can include or exclude routes from your application, providing the flexibility you need during development.\n"
        "- Organized Codebase: By dynamically registering routes, you can maintain a clean and well-structured codebase, even in large-scale projects.\n\n"
        "Usage Example:\n\n"
        "```python\n"
        "# main.py\n"
        "from fastapi import FastAPI\n"
        "from fastapi_dynamic_routers import Routers\n\n"
        "app = FastAPI()\n\n"
        "# List of router modules to include dynamically\n"
        "URLS = [\n"
        "    'path.to.APIRouter.instantiate',\n"
        "    '...'\n"
        "]\n\n"
        "# Initialize the dynamic routers\n"
        "routers = Routers(app, URLS)()\n"
        "```\n\n"
        "In this example, simply modify the `URLS` list to add or remove routes from your FastAPI application. "
        "The dynamic routes includer will handle the registration, keeping your main file clean and focused.\n\n"
    ),
    long_description_content_type='text/markdown',
    url='https://github.com/ashkangoleh/fastapi_dynamic_routes',
)