# RecurringTransaction

Recurring Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Transaction | 
**description** | **str** |  | 
**var_date** | **date** |  | 
**paid** | **bool** |  | 
**amount_cents** | **int** |  | 
**total_installments** | **int** |  | 
**installment** | **int** |  | 
**recurring** | **bool** |  | 
**account_id** | **int** | ID of the Bank Account | 
**category_id** | **int** |  | 
**notes** | **str** |  | 
**attachments_count** | **int** |  | 
**credit_card_id** | **int** |  | 
**credit_card_invoice_id** | **int** |  | 
**paid_credit_card_id** | **int** |  | 
**paid_credit_card_invoice_id** | **int** |  | 
**oposite_transaction_id** | **int** |  | 
**oposite_account_id** | **int** | ID of the Bank Account | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**tags** | [**TransactionTags**](TransactionTags.md) |  | 
**attachments** | **List[str]** |  | 
**recurrence_id** | **int** |  | 
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


