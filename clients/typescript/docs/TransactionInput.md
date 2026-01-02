
# TransactionInput

Schema for creating a transaction

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

## Example

```typescript
import type { TransactionInput } from ''

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
} satisfies TransactionInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TransactionInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


