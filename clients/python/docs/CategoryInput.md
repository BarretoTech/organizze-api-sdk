# CategoryInput

Schema for creating or updating a category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | 
**parent_id** | **int** |  | [optional] 
**group_id** | **str** |  | [optional] 
**fixed** | **bool** |  | [optional] 
**essential** | **bool** |  | [optional] 

## Example

```python
from organizze_api.models.category_input import CategoryInput

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryInput from a JSON string
category_input_instance = CategoryInput.from_json(json)
# print the JSON string representation of the object
print(CategoryInput.to_json())

# convert the object into a dict
category_input_dict = category_input_instance.to_dict()
# create an instance of CategoryInput from a dict
category_input_from_dict = CategoryInput.from_dict(category_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


