import random

import allure
import requests
from services.university.helpers.grade_helper import GradeHelper
from faker import Faker

from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest

from utils.allure_tags import AllureTag

fake = Faker()


@allure.tag(AllureTag.CREATE_USER)
class TestGradeCreate:
    def test_create_grade_anonym(self, university_api_utils_anonym, university_api_utils_admin, create_student,
                                 create_teacher):
        grade_helper = GradeHelper(university_api_utils_anonym)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == 403, \
            (f"Wrong status code: {response.status_code}, "
             f"Expected: {403}")

    def test_create_grade_admin(self, university_api_utils_admin, create_student, create_teacher):
        grade_helper = GradeHelper(university_api_utils_admin)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            f"Wrong status code: {response.status_code}, Expected: {requests.status_codes.codes.created} "
