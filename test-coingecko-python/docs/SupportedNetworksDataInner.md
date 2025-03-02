# SupportedNetworksDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**SupportedNetworksDataInnerAttributes**](SupportedNetworksDataInnerAttributes.md) |  | [optional] 

## Example

```python
from test_coingecko_python.models.supported_networks_data_inner import SupportedNetworksDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedNetworksDataInner from a JSON string
supported_networks_data_inner_instance = SupportedNetworksDataInner.from_json(json)
# print the JSON string representation of the object
print(SupportedNetworksDataInner.to_json())

# convert the object into a dict
supported_networks_data_inner_dict = supported_networks_data_inner_instance.to_dict()
# create an instance of SupportedNetworksDataInner from a dict
supported_networks_data_inner_from_dict = SupportedNetworksDataInner.from_dict(supported_networks_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


