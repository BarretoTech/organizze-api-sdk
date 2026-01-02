# UpdateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**paid** | **bool** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**account_id** | **int** | ID of the Bank Account | [optional] 
**category_id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**credit_card_id** | **int** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**update_future** | **bool** |  | [optional] 
**update_all** | **bool** |  | [optional] 

## Example

```python
from organizze_api.models.update_transaction_request import UpdateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionRequest from a JSON string
update_transaction_request_instance = UpdateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionRequest.to_json())

# convert the object into a dict
update_transaction_request_dict = update_transaction_request_instance.to_dict()
# create an instance of UpdateTransactionRequest from a dict
update_transaction_request_from_dict = UpdateTransactionRequest.from_dict(update_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


