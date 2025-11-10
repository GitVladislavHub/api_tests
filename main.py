import random

import requests
from faker import Faker

AUTH_URL = "http://127.0.0.1:8000"
UNIVERSITY_URL = "http://127.0.0.1:8001"

REGISTER_ENDPOINT = "/auth/register/"
LOGIN_ENDPOINT = "/auth/login/"
ME_ENDPOINT = "/users/me/"
GROUPS_ENDPOINT = "/groups/"
STUDENTS_ENDPOINT = "/students/"

faker = Faker()

username = faker.user_name()
password = faker.word() + "!$<1"

response_register = requests.post(AUTH_URL + REGISTER_ENDPOINT, data={"username": username,
                                                                      "password": password,
                                                                      "password_repeat": password,
                                                                      "email": faker.email()})

response_password = requests.post(AUTH_URL + LOGIN_ENDPOINT, data={"username": username,
                                                                   "password": password,
                                                                   })

access_token = response_password.json()["access_token"]

response_token = requests.get(AUTH_URL + ME_ENDPOINT, headers={"Authorization": f"Bearer {access_token}"})

response_group = requests.post(UNIVERSITY_URL + GROUPS_ENDPOINT, json={"name": faker.name()},
                               headers={"Authorization": f"Bearer {access_token}"})

response = requests.post(UNIVERSITY_URL + STUDENTS_ENDPOINT, json={"first_name": faker.first_name(),
                                                                   "last_name": faker.last_name(),
                                                                   "email": faker.email(),
                                                                   "degree": random.choice(["Associate",
                                                                                            "Bachelor",
                                                                                            "Master",
                                                                                            "Doctorate"]),
                                                                   "phone": faker.numerify("+798968565109"),
                                                                   "group_id": response_group.json()["id"], },
                         headers={"Authorization": f"Bearer {access_token}"})
print(response.status_code)
print(response.json())
