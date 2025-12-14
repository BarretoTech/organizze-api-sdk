# InstallmentTransaction

Installment Transaction

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
**tags** | [**List[Tag]**](Tag.md) |  | 
**attachments** | **List[str]** |  | 
**recurrence_id** | **int** |  | 
**installments_attributes** | [**InstallmentTransactionAllOfInstallmentsAttributes**](InstallmentTransactionAllOfInstallmentsAttributes.md) |  | [optional] 

## Example

```python
from organizze_api.models.installment_transaction import InstallmentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InstallmentTransaction from a JSON string
installment_transaction_instance = InstallmentTransaction.from_json(json)
# print the JSON string representation of the object
print(InstallmentTransaction.to_json())

# convert the object into a dict
installment_transaction_dict = installment_transaction_instance.to_dict()
# create an instance of InstallmentTransaction from a dict
installment_transaction_from_dict = InstallmentTransaction.from_dict(installment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


