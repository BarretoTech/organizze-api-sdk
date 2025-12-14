
# Budget


## Properties

Name | Type
------------ | -------------
`amountInCents` | number
`categoryId` | number
`date` | Date
`activityType` | number
`total` | number
`predictedTotal` | number
`percentage` | string

## Example

```typescript
import type { Budget } from ''

// TODO: Update the object below with actual values
const example = {
  "amountInCents": null,
  "categoryId": null,
  "date": null,
  "activityType": null,
  "total": null,
  "predictedTotal": null,
  "percentage": null,
} satisfies Budget

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Budget
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


