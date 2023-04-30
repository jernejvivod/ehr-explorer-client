# generated_client.IdsApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ids**](IdsApi.md#ids) | **POST** /ids | get id values
[**ids_fk**](IdsApi.md#ids_fk) | **POST** /ids/by-fk-path | get id values


# **ids**
> list[str] ids(id_retrieval_spec)

get id values

get id values for specified entity

### Example

```python
from __future__ import print_function
import time
import generated_client
from generated_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = generated_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with generated_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = generated_client.IdsApi(api_client)
    id_retrieval_spec = generated_client.IdRetrievalSpec() # IdRetrievalSpec | 

    try:
        # get id values
        api_response = api_instance.ids(id_retrieval_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdsApi->ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_retrieval_spec** | [**IdRetrievalSpec**](IdRetrievalSpec.md)|  | 

### Return type

**list[str]**

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

# **ids_fk**
> list[str] ids_fk(foreign_key_path_id_retrieval_spec)

get id values

get id values for entities on end of foreign key path

### Example

```python
from __future__ import print_function
import time
import generated_client
from generated_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = generated_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with generated_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = generated_client.IdsApi(api_client)
    foreign_key_path_id_retrieval_spec = generated_client.ForeignKeyPathIdRetrievalSpec() # ForeignKeyPathIdRetrievalSpec | 

    try:
        # get id values
        api_response = api_instance.ids_fk(foreign_key_path_id_retrieval_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdsApi->ids_fk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foreign_key_path_id_retrieval_spec** | [**ForeignKeyPathIdRetrievalSpec**](ForeignKeyPathIdRetrievalSpec.md)|  | 

### Return type

**list[str]**

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

