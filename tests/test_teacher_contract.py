import requests
from faker import Faker

from services.university.helpers.teacher_helper import TeacherHelper

fake = Faker()



class TestTeacherContract:
    def test_create_teacher_contract(self, university_api_utils_anonym):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        response = teacher_helper.post_teacher({"name": fake.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.unauthorized}")
