from unittest.mock import Mock
from func.src.domain.employ_positions.model import EmployPositionsModel


employ_positions_service_stub = Mock()

response_service_stub = {'employ_positions': [EmployPositionsModel(
    code='ADVERTISER', description='ANUNCIANTE'), EmployPositionsModel(
    code='AGENT', description='AGENTE'), EmployPositionsModel(
    code='ANALYST', description='ANALISTA')]
}
