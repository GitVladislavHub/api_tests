import allure

from services.university.helpers.grade_helper import GradeHelper
from utils.allure_tags import AllureTag


@allure.tag(AllureTag.TEST_CONTRACT)
class TestGradeStatsContract:
    @allure.title("Test grade stats contract")
    def test_grade_stats(self, university_api_utils_admin):
        grade_stats_helper = GradeHelper(api_utils=university_api_utils_admin)

        response = grade_stats_helper.get_grades_stats()

        assert response.status_code == 200, f"Actual: {response.status_code}, Expected 200"

    @allure.title("Test grade stats contract anonym")
    def test_grade_stats_anonym(self, university_api_utils_anonym):
        grade_stats_helper = GradeHelper(api_utils=university_api_utils_anonym)

        response = grade_stats_helper.get_grades_stats()

        assert response.status_code == 401, f"Actual: {response.status_code}, Expected 401"
