# STANDARD IMPORTS
from unittest.mock import patch

# PROJECT IMPORTS
from func.src.domain.employ_positions.response.model import EmployPositionsToResponse
from func.src.repositories.job_positions.repository import EmployPositionsRepository
from func.src.services.employ_positions.service import EmployPositionsService
from tests.src.employ_positions.stub_service import employ_positions_service_stub, response_service_stub


@patch.object(EmployPositionsRepository, "get_employ_positions", return_value=employ_positions_service_stub)
@patch.object(EmployPositionsToResponse, "employ_positions_response", return_value=response_service_stub)
def test_when_sending_right_params_to_get_response_service_then_return_the_expected(
        mock_get_employ_positions,
        mock_employ_positions_response
):
    response = EmployPositionsService.get_employ_positions_response()
    assert response == response_service_stub
