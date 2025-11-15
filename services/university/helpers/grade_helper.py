import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_grade(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_grade(self, json: dict) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, json=json)
        return response
