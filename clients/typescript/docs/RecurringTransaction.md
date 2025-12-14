
# RecurringTransaction

Recurring Transaction

## Properties

Name | Type
------------ | -------------
`id` | number
`description` | string
`date` | Date
`paid` | boolean
`amountCents` | number
`totalInstallments` | number
`installment` | number
`recurring` | boolean
`accountId` | number
`categoryId` | number
`notes` | string
`attachmentsCount` | number
`creditCardId` | number
`creditCardInvoiceId` | number
`paidCreditCardId` | number
`paidCreditCardInvoiceId` | number
`opositeTransactionId` | number
`opositeAccountId` | number
`createdAt` | Date
`updatedAt` | Date
`tags` | [Array&lt;Tag&gt;](Tag.md)
`attachments` | Array&lt;string&gt;
`recurrenceId` | number
`recurrenceAttributes` | [RecurringTransactionAllOfRecurrenceAttributes](RecurringTransactionAllOfRecurrenceAttributes.md)

## Example

```typescript
import type { RecurringTransaction } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "description": null,
  "date": null,
  "paid": null,
  "amountCents": null,
  "totalInstallments": null,
  "installment": null,
  "recurring": null,
  "accountId": null,
  "categoryId": null,
  "notes": null,
  "attachmentsCount": null,
  "creditCardId": null,
  "creditCardInvoiceId": null,
  "paidCreditCardId": null,
  "paidCreditCardInvoiceId": null,
  "opositeTransactionId": null,
  "opositeAccountId": null,
  "createdAt": null,
  "updatedAt": null,
  "tags": null,
  "attachments": null,
  "recurrenceId": null,
  "recurrenceAttributes": null,
} satisfies RecurringTransaction

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RecurringTransaction
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


