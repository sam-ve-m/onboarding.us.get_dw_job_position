from typing import List

from src.domain.models.employ_position.model import EmployPositionModel
from src.repositories.cache.repository import EmployPositionCacheRepository
from src.repositories.oracle.repository import EmployPositionOracleRepository


class EmployPositionService:

    @classmethod
    def get_employ_position_response(cls) -> List[dict]:
        enum_values = EmployPositionCacheRepository.get_employ_position_enum()
        if not enum_values:
            enum_values = EmployPositionOracleRepository.get_employ_position()
            EmployPositionCacheRepository.save_employ_position_enum(enum_values)
        response = list(map(
            EmployPositionModel.from_database, enum_values
        ))
        return response
