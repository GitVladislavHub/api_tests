import random
import requests

from services.university.helpers.grade_helper import GradeHelper
from faker import Faker

from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest

faker = Faker()


class TestGradeCreate:
    def test_create_grade_anonym(self, university_api_utils_anonym):
        grade_helper = GradeHelper(university_api_utils_anonym)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=faker.random_int(min=1, max=10),
            student_id=faker.random_int(min=1, max=10),
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code: {response.status_code}, "
             f"Expected: {requests.codes.unauthorized}")

    def test_create_grade_admin(self, university_api_utils_admin):
        grade_helper = GradeHelper(university_api_utils_admin)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=faker.random_int(min=1, max=10),
            student_id=faker.random_int(min=1, max=10),
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            f"Wrong status code: {response.status_code}, Expected: {requests.status_codes.codes.created} "
