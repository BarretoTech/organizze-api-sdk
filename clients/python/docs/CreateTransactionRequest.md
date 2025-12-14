# CreateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**var_date** | **date** |  | 
**paid** | **bool** |  | 
**amount_cents** | **int** |  | 
**account_id** | **int** | ID of the Bank Account | 
**category_id** | **int** |  | 
**notes** | **str** |  | 
**credit_card_id** | **int** |  | 
**tags** | [**List[Tag]**](Tag.md) |  | 
**id** | **int** | ID of the Transaction | 
**total_installments** | **int** |  | 
**installment** | **int** |  | 
**recurring** | **bool** |  | 
**attachments_count** | **int** |  | 
**credit_card_invoice_id** | **int** |  | 
**paid_credit_card_id** | **int** |  | 
**paid_credit_card_invoice_id** | **int** |  | 
**oposite_transaction_id** | **int** |  | 
**oposite_account_id** | **int** | ID of the Bank Account | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**attachments** | **List[str]** |  | 
**recurrence_id** | **int** |  | 
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


