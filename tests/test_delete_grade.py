from logger.logger import Logger
from services.university.university_service import UniversityService
from faker import Faker

fake = Faker()


class TestDeleteGrade:
    def test_delete_grade_by_id(self, university_api_utils_admin, create_teacher, create_student, create_grade):
        university_service = UniversityService(university_api_utils_admin)
        Logger.info("### Step 1. Create grade and delete grade")

        delete_grade_response = university_service.delete_grade(grade_id=create_grade.id)

        assert delete_grade_response == {"detail": "Grade deleted"}, \
            (f"Actual: {delete_grade_response}, "
             f"Expected: {{'detail': 'Grade deleted'}}")

    def test_delete_grade_by_id_anonym(self, university_api_utils_anonym, create_teacher,
                                       create_student, create_grade):
        university_service_2 = UniversityService(university_api_utils_anonym)
        Logger.info("### Step 1. Delete grade by id anonym")
        delete_grade_response = university_service_2.delete_grade(grade_id=create_grade.id)

        assert delete_grade_response == {"detail": "Invalid login credentials"}, \
            (f"Actual: {delete_grade_response}, "
             f"Expected: {{'detail': 'Invalid login credentials'}}")
