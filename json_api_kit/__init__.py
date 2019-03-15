import json

import requests

class APIClient:

    def __init__(self, username, password, host_url):
        self.username = username
        self.password = password
        self.base_url = host_url
        self.transport = requests.Session()
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get(self, path, data=None, params=None):
        url = self.base_url + path
        auth = (self.username, self.password)
        return self.transport.get(url, auth=auth, data=data, params=params, headers=self.headers)

    def post(self, path, data=None, params=None):
        url = self.base_url + path
        auth = (self.username, self.password)
        return self.transport.post(url, auth=auth, data=data, params=params, headers=self.headers)

    def put(self, path, data=None, params=None):
        url = self.base_url + path
        auth = (self.username, self.password)
        return self.transport.put(url, auth=auth, data=data, params=params, headers=self.headers)

    def delete(self, path, data=None, params=None):
        url = self.base_url + path
        auth = (self.username, self.password)
        return self.transport.delete(url, auth=auth, data=data, params=params, headers=self.headers)

    def do_request(self, method, path, data=None, params=None):
        url = self.base_url + path
        auth = (self.username, self.password)
        req = requests.Request(method, url, auth=auth, data=data, params=params, headers=self.headers)
        return self.transport.send(req.prepare())


def _get_json_from_response(response):
    try:
        data = json.loads(response.text)
    except json.JSONDecodeError:
        # Response body was not JSON or not good JSON
        data = response.text

    return data


class APIResource:

    def __init__(self, client, endpoint, create_method='POST', update_method='PUT'):
        self.endpoint = endpoint
        self.client = client
        self.create_method = create_method
        self.update_method = update_method

    def get_one(self, target):
        path = self.endpoint + '/' + target
        r = self.client.get(path)
        return _get_json_from_response(r)
