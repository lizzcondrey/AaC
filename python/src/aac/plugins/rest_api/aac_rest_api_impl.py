"""AaC Plugin implementation module for the aac-rest-api plugin."""
# NOTE: It is safe to edit this file.
# This file is only initially generated by the aac gen-plugin, and it won't be overwritten if the file already exists.

from typing import Optional
import uvicorn

from aac.plugins.plugin_execution import PluginExecutionResult, plugin_result
from aac.plugins.rest_api.aac_rest_app import app

plugin_name = "aac-rest-api"


def rest_api(host: Optional[str], port: Optional[int]) -> PluginExecutionResult:
    """
    Start a RESTful interface for interacting with and managing AaC.

    Args:
        host (Optional[str]): Set the hostname of the service. Useful for operating behind proxies.
        port (Optional[int]): The port to which the RESTful service will be bound.
    """
    with plugin_result(plugin_name, _start_restful_service, host, port) as result:
        return result


def _start_restful_service(host: Optional[str] = "0.0.0.0", port: Optional[int] = 8000) -> str:
    """Start the RESTful interface service."""
    uvicorn.run(app, host=host, port=port)
    return "Successfully started and stopped the RESTful API."