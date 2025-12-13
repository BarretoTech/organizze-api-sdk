# TransactionInput

Schema for creating a transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**var_date** | **date** |  | 
**paid** | **bool** |  | [optional] 
**amount_cents** | **int** |  | 
**account_id** | **int** | ID of the Bank Account | [optional] 
**category_id** | **int** |  | 
**notes** | **str** |  | [optional] 
**credit_card_id** | **int** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 

## Example

```python
from organizze_api.models.transaction_input import TransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInput from a JSON string
transaction_input_instance = TransactionInput.from_json(json)
# print the JSON string representation of the object
print(TransactionInput.to_json())

# convert the object into a dict
transaction_input_dict = transaction_input_instance.to_dict()
# create an instance of TransactionInput from a dict
transaction_input_from_dict = TransactionInput.from_dict(transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


