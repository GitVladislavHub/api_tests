import random
import requests
from services.university.helpers.grade_helper import GradeHelper
from faker import Faker
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.models.teacher_request import TeacherRequest

fake = Faker()


class TestGradeCreate:
    def test_data(self, university_api_utils_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher(TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum))).model_dump())
        teacher_id = response.json()["id"]
        return teacher_id

    def test_create_grade_anonym(self, university_api_utils_anonym, university_api_utils_admin):
        teacher_id = self.test_data(university_api_utils_admin)

        grade_helper = GradeHelper(university_api_utils_anonym)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=teacher_id,
            student_id=1,
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code: {response.status_code}, "
             f"Expected: {requests.codes.unauthorized}")

    def test_create_grade_admin(self, university_api_utils_admin):
        teacher_id = self.test_data(university_api_utils_admin)
        grade_helper = GradeHelper(university_api_utils_admin)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=teacher_id,
            student_id=1,
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            f"Wrong status code: {response.status_code}, Expected: {requests.status_codes.codes.created} "
