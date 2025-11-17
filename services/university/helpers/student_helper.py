import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    ENDPOINT_STUDENT_ID = f"{ENDPOINT_PREFIX}/student_id"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_students(self, json:dict) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, json=json)
        return response
