# STANDARD IMPORTS
from http import HTTPStatus
from typing import List

# THIRD PART IMPORT
from etria_logger import Gladsheim

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import FailToFetchData
from src.domain.models.employ_positions.model import EmployPositionsResponse
from src.domain.enums.status_code.enum import InternalCode
from src.domain.models.response.model import ResponseModel
from src.repositories.base_repository.oracle.base import OracleBaseRepository
from src.repositories.cache.repository import EmployPositionsCacheRepository


class EmployPositionsRepository:

    @staticmethod
    def build_employ_positions_model(employ_position: tuple) -> EmployPositionsResponse:
        employ_positions_model = EmployPositionsResponse(
            code=employ_position[0],
            description=employ_position[1],
        )

        return employ_positions_model

    @classmethod
    def get_employ_positions(cls) -> List[EmployPositionsResponse]:
        try:
            sql = """
                SELECT CODE, DESCRIPTION
                FROM USPIXDB001.SINCAD_EXTERNAL_EMPLOY_POSITIONS
                """

            employ_positions_tuple = cls._get_employ_cached_enum(query=sql)

            employ_positions_model = [
                EmployPositionsRepository.build_employ_positions_model(
                    employ_position=employ_position
                )
                for employ_position in employ_positions_tuple
            ]
            return employ_positions_model

        except Exception as error:
            Gladsheim.error(message=f"{cls.__class__}::get_employ_positions", error=error)
            raise FailToFetchData()

    @classmethod
    def _get_employ_cached_enum(cls, query: str) -> list:
        if cached_enum := EmployPositionsCacheRepository.get_employ_positions_enum():
            return cached_enum

        enum_values = OracleBaseRepository.query(sql=query)
        EmployPositionsCacheRepository.save_employ_positions_enum(enum_values)
        return enum_values
