from abc import ABC

from requests.auth import AuthBase


class EmailGenerator(ABC):

    ENDPOINT_API: str

    def get_auth(self) -> AuthBase:
        raise NotImplementedError

    def get_data(self) -> dict:
        raise NotImplementedError
