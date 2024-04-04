import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url_parameter):
        if isinstance(url_parameter, str):
            self._url = url_parameter

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)