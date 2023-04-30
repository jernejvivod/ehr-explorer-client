# generated_client.PropositionalizationApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wordification**](PropositionalizationApi.md#wordification) | **POST** /propositionalization/wordification | perform Wordification propositionalization algorithm


# **wordification**
> list[WordificationResult] wordification(wordification_config)

perform Wordification propositionalization algorithm

perform Woridification propositionalization algorithm with specified settings

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
    api_instance = generated_client.PropositionalizationApi(api_client)
    wordification_config = generated_client.WordificationConfig() # WordificationConfig | 

    try:
        # perform Wordification propositionalization algorithm
        api_response = api_instance.wordification(wordification_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropositionalizationApi->wordification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wordification_config** | [**WordificationConfig**](WordificationConfig.md)|  | 

### Return type

[**list[WordificationResult]**](WordificationResult.md)

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

