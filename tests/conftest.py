import random
import time

import pytest
import requests

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker

fake = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_itils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_itils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = fake.user_name()
    password = fake.password(length=30,
                             special_chars=True,
                             digits=True,
                             upper_case=True,
                             lower_case=True)
    auth_service.register_user(register_request=RegisterRequest(
        username=username,
        password=password,
        password_repeat=password,
        email=fake.email()))
    login_response = auth_service.login_user(login_request=LoginRequest(
        username=username,
        password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=True)
def auth_service_readiness():
    """Готовность сервиса авторизация"""
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.' ")


@pytest.fixture(scope="function", autouse=True)
def university_service_readiness():
    """Готовность сервиса университет"""
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(UniversityService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.' ")


@pytest.fixture(scope="function")
def create_teacher(university_api_utils_admin):
    """Создание учителя"""
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher_data = TeacherRequest(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    teacher_response = university_service.create_teacher(teacher_request=teacher_data)
    return teacher_response


@pytest.fixture(scope="function")
def create_group(university_api_utils_admin):
    """Создание группы"""
    university_service = UniversityService(api_utils=university_api_utils_admin)
    group = GroupRequest(name=fake.name())
    group_response = university_service.create_group(group)
    return group_response


@pytest.fixture(scope="function")
def create_student(university_api_utils_admin, create_group):
    """Создание студента"""
    university_service = UniversityService(api_utils=university_api_utils_admin)
    student_data = StudentRequest(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        degree=random.choice(list(DegreeEnum)),
        phone=fake.numerify("+7##########"),
        group_id=create_group.id
    )
    student_response = university_service.create_student(student_request=student_data)
    return student_response
