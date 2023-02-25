import os
import sys

# NOTE: this line should be before any imports from the 'generated_client' package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../mimic_iii_explorer_client/client/gen"))

import http  # noqa: E402
import unittest  # noqa: E402

from generated_client import ApiException  # noqa: E402
from generated_client.models.id_retrieval_filter_spec import IdRetrievalFilterSpec  # noqa: E402
from generated_client.models.id_retrieval_spec import IdRetrievalSpec  # noqa: E402
from mimic_iii_explorer_client.client.ids_api_client import IdsApiClient  # noqa: E402


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
            foreign_key_path=['AdmissionsEntity', 'PatientsEntity'],
            property_name='gender',
            comparator='EQUAL',
            property_val='M'
        )

        filter_spec2 = IdRetrievalFilterSpec(
            foreign_key_path=['AdmissionsEntity'],
            property_name='admissionType',
            comparator='EQUAL',
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
