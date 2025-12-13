# CreateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Transaction | [optional] 
**description** | **str** |  | 
**var_date** | **date** |  | 
**paid** | **bool** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**total_installments** | **int** |  | [optional] 
**installment** | **int** |  | [optional] 
**recurring** | **bool** |  | [optional] 
**account_id** | **int** | ID of the Bank Account | [optional] 
**account_type** | **str** |  | [optional] 
**category_id** | **int** |  | [optional] 
**notes** | **str** |  | 
**attachments_count** | **int** |  | [optional] 
**credit_card_id** | **int** |  | [optional] 
**credit_card_invoice_id** | **int** |  | [optional] 
**paid_credit_card_id** | **int** |  | [optional] 
**paid_credit_card_invoice_id** | **int** |  | [optional] 
**oposite_transaction_id** | **int** |  | [optional] 
**oposite_account_id** | **int** | ID of the Bank Account | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**installments_attributes** | [**InstallmentTransactionAllOfInstallmentsAttributes**](InstallmentTransactionAllOfInstallmentsAttributes.md) |  | [optional] 
**recurrence_attributes** | [**RecurringTransactionAllOfRecurrenceAttributes**](RecurringTransactionAllOfRecurrenceAttributes.md) |  | 

## Example

```python
from organizze_api.models.create_transaction_request import CreateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionRequest from a JSON string
create_transaction_request_instance = CreateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionRequest.to_json())

# convert the object into a dict
create_transaction_request_dict = create_transaction_request_instance.to_dict()
# create an instance of CreateTransactionRequest from a dict
create_transaction_request_from_dict = CreateTransactionRequest.from_dict(create_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


