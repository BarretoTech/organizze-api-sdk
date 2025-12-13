# CreditCardInvoiceFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**var_date** | **date** |  | 
**starting_date** | **date** |  | 
**closing_date** | **date** |  | 
**amount_cents** | **int** |  | 
**payment_amount_cents** | **int** |  | 
**balance_cents** | **int** |  | 
**previous_balance_cents** | **int** |  | 
**credit_card_id** | **int** |  | 
**transactions** | [**List[Transaction]**](Transaction.md) |  | 
**payments** | [**List[Transaction]**](Transaction.md) |  | 

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


