from conftest import create_teacher
from logger.logger import Logger
from services.university.university_service import UniversityService


class TestDeleteTeacher:
    def test_delete_teacher(self, university_api_utils_admin, create_teacher):
        university_service = UniversityService(university_api_utils_admin, )
        Logger.info("### Step 1.Create teacher ")
        teacher_id_to_delete_response = create_teacher.id
        Logger.info("### Step 2.Delete teacher ")
        delete_response = university_service.delete_teacher(teacher_id_to_delete_response)

        assert delete_response == {"detail": "Teacher deleted"}, \
            (f"Actual: {delete_response}, "
             f"Expected: {{'detail': 'Teacher deleted'}}")
