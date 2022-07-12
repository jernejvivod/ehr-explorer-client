import unittest

from mimic_iii_explorer_client.errors.client_errors import ClientException
from mimic_iii_explorer_client.mimic_iii_explorer_client.client import Client
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.id_retrieval_spec import IdRetrievalSpec, IdRetrievalFilterSpec, ComparatorEnum

import http


class TestIdRetrieval(unittest.TestCase):
    """Integration tests for ID retrieval"""

    def test_basic_retrieval(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="AdmissionsEntity",
            id_property="hadmId",
            filter_specs=None
        )
        client = Client()
        res = client.retrieve_ids(id_retrieval_spec)
        self.assertEqual(58976, len(res))

    def test_retrieval_non_existing_root_entity(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="Wrong",
            id_property="hadmId",
            filter_specs=None
        )
        client = Client()
        with self.assertRaises(ClientException) as context:
            client.retrieve_ids(id_retrieval_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_retrieval_non_existing_id_property(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="AdmissionsEntity",
            id_property="wrong",
            filter_specs=None
        )
        client = Client()
        with self.assertRaises(ClientException) as context:
            client.retrieve_ids(id_retrieval_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_retrieval_non_existing_root_entity_and_id_property(self):
        id_retrieval_spec = IdRetrievalSpec(
            entity_name="Wrong",
            id_property="wrong",
            filter_specs=None
        )
        client = Client()
        with self.assertRaises(ClientException) as context:
            client.retrieve_ids(id_retrieval_spec)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_retrieval_with_filters(self):
        filter_spec1 = IdRetrievalFilterSpec(
            'PatientsEntity',
            'gender',
            ComparatorEnum.EQUAL.value,
            'M'
        )

        filter_spec2 = IdRetrievalFilterSpec(
            'AdmissionsEntity',
            'admissionType',
            ComparatorEnum.EQUAL.value,
            'EMERGENCY'
        )

        id_retrieval_spec = IdRetrievalSpec(
            entity_name="AdmissionsEntity",
            id_property="hadmId",
            filter_specs=[filter_spec1, filter_spec2]
        )

        client = Client()
        res = client.retrieve_ids(id_retrieval_spec)
        self.assertEqual(23437, len(res))
