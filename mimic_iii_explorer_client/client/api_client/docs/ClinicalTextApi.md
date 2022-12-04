# api_client.ClinicalTextApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clinical_text**](ClinicalTextApi.md#clinical_text) | **POST** /clinical-text/extract | extract clinical text (note events)


# **clinical_text**
> [ClinicalTextResult] clinical_text(clinical_text_config)

extract clinical text (note events)

extract clinical text (note events) with specified settings

### Example

```python
import time
import api_client
from api_client.api import clinical_text_api
from api_client.model.clinical_text_config import ClinicalTextConfig
from api_client.model.clinical_text_result import ClinicalTextResult
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clinical_text_api.ClinicalTextApi(api_client)
    clinical_text_config = ClinicalTextConfig(
        clinical_text_entity_name="NoteEventsEntity",
        text_property_name="text",
        clinical_text_entity_id_property_name="rowId",
        date_time_properties_names=[
            "date_time_properties_names_example",
        ],
        root_entities_spec=RootEntitiesSpec(
            root_entity="AdmissionsEntity",
            id_property="hadmId",
            ids=[
                1,
            ],
        ),
        data_range_spec=DataRangeSpec(
            first_minutes=1,
        ),
    ) # ClinicalTextConfig | 

    # example passing only required values which don't have defaults set
    try:
        # extract clinical text (note events)
        api_response = api_instance.clinical_text(clinical_text_config)
        pprint(api_response)
    except api_client.ApiException as e:
        print("Exception when calling ClinicalTextApi->clinical_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clinical_text_config** | [**ClinicalTextConfig**](ClinicalTextConfig.md)|  |

### Return type

[**[ClinicalTextResult]**](ClinicalTextResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully extracted clinical text |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

