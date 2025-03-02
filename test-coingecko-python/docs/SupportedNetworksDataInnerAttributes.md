# SupportedNetworksDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**coingecko_asset_platform_id** | **str** |  | [optional] 

## Example

```python
from test_coingecko_python.models.supported_networks_data_inner_attributes import SupportedNetworksDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedNetworksDataInnerAttributes from a JSON string
supported_networks_data_inner_attributes_instance = SupportedNetworksDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(SupportedNetworksDataInnerAttributes.to_json())

# convert the object into a dict
supported_networks_data_inner_attributes_dict = supported_networks_data_inner_attributes_instance.to_dict()
# create an instance of SupportedNetworksDataInnerAttributes from a dict
supported_networks_data_inner_attributes_from_dict = SupportedNetworksDataInnerAttributes.from_dict(supported_networks_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


