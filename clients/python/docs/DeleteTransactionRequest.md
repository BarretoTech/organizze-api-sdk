# DeleteTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_future** | **bool** |  | [optional] 
**update_all** | **bool** |  | [optional] 

## Example

```python
from organizze_api.models.delete_transaction_request import DeleteTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTransactionRequest from a JSON string
delete_transaction_request_instance = DeleteTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTransactionRequest.to_json())

# convert the object into a dict
delete_transaction_request_dict = delete_transaction_request_instance.to_dict()
# create an instance of DeleteTransactionRequest from a dict
delete_transaction_request_from_dict = DeleteTransactionRequest.from_dict(delete_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


