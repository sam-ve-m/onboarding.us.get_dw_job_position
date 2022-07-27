# # STANDARD IMPORTS
# from unittest.mock import patch, Mock
#
# # PROJECT IMPORTS
# from func.src.domain.employ_positions.response.model import EmployPositionsToResponse
# from func.src.repositories.job_positions.repository import EmployPositionsRepository
# from func.src.services.employ_positions.service import EmployPositionsService
# from tests.src.employ_positions.stub_service import employ_positions_service_stub, response_service_stub, \
#     response_stub_employ
#
#
# class Iterable:
#     def __iter__(self):
#         return self
#
#
# @patch.object(EmployPositionsRepository, "get_employ_cached_enum", return_value=Mock())
# @patch.object(EmployPositionsRepository, "get_employ_positions", side_effect=[response_stub_employ, {}])
# def test_when_sending_right_params_to_get_response_service_then_return_the_expected(
#         mock_get_employ_cached_enum, mock_get_employ_positions
# ):
#     Iterable.__next__ = mock_get_employ_cached_enum
#     Iterable.__next__ = mock_get_employ_positions
#     response = EmployPositionsService.get_employ_positions_response()
#     assert response == response_service_stub
