# InstallmentTransaction

Installment Transaction

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


