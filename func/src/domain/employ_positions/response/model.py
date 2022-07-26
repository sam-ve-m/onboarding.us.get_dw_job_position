# STANDARD IMPORTS
from typing import List
from pydantic import BaseModel

# PROJECT IMPORTS
from src.domain.employ_positions.model import EmployPositionsModel, EmployPositionsResponse


class EmployPositionsRecordResponse(BaseModel):
    employ_positions: List[EmployPositionsModel]

    def to_dict(self):
        return self.employ_positions.__dict__


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

        response = EmployPositionsRecordResponse(**employ_positions_dict)

        return response
