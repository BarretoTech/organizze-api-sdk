# CreditCardInvoiceFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**starting_date** | **date** |  | [optional] 
**closing_date** | **date** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**payment_amount_cents** | **int** |  | [optional] 
**balance_cents** | **int** |  | [optional] 
**previous_balance_cents** | **int** |  | [optional] 
**credit_card_id** | **int** |  | [optional] 
**transactions** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**payments** | [**List[Transaction]**](Transaction.md) |  | [optional] 

## Example

```python
from organizze_api.models.credit_card_invoice_full import CreditCardInvoiceFull

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardInvoiceFull from a JSON string
credit_card_invoice_full_instance = CreditCardInvoiceFull.from_json(json)
# print the JSON string representation of the object
print(CreditCardInvoiceFull.to_json())

# convert the object into a dict
credit_card_invoice_full_dict = credit_card_invoice_full_instance.to_dict()
# create an instance of CreditCardInvoiceFull from a dict
credit_card_invoice_full_from_dict = CreditCardInvoiceFull.from_dict(credit_card_invoice_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


