import http
import unittest
from datetime import datetime

from generated_client import WordificationConfig, ConcatenationSpec, RootEntitiesSpec, PropertySpec, PropertySpecEntry, RootEntityAndTimeLimit, ApiException, ValueTransformationSpec, ValueTransformationSpecEntry, Transform, CompositeColumnsSpec, CompositeColumnsSpecEntry
from mimic_iii_explorer_client.client.wordification_api_client import PropositionalizationApiClient


class TestComputeWordification(unittest.TestCase):
    """Integration tests for Wordification"""

    def set_config(self):
        self.wordification_config_basic = WordificationConfig(
            concatenation_spec=ConcatenationSpec(
                concatenation_scheme='ZERO'
            ),
            root_entities_spec=RootEntitiesSpec(
                root_entity='PatientsEntity',
                id_property='subjectId',
                ids=[291]
            ),
            property_spec=PropertySpec(
                entries=[
                    PropertySpecEntry(
                        entity='PatientsEntity',
                        properties=['gender', 'icuStaysEntitys']
                    ),
                    PropertySpecEntry(
                        entity='IcuStaysEntity',
                        properties=['dbSource', 'firstCareUnit'],
                        property_for_limit='outTime'
                    )
                ],
                root_entity_and_lime_limit=[
                    RootEntityAndTimeLimit(
                        root_entity_id=291,
                        time_lim=datetime(2102, 4, 9, 11, 20, 11)
                    ),
                    RootEntityAndTimeLimit(
                        root_entity_id=291,
                        time_lim=datetime(2106, 4, 18, 22, 5, 39)
                    ),
                    RootEntityAndTimeLimit(
                        root_entity_id=291,
                        time_lim=datetime(2107, 9, 14, 18, 34, 48)
                    )
                ]
            )
        )

    client = PropositionalizationApiClient()

    def setUp(self):
        self.set_config()

    def test_basic(self):
        res = self.client.wordification(self.wordification_config_basic)
        self.assertEqual(3, len(res))
        self.assertEqual(3, len(res[0].words))
        self.assertEqual(5, len(res[1].words))
        self.assertEqual(7, len(res[2].words))

    def test_basic_with_concatenation(self):
        self.wordification_config_basic.concatenation_spec.concatenation_scheme = 'ONE'
        res = self.client.wordification(self.wordification_config_basic)
        self.assertEqual(3, len(res))
        self.assertEqual(4, len(res[0].words))
        self.assertEqual(7, len(res[1].words))
        self.assertEqual(10, len(res[2].words))

    def test_non_existent_entity_or_property(self):
        # wrong entity name in RootEntitiesSpec
        self.wordification_config_basic.root_entities_spec.root_entity = 'Wrong'

        with self.assertRaises(ApiException) as context:
            self.client.wordification(self.wordification_config_basic)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

        # wrong property name in PropertySpecEntry
        self.set_config()
        self.wordification_config_basic.property_spec.entries[0].properties[0] = 'wrong'

        with self.assertRaises(ApiException) as context:
            self.client.wordification(self.wordification_config_basic)

        self.assertEqual(http.HTTPStatus.BAD_REQUEST, context.exception.status)

    def test_wordification_value_transformations(self):
        self.wordification_config_basic.root_entities_spec.ids = [307]

        self.wordification_config_basic.property_spec.entries[1].properties.append('los')

        self.wordification_config_basic.property_spec.root_entity_and_lime_limit = [
            RootEntityAndTimeLimit(
                root_entity_id=291,
                time_lim=datetime(2162, 12, 3, 20, 41, 29)
            ),
            RootEntityAndTimeLimit(
                root_entity_id=291,
                time_lim=datetime(2164, 1, 3, 15, 48, 49)
            )
        ]

        self.wordification_config_basic.value_transformation_spec = ValueTransformationSpec(
            entries=[
                ValueTransformationSpecEntry(
                    entity="IcuStaysEntity",
                    _property="los",
                    transform=Transform(
                        kind='ROUNDING',
                        rounding_multiple=1
                    )
                )
            ]
        )

        # test rounding results
        res = self.client.wordification(self.wordification_config_basic)
        self.assertTrue('icustaysentity@los@1.0' in res[0].words)
        self.assertTrue('icustaysentity@los@6.0' in res[0].words)

    def test_wordification_composite_columns(self):
        self.wordification_config_basic.composite_columns_spec = CompositeColumnsSpec(
            entries=[
                CompositeColumnsSpecEntry(
                    foreign_key_path1=['PatientsEntity'],
                    property1='dob',
                    foreign_key_path2=['PatientsEntity'],
                    property2='dod',
                    composite_name='test',
                    combiner='DATE_DIFF'
                )
            ]
        )

        res = self.client.wordification(self.wordification_config_basic)
        self.assertTrue('composite@test@73_8_2' in res[0].words)

    # TODO implement when functionality implemented in mimic-iii-explorer
    def test_wordification_composite_properties(self):
        pass
