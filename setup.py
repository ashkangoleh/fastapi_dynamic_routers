# setup.py
from setuptools import setup, find_packages

setup(
    name='fastapi_dynamic_routes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
    ],
    author='Ashkan Goleh Pour',
    author_email='ashkangoleh@gmail.com',
    description='A dynamic routes includer for FastAPI',
    url='https://github.com/ashkangoleh/fastapi_dynamic_routes',
)