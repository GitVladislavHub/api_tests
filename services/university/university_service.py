from services.general.base_service import BaseService
from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_response import GradeResponse
from services.university.models.grade_statistic_response import GradeStatisticResponse
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from services.university.models.teacher_request import TeacherRequest
from services.university.models.teacher_response import TeacherResponse
from utils.api_utils import ApiUtils
from typing import List, Optional


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.student_helper = StudentHelper(self.api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_random_student(self):
        raise NotImplementedError

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def delete_teacher(self, teacher_id: int) -> dict:
        response = self.teacher_helper.delete_teacher(teacher_id=teacher_id)
        return response.json()

    def update_teacher(self, teacher_id: int, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.put_teacher(teacher_id=teacher_id, json=teacher_request.model_dump())
        return response.json()

    def create_grade(self, grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.post_grade(data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def delete_grade(self, grade_id: int) -> dict:
        response = self.grade_helper.delete_grade(grade_id=grade_id)
        return response.json()

    def update_grade(self, grade_id: int, grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.put_grade(grade_id=grade_id, data=grade_request.model_dump())
        return response.json()

    def get_grade_statistics(self,
                             student_id: int = None,
                             teacher_id: int = None,
                             group_id: int = None) -> GradeStatisticResponse:
        response = self.grade_helper.get_grades_stats(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id)
        return GradeStatisticResponse(**response.json())

    def get_grades(self,
                   student_id: Optional[int] = None,
                   teacher_id: Optional[int] = None,
                   group_id: Optional[int] = None) -> List[GradeResponse]:
        params = {}
        if student_id is not None: params['student_id'] = student_id
        if teacher_id is not None: params['teacher_id'] = teacher_id
        if group_id is not None: params['group_id'] = group_id

        response = self.grade_helper.get_grade(**params)
        grades_data = response.json()

        return [GradeResponse(**grade_item) for grade_item in grades_data]
