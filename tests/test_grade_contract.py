import requests

from services.university.helpers.grade_helper import GradeHelper
from faker import Faker

faker = Faker()


class TestGradeCreate:
    def test_create_grade_anonym(self, university_api_utils_anonym):
        grade_helper = GradeHelper(university_api_utils_anonym)
        response = grade_helper.post_grade(
            {"teacher_id": faker.random_int(min=1, max=10),
             "student_id": faker.random_int(min=1, max=10),
             "grade": faker.pyint(min_value=0, max_value=5)})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code: {response.status_code}, "
             f"Expected: {requests.codes.unauthorized}")

    def test_create_grade_admin(self, university_api_utils_anonym):
        grade_helper = GradeHelper(university_api_utils_anonym)
        response = grade_helper.post_grade(
            {"teacher_id": faker.random_int(min=1, max=10),
             "student_id": faker.random_int(min=1, max=10),
             "grade": faker.pyint(min_value=0, max_value=5)})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            f"Wrong status code: {response.status_code}, Expected: {requests.status_codes.codes.unauthorized} "
