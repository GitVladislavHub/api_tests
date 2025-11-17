import random

import requests
from faker import Faker

from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.teacher_request import TeacherRequest

fake = Faker()


class TestTeacherContract:
    def test_create_authorized_teacher_admin(self, university_api_utils_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.created}")

    def test_create_unauthorized_teacher_anonym(self, university_api_utils_anonym):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        response = teacher_helper.post_teacher({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "subject": "History"
        })

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.unauthorized}")

    def test_get_teacher_admin(self, university_api_utils_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.created}")

    def test_get_anonym(self, university_api_utils_anonym):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.created}")
