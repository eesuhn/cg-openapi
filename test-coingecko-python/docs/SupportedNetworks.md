# SupportedNetworks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SupportedNetworksDataInner]**](SupportedNetworksDataInner.md) |  | [optional] 

## Example

```python
from test_coingecko_python.models.supported_networks import SupportedNetworks

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedNetworks from a JSON string
supported_networks_instance = SupportedNetworks.from_json(json)
# print the JSON string representation of the object
print(SupportedNetworks.to_json())

# convert the object into a dict
supported_networks_dict = supported_networks_instance.to_dict()
# create an instance of SupportedNetworks from a dict
supported_networks_from_dict = SupportedNetworks.from_dict(supported_networks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


