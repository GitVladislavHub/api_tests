import random

import requests
from faker import Faker

from services.university.helpers.teacher_helper import TeacherHelper

fake = Faker()


class TestTeacherContract:
    def test_create_teacher_contract(self, university_api_utils_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "subject": "History"
        })

        assert response.status_code == requests.status_codes.codes.created, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.created}")

    def test_create_teacher_contract_anonym(self, university_api_utils_anonym):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        response = teacher_helper.post_teacher({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "subject": "History"
        })

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.unauthorized}")
