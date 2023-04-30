# generated_client.StatsApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_stats**](StatsApi.md#all_stats) | **GET** /stats | get statistics for all columns
[**entity_stats**](StatsApi.md#entity_stats) | **GET** /stats/{entityName} | get statistics for specified entity


# **all_stats**
> list[EntityStats] all_stats()

get statistics for all columns

Get all statistics for all columns in the dataset

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
    api_instance = generated_client.StatsApi(api_client)
    
    try:
        # get statistics for all columns
        api_response = api_instance.all_stats()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->all_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EntityStats]**](EntityStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved statistics for all columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_stats**
> EntityStats entity_stats(entity_name)

get statistics for specified entity

get all statistics for all properies in the specified entity

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
    api_instance = generated_client.StatsApi(api_client)
    entity_name = 'entity_name_example' # str | name of the entity for which to compute the column statistics

    try:
        # get statistics for specified entity
        api_response = api_instance.entity_stats(entity_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->entity_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_name** | **str**| name of the entity for which to compute the column statistics | 

### Return type

[**EntityStats**](EntityStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved statistics for specified entity |  -  |
**400** | Invalid entity name |  -  |
**404** | Entity with specified name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

