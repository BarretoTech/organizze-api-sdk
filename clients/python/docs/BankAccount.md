# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Bank Account | 
**name** | **str** | Name of the Bank Account | 
**institution_id** | **str** |  | 
**institution_name** | **str** |  | 
**description** | **str** |  | 
**kind** | **str** |  | [optional] 
**archived** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**default** | **bool** |  | 
**type** | **str** |  | [optional] 

## Example

```python
from organizze_api.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


