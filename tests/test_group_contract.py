import requests.status_codes
from faker import Faker

from services.university.helpers.group_helper import GroupHelper

fake = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": fake.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"but expected: {requests.status_codes.codes.unauthorized}")

    def test_get_group(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_groups()

        assert response.status_code == requests.status_codes.codes.ok, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.ok}")

    def test_get_groups_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.get_groups()

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"Expected: {requests.status_codes.codes.unauthorized}")
