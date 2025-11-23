import random

import allure
from allure_commons.types import Severity
from faker import Faker
from logger.logger import Logger
from services.university.models.base_student import DegreeEnum
from services.university.models.student_request import StudentRequest
from services.university.university_service import UniversityService
from utils.allure_tags import AllureTag

fake = Faker()


@allure.tag(AllureTag.TEST_CONTRACT, AllureTag.CREATE_USER)
@allure.severity(Severity.CRITICAL)
class TestStudentCreate:
    @allure.title("Test create student contract admin")
    def test_student_create(self, university_api_utils_admin, create_group):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        Logger.info("### Step 1. Create student and student in a group")
        student = StudentRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            degree=random.choice([option for option in DegreeEnum]),
            phone=fake.numerify("+7##########"),
            group_id=create_group.id
        )

        student_response = university_service.create_student(student_request=student)

        assert student_response.group_id == create_group.id, \
            f"Wrong group id. Actual: '{student_response.group_id}', but expected: '{create_group.id}'"
