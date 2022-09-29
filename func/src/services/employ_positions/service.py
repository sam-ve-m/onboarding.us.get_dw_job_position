# PROJECT IMPORTS
from src.domain.models.employ_positions.response.model import EmployPositionsToResponse
from src.repositories.job_positions.repository import EmployPositionsRepository


class EmployPositionsService:

    @classmethod
    def get_employ_positions_response(cls) -> list:
        employ_positions = EmployPositionsRepository.get_employ_positions()

        response = EmployPositionsToResponse.employ_positions_response(
            employ_positions
        )

        return response
