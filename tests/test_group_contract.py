import allure
import requests.status_codes
from faker import Faker

from services.university.helpers.group_helper import GroupHelper
from utils.allure_tags import AllureTag

fake = Faker()

@allure.tag(AllureTag.TEST_CONTRACT)
class TestGroupContract:
    @allure.title("Test create group contract anonym")
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": fake.name()})

        assert response.status_code == 403, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"but expected: {403}")

    @allure.title("Test get group contract admin")
    def test_get_group_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_groups()

        assert response.status_code == requests.status_codes.codes.ok, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.ok}")

    @allure.title("Test get group contract anonym")
    def test_get_groups_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.get_groups()

        assert response.status_code == 403, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {403}")
