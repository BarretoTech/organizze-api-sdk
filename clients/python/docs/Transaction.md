# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Transaction | [optional] 
**description** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**paid** | **bool** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**total_installments** | **int** |  | [optional] 
**installment** | **int** |  | [optional] 
**recurring** | **bool** |  | [optional] 
**account_id** | **int** | ID of the Bank Account | [optional] 
**account_type** | **str** |  | [optional] 
**category_id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**attachments_count** | **int** |  | [optional] 
**credit_card_id** | **int** |  | [optional] 
**credit_card_invoice_id** | **int** |  | [optional] 
**paid_credit_card_id** | **int** |  | [optional] 
**paid_credit_card_invoice_id** | **int** |  | [optional] 
**oposite_transaction_id** | **int** |  | [optional] 
**oposite_account_id** | **int** | ID of the Bank Account | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**attachments** | **List[str]** |  | [optional] 

## Example

```python
from organizze_api.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


