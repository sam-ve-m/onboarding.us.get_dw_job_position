from unittest.mock import patch

import pytest
from flask import Flask
from heimdall_client import Heimdall, HeimdallStatusResponses
from werkzeug.datastructures import Headers

from main import get_employ_positions
from src.domain.exceptions.exceptions import FailToFetchData
from src.services.employ_positions.service import EmployPositionsService
from tests.main_stub import decoded_jwt_stub, stub_employ_stub


@pytest.mark.asyncio
@patch.object(EmployPositionsService, "get_employ_positions_response", side_effect=stub_employ_stub)
@patch.object(Heimdall, "decode_payload", return_value=(decoded_jwt_stub, HeimdallStatusResponses.SUCCESS))
async def test_when_sending_right_params_to_get_employ_positions_then_return_the_expected(
        mock_get_employ_positions_response,
        mock_decode_payload
):
    app = Flask(__name__)
    with app.test_request_context(
            headers=Headers({"x-thebes-answer": "jwt_to_decode_stub"}),
    ).request as request:

        response = await get_employ_positions(
            request_body=request
        )
        assert response is not None


@pytest.mark.asyncio
@patch.object(Heimdall, "decode_payload", return_value=(None, HeimdallStatusResponses.INVALID_TOKEN))
@patch.object(EmployPositionsService, "get_employ_positions_response", return_value=stub_employ_stub)
async def test_when_sending_invalid_jwt_to_get_employ_positions_then_raise_error(
        mock_decode_payload,
        mock_get_response
):
    app = Flask(__name__)
    with app.test_request_context(
            headers=Headers({"x-thebes-answer": "jwt_to_decode_stub"}),
    ).request as request:
        with pytest.raises(Exception):
            await get_employ_positions(
                request_body=None
            )


@pytest.mark.asyncio
@patch.object(Heimdall, "decode_payload", return_value=(decoded_jwt_stub, HeimdallStatusResponses.SUCCESS))
@patch.object(EmployPositionsService, "get_employ_positions_response", return_value=None)
async def test_when_fail_to_fetch_data(
    mock_get_response,
    mock_decode_payload
):
    mock_get_response.side_effect = FailToFetchData()
    app = Flask(__name__)
    with app.test_request_context(
            headers=Headers({"x-thebes-answer": "jwt_to_decode_stub"}),
    ).request as request:
        result = await get_employ_positions(
            request_body=request
        )
    expected_result = b'{"result": null, "message": "Not able to get data from database", "success": false, "code": 100}'
    assert result.data == expected_result
