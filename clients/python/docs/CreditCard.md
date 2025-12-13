# CreditCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**card_network** | **str** |  | 
**closing_day** | **int** |  | 
**due_day** | **int** |  | 
**limit_cents** | **int** |  | 
**archived** | **bool** |  | 
**default** | **bool** |  | 
**institution_id** | **str** |  | 
**institution_name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**type** | **str** |  | 

## Example

```python
from organizze_api.models.credit_card import CreditCard

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCard from a JSON string
credit_card_instance = CreditCard.from_json(json)
# print the JSON string representation of the object
print(CreditCard.to_json())

# convert the object into a dict
credit_card_dict = credit_card_instance.to_dict()
# create an instance of CreditCard from a dict
credit_card_from_dict = CreditCard.from_dict(credit_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


