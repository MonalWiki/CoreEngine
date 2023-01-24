"""
put all the wikiengine dependencies here in one central container.
"""
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
import justpy as jp

class Container(containers.DeclarativeContainer):
    app_builder = providers.Callable(jp.build_app,
                             middlewares = None,
                             APPCLASS = jp.JustpyApp,
                                     startup_func = None
                             )

    
    
