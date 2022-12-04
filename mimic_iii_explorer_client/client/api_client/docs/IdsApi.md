# api_client.IdsApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ids**](IdsApi.md#ids) | **POST** /ids | get id values


# **ids**
> [int] ids(id_retrieval_spec)

get id values

get id values for specified entity

### Example

```python
import time
import api_client
from api_client.api import ids_api
from api_client.model.id_retrieval_spec import IdRetrievalSpec
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ids_api.IdsApi(api_client)
    id_retrieval_spec = IdRetrievalSpec(
        entity_name="entity_name_example",
        id_property="id_property_example",
        filter_specs=[
            IdRetrievalFilterSpec(
                entity_name="entity_name_example",
                property_name="property_name_example",
                comparator="LESS",
                property_val={},
            ),
        ],
    ) # IdRetrievalSpec | 

    # example passing only required values which don't have defaults set
    try:
        # get id values
        api_response = api_instance.ids(id_retrieval_spec)
        pprint(api_response)
    except api_client.ApiException as e:
        print("Exception when calling IdsApi->ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_retrieval_spec** | [**IdRetrievalSpec**](IdRetrievalSpec.md)|  |

### Return type

**[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

