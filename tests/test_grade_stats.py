from logger.logger import Logger
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.university_service import UniversityService

ALL_GRADES = 10
COUNT_GRADES = 51


class TestGradeStats:
    def test_grade_stats(self, university_api_utils_admin, create_teacher, create_student, create_group):
        university_service = UniversityService(university_api_utils_admin)
        Logger.info("### Step 1. Берем статистику оценок")

        statistic_response = university_service.get_grade_statistics()

        assert statistic_response.count == COUNT_GRADES, f" Actual {statistic_response.count}, Expected {COUNT_GRADES}"
        assert statistic_response.min == GRADE_MIN, f" Actual {statistic_response.min}, Expected {GRADE_MIN}"
        assert statistic_response.max == GRADE_MAX, f" Actual {statistic_response.max}, Expected {GRADE_MAX}"
