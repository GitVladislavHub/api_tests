from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()
NUM_GRADES = 5


class TestGradeStats:
    def test_grade_statistics_filter(self, university_api_utils_admin, create_teacher, create_student,
                                     create_grades_for_teacher_student):
        university_service = UniversityService(university_api_utils_admin)
        grades = create_grades_for_teacher_student(num_grades=NUM_GRADES)

        stats = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
            student_id=create_student.id
        )

        assert stats.avg == sum(grades) / len(grades), \
            (f"Actual: {stats.avg:.2f}, "
             f"Expected: {sum(grades) / len(grades):.2f}")

    def test_grade_student_statistics(self, university_api_utils_admin, create_teacher, create_student,
                                      create_grades_for_teacher_student):
        university_service = UniversityService(university_api_utils_admin)
        grades_student = create_grades_for_teacher_student(num_grades=NUM_GRADES)

        stats_student = university_service.get_grade_statistics(
            student_id=create_student.id,
        )
        assert stats_student.avg == sum(grades_student) / len(grades_student), \
            (f"Actual: {stats_student.avg:.2f}, "
             f"Expected: {sum(grades_student) / len(grades_student):.2f}")

    def test_grade_teacher_statistic_filter(self, university_api_utils_admin, create_teacher, create_student,
                                            create_grades_for_teacher_student):
        university_service = UniversityService(university_api_utils_admin)
        grades_teacher = create_grades_for_teacher_student(num_grades=NUM_GRADES)

        stats_teacher = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
        )
        assert stats_teacher.count == len(grades_teacher), \
            (f"Actual: {stats_teacher.count}, "
             f"Expected: {len(grades_teacher)}")

    def test_grade_group_statistic_filter(self, university_api_utils_admin, create_teacher, create_student,
                                          create_grades_for_teacher_student, create_group):
        university_service = UniversityService(university_api_utils_admin)

        grades = create_grades_for_teacher_student(num_grades=NUM_GRADES)

        filter_stats_group_grade = university_service.get_grade_statistics(
            group_id=create_group.id
        )
        assert filter_stats_group_grade.count == len(grades)

    def test_combine_filter_stats(self, university_api_utils_admin, create_teacher, create_student,
                                  create_grades_for_teacher_student, create_group):
        university_service = UniversityService(university_api_utils_admin)

        grades = create_grades_for_teacher_student(num_grades=NUM_GRADES)

        stats = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
            student_id=create_student.id,
            group_id=create_group.id
        )
        assert stats.count == len(grades), \
            (f"Actual: {stats.count}, "
             f"Expected: {len(grades)}")

    def test_grade_teacher_group_statistic_filter(self, university_api_utils_admin, create_teacher, create_student,
                                                  create_grades_for_teacher_student, create_group):
        university_service = UniversityService(university_api_utils_admin)

        grades = create_grades_for_teacher_student(num_grades=NUM_GRADES)

        stats = university_service.get_grade_statistics(
            teacher_id=create_teacher.id,
            group_id=create_group.id
        )

        assert stats.avg == sum(grades) / len(grades), \
            (f"Actual: {stats.avg:.2f}, "
             f"Expected: {sum(grades) / len(grades):.2f}")
