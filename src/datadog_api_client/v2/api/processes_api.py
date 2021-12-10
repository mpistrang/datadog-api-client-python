# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    date,
    datetime,
    file_type,
    none_type,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.process_summaries_response import ProcessSummariesResponse


class ProcessesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._list_processes_endpoint = _Endpoint(
            settings={
                "response_type": (ProcessSummariesResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/processes",
                "operation_id": "list_processes",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
                    "location": "query",
                },
                "_from": {
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 10000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def list_processes(self, **kwargs):
        """Get all processes

        Get all processes for your organization.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_processes(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            search (str): String to search processes by.. [optional]
            tags (str): Comma-separated list of tags to filter processes by.. [optional]
            _from (int): Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window will be 15 minutes before the `to` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`.. [optional]
            to (int): Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window will be 15 minutes after the `from` timestamp. If neither `from` nor `to` are provided, the query window will be `[now - 15m, now]`.. [optional]
            page_limit (int): Maximum number of results returned.. [optional] if omitted the server will use the default value of 1000
            page_cursor (str): String to query the next page of results. This key is provided with each valid response from the API in `meta.page.after`.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ProcessSummariesResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_processes_endpoint.default_arguments(kwargs)
        return self._list_processes_endpoint.call_with_http_info(**kwargs)
