# FailedAuthentication

Failed Authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 

## Example

```python
from organizze_api.models.failed_authentication import FailedAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of FailedAuthentication from a JSON string
failed_authentication_instance = FailedAuthentication.from_json(json)
# print the JSON string representation of the object
print(FailedAuthentication.to_json())

# convert the object into a dict
failed_authentication_dict = failed_authentication_instance.to_dict()
# create an instance of FailedAuthentication from a dict
failed_authentication_from_dict = FailedAuthentication.from_dict(failed_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


