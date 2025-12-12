# RecurringTransaction

Recurring Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Bank Account | [optional] 
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
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**recurrence_attributes** | [**RecurringTransactionAllOfRecurrenceAttributes**](RecurringTransactionAllOfRecurrenceAttributes.md) |  | 

## Example

```python
from organizze_api.models.recurring_transaction import RecurringTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringTransaction from a JSON string
recurring_transaction_instance = RecurringTransaction.from_json(json)
# print the JSON string representation of the object
print(RecurringTransaction.to_json())

# convert the object into a dict
recurring_transaction_dict = recurring_transaction_instance.to_dict()
# create an instance of RecurringTransaction from a dict
recurring_transaction_from_dict = RecurringTransaction.from_dict(recurring_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


