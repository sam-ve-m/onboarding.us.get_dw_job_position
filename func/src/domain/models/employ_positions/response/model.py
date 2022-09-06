# STANDARD IMPORTS
from typing import List

# PROJECT IMPORTS
from src.domain.models.employ_positions.model import EmployPositionsModel, EmployPositionsResponse


class EmployPositionsToResponse:

    @staticmethod
    def employ_positions_response(
            employ_positions: List[EmployPositionsResponse]
    ):

        employ_positions_response = [
            EmployPositionsModel(**employ_position.__repr__()).dict()
            for employ_position in employ_positions
        ]

        return employ_positions_response
