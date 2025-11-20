import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    ENDPOINT_GROUP_ID = f"{ENDPOINT_PREFIX}/{{group_id}}"

    def get_groups(self) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_group(self, group_id: int) -> requests.Response:
        endpoint = self.ENDPOINT_GROUP_ID.format(group_id=group_id)
        response = self.api_utils.delete(endpoint)
        return response

    def put_group(self, group_id: int, json: dict) -> requests.Response:
        endpoint = self.ENDPOINT_GROUP_ID.format(group_id=group_id)
        response = self.api_utils.put(endpoint, json=json)
        return response
