import random

from logger.logger import Logger
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()


class TestDeleteGrade:
    def test_delete_grade_by_id(self, university_api_utils_admin, create_teacher, create_student):
        university_service = UniversityService(university_api_utils_admin)
        Logger.info("### Step 1. Create grade")
        grade_data = GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX))

        created_grade_response = university_service.create_grade(grade_data)

        Logger.info("### Step 2. Delete grade by id")
        delete_grade_response = university_service.delete_grade(grade_id=created_grade_response.id)

        assert delete_grade_response == {"detail": "Grade deleted"}, \
            (f"Actual: {delete_grade_response}, "
             f"Expected: {{'detail': 'Grade deleted'}}")

    def test_delete_grade_by_id_anonym(self, university_api_utils_anonym, university_api_utils_admin, create_teacher, create_student):
        university_service = UniversityService(university_api_utils_admin)
        Logger.info("### Step 1. Create grade")
        grade_data = GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX))

        created_grade_response = university_service.create_grade(grade_data)

        university_service_2 = UniversityService(university_api_utils_anonym)
        Logger.info("### Step 2. Delete grade by id anonym")
        delete_grade_response = university_service_2.delete_grade(grade_id=created_grade_response.id)

        assert delete_grade_response == {"detail": "Invalid login credentials"}, \
            (f"Actual: {delete_grade_response}, "
             f"Expected: {{'detail': 'Invalid login credentials'}}")
