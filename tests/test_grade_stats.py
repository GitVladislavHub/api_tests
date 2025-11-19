import random
from logger.logger import Logger
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher_model import SubjectEnum
from services.university.models.grade_base_model import GRADE_MIN, GRADE_MAX
from services.university.models.grade_request import GradeRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()


class TestGradeStats:
    def test_grade_statistics_filtering(self, university_api_utils_admin, create_teacher, create_student, create_group):
        university_service = UniversityService(university_api_utils_admin)

        teacher2 = TeacherRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            subject=random.choice(list(SubjectEnum)))
        teacher2 = university_service.create_teacher(teacher_request=teacher2)

        student2 = StudentRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            degree=random.choice([option for option in DegreeEnum]),
            phone=fake.numerify("+7##########"),
            group_id=create_group.id
        )
        student2 = university_service.create_student(student_request=student2)

        suitable_grades = [3, 4, 5]
        for grade in suitable_grades:
            grade_data = GradeRequest(
                teacher_id=create_teacher.id,
                student_id=create_student.id,
                grade=grade
            )
            university_service.create_grade(grade_data)

        grade_data_1 = GradeRequest(
            teacher_id=teacher2.id,
            student_id=create_student.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX)
        )
        university_service.create_grade(grade_data_1)

        grade_data_2 = GradeRequest(
            teacher_id=create_teacher.id,
            student_id=student2.id,
            grade=random.randint(GRADE_MIN, GRADE_MAX)
        )
        university_service.create_grade(grade_data_2)

        stats = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
            student_id=create_student.id
        )

        assert stats.avg == sum(suitable_grades) / len(suitable_grades)
