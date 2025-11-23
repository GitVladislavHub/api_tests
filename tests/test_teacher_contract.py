import random

import allure
import requests
from faker import Faker

from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.teacher_request import TeacherRequest
from utils.allure_tags import AllureTag

fake = Faker()


@allure.tag(AllureTag.TEST_CONTRACT, AllureTag.CREATE_USER, AllureTag.GET_USER)
class TestTeacherContract:
    @allure.title("Test create teacher contract admin")
    def test_create_authorized_teacher_admin(self, university_api_utils_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.created}")

    @allure.title("Test create teacher contract anonym")
    def test_create_unauthorized_teacher_anonym(self, university_api_utils_anonym):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        response = teacher_helper.post_teacher({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "subject": random.choice(list(SubjectEnum))
        })

        assert response.status_code == 403, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {403}")

    @allure.title("Test get teacher contract admin")
    def test_get_teacher_admin(self, university_api_utils_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.created}")

    @allure.title("Test get teacher contract anonym")
    def test_get_anonym(self, university_api_utils_anonym):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())

        assert response.status_code == 403, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {403}")
