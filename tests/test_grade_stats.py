import random
from logger.logger import Logger
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService


class TestGradeStats:
    def test_grades_teachers(self, university_api_utils_admin, create_teacher, create_student, create_group):
        university_service = UniversityService(university_api_utils_admin)
        Logger.info("### Step 1.Grade stats teacher")
        grade_data = GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX))
        university_service.create_grade(grade_data)

        grade_response = university_service.get_grade_statistics(teacher_id=create_teacher.id)

        assert grade_response.min == grade_data.grade, \
            (f"Actual{grade_response.min}, "
             f"Expected {grade_data.grade}")
