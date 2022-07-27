from unittest.mock import Mock
from func.src.domain.employ_positions.model import EmployPositionsModel


employ_positions_service_stub = Mock()

response_service_stub = [EmployPositionsModel(code='ADVERTISER', description='ANUNCIANTE'),
                         EmployPositionsModel(code='AGENT', description='AGENTE'),
                         EmployPositionsModel(code='ANALYST', description='ANALISTA')]


response_stub_employ = {
'employ_positions': [{'code': 'ACCOUNTANT', 'description': 'ACCOUNTANT'}, {'code': 'ACTUARY','description': 'ACTUARY'},
{'code': 'ADJUSTER', 'description': 'ADJUSTER'}]}
