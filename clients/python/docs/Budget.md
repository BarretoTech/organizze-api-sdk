# Budget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in_cents** | **int** |  | [optional] 
**category_id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**activity_type** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**predicted_total** | **int** |  | [optional] 
**percentage** | **str** |  | [optional] 

## Example

```python
from organizze_api.models.budget import Budget

# TODO update the JSON string below
json = "{}"
# create an instance of Budget from a JSON string
budget_instance = Budget.from_json(json)
# print the JSON string representation of the object
print(Budget.to_json())

# convert the object into a dict
budget_dict = budget_instance.to_dict()
# create an instance of Budget from a dict
budget_from_dict = Budget.from_dict(budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


