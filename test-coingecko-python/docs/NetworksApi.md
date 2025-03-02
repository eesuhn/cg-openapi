# test_coingecko_python.NetworksApi

All URIs are relative to *https://pro-api.coingecko.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networks_list**](NetworksApi.md#networks_list) | **GET** /onchain/networks | Supported Networks List


# **networks_list**
> SupportedNetworks networks_list()

Supported Networks List

Query all the supported networks on GeckoTerminal

### Example

* Api Key Authentication (proKeyAuth):
* Api Key Authentication (demoKeyAuth):

```python
import test_coingecko_python
from test_coingecko_python.models.supported_networks import SupportedNetworks
from test_coingecko_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pro-api.coingecko.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = test_coingecko_python.Configuration(
    host = "https://pro-api.coingecko.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: proKeyAuth
configuration.api_key['proKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['proKeyAuth'] = 'Bearer'

# Configure API key authorization: demoKeyAuth
configuration.api_key['demoKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['demoKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with test_coingecko_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_coingecko_python.NetworksApi(api_client)

    try:
        # Supported Networks List
        api_response = api_instance.networks_list()
        print("The response of NetworksApi->networks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SupportedNetworks**](SupportedNetworks.md)

### Authorization

[proKeyAuth](../README.md#proKeyAuth), [demoKeyAuth](../README.md#demoKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

