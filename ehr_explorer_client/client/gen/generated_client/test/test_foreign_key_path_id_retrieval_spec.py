# coding: utf-8

"""
    EHR Explorer Processor API

    API for the EHR Explorer Processor microservice  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: vivod.jernej@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import generated_client
from generated_client.models.foreign_key_path_id_retrieval_spec import ForeignKeyPathIdRetrievalSpec  # noqa: E501
from generated_client.rest import ApiException

class TestForeignKeyPathIdRetrievalSpec(unittest.TestCase):
    """ForeignKeyPathIdRetrievalSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ForeignKeyPathIdRetrievalSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = generated_client.models.foreign_key_path_id_retrieval_spec.ForeignKeyPathIdRetrievalSpec()  # noqa: E501
        if include_optional :
            return ForeignKeyPathIdRetrievalSpec(
                foreign_key_path = [
                    '["PatientsEntity","IcuStaysEntity"]'
                    ], 
                root_entity_id_property = 'subjectId', 
                end_entity_id_property = 'icuStayId', 
                root_entity_ids = [
                    56
                    ], 
                filter_specs = [
                    generated_client.models.id_retrieval_filter_spec.IdRetrievalFilterSpec(
                        foreign_key_path = [
                            '["AdmissionsEntity","NoteEventsEntity"]'
                            ], 
                        property_name = '0', 
                        comparator = 'LESS', 
                        property_val = generated_client.models.property_val.propertyVal(), )
                    ]
            )
        else :
            return ForeignKeyPathIdRetrievalSpec(
                foreign_key_path = [
                    '["PatientsEntity","IcuStaysEntity"]'
                    ],
                root_entity_id_property = 'subjectId',
                end_entity_id_property = 'icuStayId',
                root_entity_ids = [
                    56
                    ],
        )

    def testForeignKeyPathIdRetrievalSpec(self):
        """Test ForeignKeyPathIdRetrievalSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
