# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


class AWSAccount(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the name of the attribute. The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      validations (dict): The key is the name of the attribute. The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    validations = {}

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "access_key_id": (str,),
            "account_id": (str,),
            "account_specific_namespace_rules": ({str: (bool,)},),
            "cspm_resource_collection_enabled": (bool,),
            "excluded_regions": ([str],),
            "filter_tags": ([str],),
            "host_tags": ([str],),
            "metrics_collection_enabled": (bool,),
            "resource_collection_enabled": (bool,),
            "role_name": (str,),
            "secret_access_key": (str,),
        }

    attribute_map = {
        "access_key_id": "access_key_id",
        "account_id": "account_id",
        "account_specific_namespace_rules": "account_specific_namespace_rules",
        "cspm_resource_collection_enabled": "cspm_resource_collection_enabled",
        "excluded_regions": "excluded_regions",
        "filter_tags": "filter_tags",
        "host_tags": "host_tags",
        "metrics_collection_enabled": "metrics_collection_enabled",
        "resource_collection_enabled": "resource_collection_enabled",
        "role_name": "role_name",
        "secret_access_key": "secret_access_key",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """AWSAccount - a model defined in OpenAPI

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
            access_key_id (str): Your AWS access key ID. Only required if your AWS account is a GovCloud or China account.. [optional]
            account_id (str): Your AWS Account ID without dashes.. [optional]
            account_specific_namespace_rules ({str: (bool,)}): An object, (in the form `{\"namespace1\":true/false, \"namespace2\":true/false}`), that enables or disables metric collection for specific AWS namespaces for this AWS account only.. [optional]
            cspm_resource_collection_enabled (bool): Whether Datadog collects cloud security posture management resources from your AWS account. This includes additional resources not covered under the general `resource_collection`.. [optional] if omitted the server will use the default value of False
            excluded_regions ([str]): An array of AWS regions to exclude from metrics collection.. [optional]
            filter_tags ([str]): The array of EC2 tags (in the form `key:value`) defines a filter that Datadog uses when collecting metrics from EC2. Wildcards, such as `?` (for single characters) and `*` (for multiple characters) can also be used. Only hosts that match one of the defined tags will be imported into Datadog. The rest will be ignored. Host matching a given tag can also be excluded by adding `!` before the tag. For example, `env:production,instance-type:c1.*,!region:us-east-1`. [optional]
            host_tags ([str]): Array of tags (in the form `key:value`) to add to all hosts and metrics reporting through this integration.. [optional]
            metrics_collection_enabled (bool): Whether Datadog collects metrics for this AWS account.. [optional] if omitted the server will use the default value of True
            resource_collection_enabled (bool): Whether Datadog collects a standard set of resources from your AWS account.. [optional] if omitted the server will use the default value of False
            role_name (str): Your Datadog role delegation name.. [optional]
            secret_access_key (str): Your AWS secret access key. Only required if your AWS account is a GovCloud or China account.. [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSAccount, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
