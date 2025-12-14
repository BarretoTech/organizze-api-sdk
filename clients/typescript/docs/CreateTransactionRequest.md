
# CreateTransactionRequest


## Properties

Name | Type
------------ | -------------
`description` | string
`date` | Date
`paid` | boolean
`amountCents` | number
`accountId` | number
`categoryId` | number
`notes` | string
`creditCardId` | number
`creditCardInvoiceId` | number
`tags` | [Array&lt;Tag&gt;](Tag.md)
`id` | number
`totalInstallments` | number
`installment` | number
`recurring` | boolean
`attachmentsCount` | number
`paidCreditCardId` | number
`paidCreditCardInvoiceId` | number
`opositeTransactionId` | number
`opositeAccountId` | number
`createdAt` | Date
`updatedAt` | Date
`attachments` | Array&lt;string&gt;
`recurrenceId` | number
`installmentsAttributes` | [InstallmentTransactionAllOfInstallmentsAttributes](InstallmentTransactionAllOfInstallmentsAttributes.md)
`recurrenceAttributes` | [RecurringTransactionAllOfRecurrenceAttributes](RecurringTransactionAllOfRecurrenceAttributes.md)

## Example

```typescript
import type { CreateTransactionRequest } from ''

// TODO: Update the object below with actual values
const example = {
  "description": null,
  "date": null,
  "paid": null,
  "amountCents": null,
  "accountId": null,
  "categoryId": null,
  "notes": null,
  "creditCardId": null,
  "creditCardInvoiceId": null,
  "tags": null,
  "id": null,
  "totalInstallments": null,
  "installment": null,
  "recurring": null,
  "attachmentsCount": null,
  "paidCreditCardId": null,
  "paidCreditCardInvoiceId": null,
  "opositeTransactionId": null,
  "opositeAccountId": null,
  "createdAt": null,
  "updatedAt": null,
  "attachments": null,
  "recurrenceId": null,
  "installmentsAttributes": null,
  "recurrenceAttributes": null,
} satisfies CreateTransactionRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateTransactionRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


