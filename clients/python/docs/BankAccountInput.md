# BankAccountInput

Schema for creating or updating a bank account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Bank Account | 
**institution_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**default** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from organizze_api.models.bank_account_input import BankAccountInput

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountInput from a JSON string
bank_account_input_instance = BankAccountInput.from_json(json)
# print the JSON string representation of the object
print(BankAccountInput.to_json())

# convert the object into a dict
bank_account_input_dict = bank_account_input_instance.to_dict()
# create an instance of BankAccountInput from a dict
bank_account_input_from_dict = BankAccountInput.from_dict(bank_account_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


