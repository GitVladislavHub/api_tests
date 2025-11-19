from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()


class TestGradeStats:
    def test_grade_statistics_filter(self, university_api_utils_admin, create_teacher, create_student):
        university_service = UniversityService(university_api_utils_admin)

        grades = [3, 4, 5, 2, 4]

        for grade in grades:
            grade_data = GradeRequest(
                teacher_id=create_teacher.id,
                student_id=create_student.id,
                grade=grade
            )
            university_service.create_grade(grade_data)

        stats = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
            student_id=create_student.id
        )

        assert stats.avg == sum(grades) / len(grades)

    def test_grade_student_statistics(self, university_api_utils_admin, create_teacher, create_student):
        university_service = UniversityService(university_api_utils_admin)
        grades_student = [1, 2]

        for grade in grades_student:
            grade_data_student = GradeRequest(
                teacher_id=create_teacher.id,
                student_id=create_student.id,
                grade=grade
            )
            university_service.create_grade(grade_data_student)

        stats_student = university_service.get_grade_statistics(
            student_id=create_student.id,
        )
        assert stats_student.avg == sum(grades_student) / len(grades_student)

    def test_grade_teacher_statistics(self, university_api_utils_admin, create_teacher, create_student):
        university_service = UniversityService(university_api_utils_admin)
        grades_teacher = [3, 4]

        for grade in grades_teacher:
            grade_data_teacher = GradeRequest(
                teacher_id=create_teacher.id,
                student_id=create_student.id,
                grade=grade
            )
            university_service.create_grade(grade_data_teacher)

        stats_teacher = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
        )
        assert stats_teacher.count == len(grades_teacher)
