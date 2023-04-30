# generated_client.TargetApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**target_extraction**](TargetApi.md#target_extraction) | **POST** /target | extract target value


# **target_extraction**
> list[ExtractedTarget] target_extraction(target_extraction_spec)

extract target value

extract target value from database for specified goal

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
    api_instance = generated_client.TargetApi(api_client)
    target_extraction_spec = generated_client.TargetExtractionSpec() # TargetExtractionSpec | 

    try:
        # extract target value
        api_response = api_instance.target_extraction(target_extraction_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TargetApi->target_extraction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_extraction_spec** | [**TargetExtractionSpec**](TargetExtractionSpec.md)|  | 

### Return type

[**list[ExtractedTarget]**](ExtractedTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully extracted target values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

