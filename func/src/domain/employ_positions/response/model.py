# STANDARD IMPORTS
from typing import List
from pydantic import BaseModel

# PROJECT IMPORTS
from src.domain.employ_positions.model import EmployPositionsModel, EmployPositionsResponse


class EmployPositionsRecordResponse(BaseModel):
    types: List[EmployPositionsModel]


class EmployPositionsToResponse:

    @staticmethod
    def employ_positions_response(
            employ_positions: List[EmployPositionsResponse]
    ):

        employ_positions_response = [
            EmployPositionsModel(**employ_position.__repr__())
            for employ_position in employ_positions
        ]

        employ_positions_dict = {
            "employ_positions": employ_positions_response
        }

        return employ_positions_dict
