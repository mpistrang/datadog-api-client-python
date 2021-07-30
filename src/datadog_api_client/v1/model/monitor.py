# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from datadog_api_client.v1.exceptions import ApiAttributeError


def lazy_import():
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1.model.monitor_options import MonitorOptions
    from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates
    from datadog_api_client.v1.model.monitor_state import MonitorState
    from datadog_api_client.v1.model.monitor_type import MonitorType

    globals()["Creator"] = Creator
    globals()["MonitorOptions"] = MonitorOptions
    globals()["MonitorOverallStates"] = MonitorOverallStates
    globals()["MonitorState"] = MonitorState
    globals()["MonitorType"] = MonitorType


class Monitor(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {
        ("priority",): {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "query": (str,),  # noqa: E501
            "type": (MonitorType,),  # noqa: E501
            "created": (datetime,),  # noqa: E501
            "creator": (Creator,),  # noqa: E501
            "deleted": (
                datetime,
                none_type,
            ),  # noqa: E501
            "id": (int,),  # noqa: E501
            "message": (str,),  # noqa: E501
            "modified": (datetime,),  # noqa: E501
            "multi": (bool,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "options": (MonitorOptions,),  # noqa: E501
            "overall_state": (MonitorOverallStates,),  # noqa: E501
            "priority": (int,),  # noqa: E501
            "restricted_roles": ([str],),  # noqa: E501
            "state": (MonitorState,),  # noqa: E501
            "tags": ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "query": "query",  # noqa: E501
        "type": "type",  # noqa: E501
        "created": "created",  # noqa: E501
        "creator": "creator",  # noqa: E501
        "deleted": "deleted",  # noqa: E501
        "id": "id",  # noqa: E501
        "message": "message",  # noqa: E501
        "modified": "modified",  # noqa: E501
        "multi": "multi",  # noqa: E501
        "name": "name",  # noqa: E501
        "options": "options",  # noqa: E501
        "overall_state": "overall_state",  # noqa: E501
        "priority": "priority",  # noqa: E501
        "restricted_roles": "restricted_roles",  # noqa: E501
        "state": "state",  # noqa: E501
        "tags": "tags",  # noqa: E501
    }

    read_only_vars = {
        "created",  # noqa: E501
        "deleted",  # noqa: E501
        "id",  # noqa: E501
        "modified",  # noqa: E501
        "multi",  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, query, type, *args, **kwargs):  # noqa: E501
        """Monitor - a model defined in OpenAPI

        Args:
            query (str): The monitor query.
            type (MonitorType):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created (datetime): Timestamp of the monitor creation.. [optional]  # noqa: E501
            creator (Creator): [optional]  # noqa: E501
            deleted (datetime, none_type): Whether or not the monitor is deleted. (Always `null`). [optional]  # noqa: E501
            id (int): ID of this monitor.. [optional]  # noqa: E501
            message (str): A message to include with notifications for this monitor.. [optional]  # noqa: E501
            modified (datetime): Last timestamp when the monitor was edited.. [optional]  # noqa: E501
            multi (bool): Whether or not the monitor is broken down on different groups.. [optional]  # noqa: E501
            name (str): The monitor name.. [optional]  # noqa: E501
            options (MonitorOptions): [optional]  # noqa: E501
            overall_state (MonitorOverallStates): [optional]  # noqa: E501
            priority (int): Integer from 1 (high) to 5 (low) indicating alert severity.. [optional]  # noqa: E501
            restricted_roles ([str]): A list of role identifiers that can be pulled from the Roles API. Cannot be used with `locked` option.. [optional]  # noqa: E501
            state (MonitorState): [optional]  # noqa: E501
            tags ([str]): Tags associated to your monitor.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.query = query
        self.type = type
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, query, type, *args, **kwargs):  # noqa: E501
        """Monitor - a model defined in OpenAPI

        Args:
            query (str): The monitor query.
            type (MonitorType):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created (datetime): Timestamp of the monitor creation.. [optional]  # noqa: E501
            creator (Creator): [optional]  # noqa: E501
            deleted (datetime, none_type): Whether or not the monitor is deleted. (Always `null`). [optional]  # noqa: E501
            id (int): ID of this monitor.. [optional]  # noqa: E501
            message (str): A message to include with notifications for this monitor.. [optional]  # noqa: E501
            modified (datetime): Last timestamp when the monitor was edited.. [optional]  # noqa: E501
            multi (bool): Whether or not the monitor is broken down on different groups.. [optional]  # noqa: E501
            name (str): The monitor name.. [optional]  # noqa: E501
            options (MonitorOptions): [optional]  # noqa: E501
            overall_state (MonitorOverallStates): [optional]  # noqa: E501
            priority (int): Integer from 1 (high) to 5 (low) indicating alert severity.. [optional]  # noqa: E501
            restricted_roles ([str]): A list of role identifiers that can be pulled from the Roles API. Cannot be used with `locked` option.. [optional]  # noqa: E501
            state (MonitorState): [optional]  # noqa: E501
            tags ([str]): Tags associated to your monitor.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.query = query
        self.type = type
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
