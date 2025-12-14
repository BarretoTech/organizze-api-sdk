
# CreditCardInvoice


## Properties

Name | Type
------------ | -------------
`id` | number
`date` | Date
`startingDate` | Date
`closingDate` | Date
`amountCents` | number
`paymentAmountCents` | number
`balanceCents` | number
`previousBalanceCents` | number
`creditCardId` | number

## Example

```typescript
import type { CreditCardInvoice } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "date": null,
  "startingDate": null,
  "closingDate": null,
  "amountCents": null,
  "paymentAmountCents": null,
  "balanceCents": null,
  "previousBalanceCents": null,
  "creditCardId": null,
} satisfies CreditCardInvoice

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreditCardInvoice
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


