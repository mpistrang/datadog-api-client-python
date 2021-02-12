# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.geomap_widget_definition_style import GeomapWidgetDefinitionStyle
from datadog_api_client.v1.model.geomap_widget_definition_type import GeomapWidgetDefinitionType
from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
from datadog_api_client.v1.model.geomap_widget_request import GeomapWidgetRequest
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["GeomapWidgetDefinitionStyle"] = GeomapWidgetDefinitionStyle
globals()["GeomapWidgetDefinitionType"] = GeomapWidgetDefinitionType
globals()["GeomapWidgetDefinitionView"] = GeomapWidgetDefinitionView
globals()["GeomapWidgetRequest"] = GeomapWidgetRequest
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition


class TestGeomapWidgetDefinition(unittest.TestCase):
    """GeomapWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGeomapWidgetDefinition(self):
        """Test GeomapWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GeomapWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
