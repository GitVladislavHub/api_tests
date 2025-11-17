import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    ENDPOINT_GRADE_STATS = f"{ENDPOINT_PREFIX}/stats"
    ENDPOINT_DELETE_GRADE = f"{ENDPOINT_PREFIX}/{{grade_id}}"
    ENDPOINT_PUT_GRADE = f"{ENDPOINT_PREFIX}/{{grade_id}}"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grade(self, json: dict) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_grade(self, grade_id: int) -> requests.Response:
        endpoint = self.ENDPOINT_DELETE_GRADE.format(grade_id=grade_id)
        response = self.api_utils.delete(endpoint)
        return response

    def put_grade(self, grade_id: int, data: dict) -> requests.Response:
        endpoint = self.ENDPOINT_PUT_GRADE.format(grade_id=grade_id)
        response = self.api_utils.put(endpoint, data=data)
        return response

    def get_grades_statistics(self, json: dict) -> requests.Response:
        response = self.api_utils.get(self.ENDPOINT_GRADE_STATS, json=json)
        return response
