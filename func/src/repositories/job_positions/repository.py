# STANDARD IMPORTS
from http import HTTPStatus
from typing import List

# THIRD PART IMPORT
from etria_logger import Gladsheim

# PROJECT IMPORTS
from src.domain.employ_positions.model import EmployPositionsResponse
from src.domain.enums.status_code.enum import InternalCode
from src.domain.response.model import ResponseModel
from src.repositories.base_repository.oracle.base import OracleBaseRepository
from src.repositories.cache.repository import EmployPositionsCacheRepository


class EmployPositionsRepository:

    @staticmethod
    def build_employ_positions_model(employ_position: dict) -> EmployPositionsResponse:
        employ_positions_model = EmployPositionsResponse(
            code=employ_position.get("CODE"),
            description=employ_position.get("DESCRIPTION"),
        )

        return employ_positions_model

    @classmethod
    def get_employ_positions(cls) -> List[EmployPositionsResponse]:
        try:
            # todo - incluir o nome da tabela
            # sql = """
            #     SELECT CODE as code, DESCRIPTION as description
            #     FROM USPIXDB001.XXXXXXXX
            #     """

            # result = cls._get_employ_cached_enum(query=sql)

            sql_response_stub = [
                {"CODE": "ADVERTISER", "DESCRIPTION": "ANUNCIANTE"},
                {"CODE": "AGENT", "DESCRIPTION": "AGENTE"},
                {"CODE": "ANALYST", "DESCRIPTION": "ANALISTA"}
            ]

            employ_positions_model = [
                EmployPositionsRepository.build_employ_positions_model(
                    employ_position=employ_position
                )
                for employ_position in sql_response_stub
            ]

            return employ_positions_model

        except Exception as error:
            Gladsheim.error(error=error)
            response = ResponseModel(
                result=False,
                success=False,
                code=InternalCode.INTERNAL_SERVER_ERROR,
                message="Not Sent to Persephone"
            ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
            return response

    @classmethod
    def _get_employ_cached_enum(cls, query: str) -> list:
        if cached_enum := EmployPositionsCacheRepository.get_employ_positions_enum():
            return cached_enum

        enum_values = OracleBaseRepository.query(sql=query)
        EmployPositionsCacheRepository.save_employ_positions_enum(enum_values)
        return enum_values
