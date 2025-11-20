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
    def test_create_grade_anonym(self, university_api_utils_anonym, university_api_utils_admin, create_student,
                                 create_teacher):
        grade_helper = GradeHelper(university_api_utils_anonym)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code: {response.status_code}, "
             f"Expected: {requests.codes.unauthorized}")

    def test_create_grade_admin(self, university_api_utils_admin, create_student, create_teacher):
        grade_helper = GradeHelper(university_api_utils_admin)
        response = grade_helper.post_grade(GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX)).model_dump())

        assert response.status_code == requests.status_codes.codes.created, \
            f"Wrong status code: {response.status_code}, Expected: {requests.status_codes.codes.created} "
