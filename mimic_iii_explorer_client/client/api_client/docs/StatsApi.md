# api_client.StatsApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_stats**](StatsApi.md#all_stats) | **GET** /stats | get statistics for all columns
[**table_stats**](StatsApi.md#table_stats) | **GET** /stats/{tableName} | get statistics for specified table


# **all_stats**
> [TableStats] all_stats()

get statistics for all columns

Get all statistics for all columns in the dataset

### Example

```python
import time
import api_client
from api_client.api import stats_api
from api_client.model.table_stats import TableStats
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stats_api.StatsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get statistics for all columns
        api_response = api_instance.all_stats()
        pprint(api_response)
    except api_client.ApiException as e:
        print("Exception when calling StatsApi->all_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[TableStats]**](TableStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfuly retrieved statistics for all columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_stats**
> TableStats table_stats(table_name)

get statistics for specified table

get all statistics for all tables in the specified table

### Example

```python
import time
import api_client
from api_client.api import stats_api
from api_client.model.table_stats import TableStats
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/jv723/reference/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "https://virtserver.swaggerhub.com/jv723/reference/1.0.0"
)


# Enter a context with an instance of the API client
with api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stats_api.StatsApi(api_client)
    table_name = "tableName_example" # str | name of the table for which to compute the column statistics

    # example passing only required values which don't have defaults set
    try:
        # get statistics for specified table
        api_response = api_instance.table_stats(table_name)
        pprint(api_response)
    except api_client.ApiException as e:
        print("Exception when calling StatsApi->table_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| name of the table for which to compute the column statistics |

### Return type

[**TableStats**](TableStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved statistics for specified table |  -  |
**400** | Invalid table name |  -  |
**404** | Table with specified name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

