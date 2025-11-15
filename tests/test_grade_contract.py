from services.university.helpers.grade_helper import GradeHelper
from faker import Faker

faker = Faker()


class TestGradeCreate:
    def test_create_grade_anonym(self, university_api_utils_admin):
        grade_helper = GradeHelper(university_api_utils_admin)
        response = grade_helper.post_grade({"grade": faker.pyint(min_value=0, max_value=5)})

        assert response.status_code == 201, \
            f"wrong status code: {response.status_code}, but expected 201"
