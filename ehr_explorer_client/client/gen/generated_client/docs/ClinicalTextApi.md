# generated_client.ClinicalTextApi

All URIs are relative to *https://virtserver.swaggerhub.com/jv723/reference/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clinical_text**](ClinicalTextApi.md#clinical_text) | **POST** /clinical-text/extract | extract clinical text (note events)


# **clinical_text**
> list[ClinicalTextResult] clinical_text(clinical_text_config)

extract clinical text (note events)

extract clinical text (note events) with specified settings

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
    api_instance = generated_client.ClinicalTextApi(api_client)
    clinical_text_config = generated_client.ClinicalTextConfig() # ClinicalTextConfig | 

    try:
        # extract clinical text (note events)
        api_response = api_instance.clinical_text(clinical_text_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClinicalTextApi->clinical_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clinical_text_config** | [**ClinicalTextConfig**](ClinicalTextConfig.md)|  | 

### Return type

[**list[ClinicalTextResult]**](ClinicalTextResult.md)

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

