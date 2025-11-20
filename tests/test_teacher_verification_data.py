import random

from faker import Faker
from logger.logger import Logger
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService

fake = Faker()


class TestTeacherCreate:
    def test_create_teacher_returns_correct_subject(self, university_api_utils_admin):
        Logger.info("### Step 1. Create teacher")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        teacher_data = TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice([subject for subject in SubjectEnum])
        )

        teacher_response = university_service.create_teacher(teacher_request=teacher_data)

        assert teacher_response.subject == teacher_data.subject
