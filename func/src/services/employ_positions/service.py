# PROJECT IMPORTS
from func.src.domain.employ_positions.response.model import EmployPositionsRecordResponse, EmployPositionsToResponse
from func.src.repositories.job_positions.repository import EmployPositionsRepository


class EmployPositionsService:

    @classmethod
    def get_response(cls) -> EmployPositionsRecordResponse:

        employ_positions = EmployPositionsRepository.get_employ_positions()

        response = EmployPositionsToResponse.employ_types_response(
            employ_positions
        )

        return response
