import random
from logger.logger import Logger
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()


class TestCreateGrade:
    def test_create_grade(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)

        Logger.info("### Step 1. Create teacher")
        teacher_data = TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum)))

        teacher_response = university_service.create_teacher(teacher_request=teacher_data)

        Logger.info("### Step 2. Create group")
        group = GroupRequest(name=fake.name())

        group_response = university_service.create_group(group)

        Logger.info("### Step 3. Create student")
        student_data = StudentRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            degree=random.choice(list(DegreeEnum)),
            phone=fake.numerify("+7##########"),
            group_id=group_response.id)

        student_response = university_service.create_student(student_request=student_data)

        Logger.info("### Step 4. Create grade")
        grade_data = GradeRequest(
            teacher_id=teacher_response.id,
            student_id=student_response.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX))

        grade_response = university_service.create_grade(grade_request=grade_data)

        assert grade_response.grade == grade_data.grade, \
            f"Actual: {grade_response.grade}, Expected: {grade_data.grade}"
