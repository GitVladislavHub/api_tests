import random
from logger.logger import Logger
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()


class TestCreateGrade:
    def test_create_grade(self, university_api_utils_admin, create_teacher, create_student):
        university_service = UniversityService(api_utils=university_api_utils_admin)

        Logger.info("### Step 1. Create grade")
        grade_data = GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX))

        grade_response = university_service.create_grade(grade_request=grade_data)

        assert grade_response.grade == grade_data.grade, \
            f"Actual: {grade_response.grade}, Expected: {grade_data.grade}"
