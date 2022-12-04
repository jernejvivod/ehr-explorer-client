import unittest

from generated_client import ApiException
from generated_client.models.id_retrieval_filter_spec import IdRetrievalFilterSpec
from generated_client.models.id_retrieval_spec import IdRetrievalSpec
from mimic_iii_explorer_client.client.ids_api_client import IdsApiClient

import http

from mimic_iii_explorer_client.mimic_iii_explorer_client.model.id_retrieval_spec import ComparatorEnum


class TestIdRetrieval(unittest.TestCase):
    """Integration tests for ID retrieval"""

    def test_basic_retrieval(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="AdmissionsEntity",
            id_property="hadmId"
        )
        client = IdsApiClient()
        res = client.ids(id_retrieval_spec)
        self.assertEqual(58976, len(res))

    def test_retrieval_non_existing_root_entity(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="Wrong",
            id_property="hadmId"
        )
        client = IdsApiClient()
        with self.assertRaises(ApiException) as context:
            client.ids(id_retrieval_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_retrieval_non_existing_id_property(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="AdmissionsEntity",
            id_property="wrong"
        )
        client = IdsApiClient()
        with self.assertRaises(ApiException) as context:
            client.ids(id_retrieval_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_retrieval_non_existing_root_entity_and_id_property(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="Wrong",
            id_property="wrong"
        )
        client = IdsApiClient()
        with self.assertRaises(ApiException) as context:
            client.ids(id_retrieval_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_retrieval_with_filters(self):
        filter_spec1 = IdRetrievalFilterSpec(
            entity_name='PatientsEntity',
            property_name='gender',
            comparator=ComparatorEnum.EQUAL.value,
            property_val='M'
        )

        filter_spec2 = IdRetrievalFilterSpec(
            entity_name='AdmissionsEntity',
            property_name='admissionType',
            comparator=ComparatorEnum.EQUAL.value,
            property_val='EMERGENCY'
        )

        id_retrieval_spec = IdRetrievalSpec(
            entity_name="AdmissionsEntity",
            id_property="hadmId",
            filter_specs=[filter_spec1, filter_spec2]
        )

        client = IdsApiClient()
        res = client.ids(id_retrieval_spec)
        self.assertEqual(23437, len(res))
