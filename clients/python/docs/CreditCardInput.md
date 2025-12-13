# CreditCardInput

Schema for creating or updating a credit card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**card_network** | **str** |  | [optional] 
**closing_day** | **int** |  | 
**due_day** | **int** |  | 
**limit_cents** | **int** |  | [optional] 
**archived** | **bool** |  | [optional] 
**default** | **bool** |  | [optional] 
**institution_id** | **str** |  | [optional] 

## Example

```python
from organizze_api.models.credit_card_input import CreditCardInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardInput from a JSON string
credit_card_input_instance = CreditCardInput.from_json(json)
# print the JSON string representation of the object
print(CreditCardInput.to_json())

# convert the object into a dict
credit_card_input_dict = credit_card_input_instance.to_dict()
# create an instance of CreditCardInput from a dict
credit_card_input_from_dict = CreditCardInput.from_dict(credit_card_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


