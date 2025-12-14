
# CategoryInput

Schema for creating or updating a category

## Properties

Name | Type
------------ | -------------
`name` | string
`color` | string
`parentId` | number
`groupId` | string
`fixed` | boolean
`essential` | boolean

## Example

```typescript
import type { CategoryInput } from ''

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "color": null,
  "parentId": null,
  "groupId": null,
  "fixed": null,
  "essential": null,
} satisfies CategoryInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CategoryInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


