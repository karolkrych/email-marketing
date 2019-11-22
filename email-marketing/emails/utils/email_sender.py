import requests
from requests import Response
from emails.utils import EmailGenerator


class EmailSender:
    def __init__(self, generator: EmailGenerator) -> None:
        self.generator = generator

    def send(self) -> Response:
        return requests.post(
            self.generator.ENDPOINT_API,
            json=self.generator.get_data(),
            auth=self.generator.get_auth()
        )
