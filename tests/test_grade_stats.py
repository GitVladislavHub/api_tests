import random

from logger.logger import Logger
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService

ALL_GRADES = 10
NORMAL_GRADE = 3


class TestGradeStats:
    def test_grade_stats(self, university_api_utils_admin, create_teacher, create_student, create_group):
        university_service = UniversityService(university_api_utils_admin)
        Logger.info("### Step 1. Берем статистику оценок")

        statistic_response = university_service.get_grade_statistics()

        assert statistic_response.min == GRADE_MIN, f" Actual {statistic_response.min}, Expected {GRADE_MIN}"
        assert statistic_response.max == GRADE_MAX, f" Actual {statistic_response.max}, Expected {GRADE_MAX}"

    def filter_student_grades(self, university_api_utils_admin, create_student, create_teacher):
        university_service = UniversityService(university_api_utils_admin)
        grade_data = GradeRequest(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX))

        created_grade_response = university_service.create_grade(grade_data)
        assert created_grade_response.grade

        all_grades = university_service.get_grades()

        good_grades = [grade for grade in all_grades if grade.grade > NORMAL_GRADE]

        student_ids_with_good_grades = list(set(grade.student_id for grade in good_grades))

        if created_grade_response.grade > NORMAL_GRADE:
            assert create_student.id in student_ids_with_good_grades
        else:
            assert create_student.id not in student_ids_with_good_grades
