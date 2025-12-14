
# UpdateTransactionRequest


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
`tags` | [Array&lt;Tag&gt;](Tag.md)
`updateFuture` | boolean
`updateAll` | boolean

## Example

```typescript
import type { UpdateTransactionRequest } from ''

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
  "tags": null,
  "updateFuture": null,
  "updateAll": null,
} satisfies UpdateTransactionRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UpdateTransactionRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


