# fastapi_dynamic_routes/dynamic_routes_includer.py
from typing import Any
from fastapi import FastAPI


class Routers:
    def __init__(self, app: FastAPI, routes: list, prefix: str = '/v1/api') -> None:
        self.app = app
        self.routes = routes
        self.prefix = prefix

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._create_route_methods()
        return self

    def _create_route_methods(self):
        for route in self.routes:
            module_path, route_name = route.rsplit('.', maxsplit=1)
            module = __import__(module_path, fromlist=[route_name])
            route_module = getattr(module, route_name)
            route_method_name = f'{route_name.title().replace("_", "")}Route'

            def route_method():
                return self.app.include_router(
                    route_module,
                    prefix=self.prefix,
                )

            setattr(self, route_method_name, route_method)
            getattr(self, route_method_name)()
