# JSON-API-Kit
Python library for working with JSON web API's

### Preface
 
 This package is a work in progress. Readme is currently a framework of how I want the package to work.

### Requirements

requests

### Getting Started

First make a client and then create a resource with the client:

```python
from josn_api_kit import APIClient
from json_api_kit import APIResource

client = APIClient('<username>', '<password>', '<host-url>')

users_resource = APIResource(client, '/users')

john = users_resource.get_one('johns-username')

```
