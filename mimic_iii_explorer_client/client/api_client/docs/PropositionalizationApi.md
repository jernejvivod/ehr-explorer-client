# api_client.PropositionalizationApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wordification**](PropositionalizationApi.md#wordification) | **POST** /propositionalization/wordification | perform Wordification propositionalization algorithm


# **wordification**
> [WordificationResult] wordification(wordification_config)

perform Wordification propositionalization algorithm

perform Woridification propositionalization algorithm with specified settings

### Example

```python
import time
import api_client
from api_client.api import propositionalization_api
from api_client.model.wordification_config import WordificationConfig
from api_client.model.wordification_result import WordificationResult
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = propositionalization_api.PropositionalizationApi(api_client)
    wordification_config = WordificationConfig(
        root_entities_spec=RootEntitiesSpec(
            root_entity="AdmissionsEntity",
            id_property="hadmId",
            ids=[
                1,
            ],
        ),
        property_spec=PropertySpec(
            entries=[
                PropertySpecEntry(
                    entity="AdmissionsEntity",
                    properties=[
                        "insurance",
                    ],
                ),
            ],
        ),
        composite_columns_spec=CompositeColumnsSpec(
            entries=[
                CompositeColumnsSpecEntry(
                    table1="AdmissionsEntity",
                    property1="admitTime",
                    table2="PatientsEntity",
                    property2="dob",
                    composite_name="ageDecades",
                    combiner="DATE_DIFF",
                ),
            ],
        ),
        value_transformation_spec=ValueTransformationSpec(
            entries=[
                ValueTransformationSpecEntry(
                    entity="AdmissionsEntity",
                    _property="_property_example",
                    transform=Transform(
                        kind="ROUNDING",
                        rounding_multiple=20.0,
                        date_diff_round_type="YEAR",
                    ),
                ),
            ],
        ),
        concatenation_spec=ConcatenationSpec(
            concatenation_scheme="ZERO",
        ),
    ) # WordificationConfig | 

    # example passing only required values which don't have defaults set
    try:
        # perform Wordification propositionalization algorithm
        api_response = api_instance.wordification(wordification_config)
        pprint(api_response)
    except api_client.ApiException as e:
        print("Exception when calling PropositionalizationApi->wordification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wordification_config** | [**WordificationConfig**](WordificationConfig.md)|  |

### Return type

[**[WordificationResult]**](WordificationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully performed the Wordification algorithm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

