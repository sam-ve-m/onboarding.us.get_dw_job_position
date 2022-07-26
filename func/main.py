# STANDARD IMPORTS
from http import HTTPStatus
from flask import request, Response, Request, Flask, jsonify

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from src.domain.enums.status_code.enum import InternalCode
from src.domain.exceptions.exceptions import ErrorOnDecodeJwt
from src.domain.models.jwt.response import Jwt
from src.domain.response.model import ResponseModel
from src.services.employ_positions.service import EmployPositionsService

app = Flask(__name__)


@app.route('/get_employ_positions')
async def get_employ_positions(request_body: Request = request) -> Response:

    thebes_answer = request_body.headers.get("x-thebes-answer")

    try:
        jwt_data = Jwt(jwt=thebes_answer)
        await jwt_data()
        service_response = EmployPositionsService.get_employ_positions_response()

        response = ResponseModel(
            success=True,
            code=InternalCode.SUCCESS,
            message="SUCCESS",
            result=jsonify(service_response.to_dict())
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except ErrorOnDecodeJwt as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.JWT_INVALID,
            message="Error On Decoding JWT"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except TypeError as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.DATA_NOT_FOUND,
            message="Data not found or inconsistent"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except Exception as error:
        Gladsheim.error(error=error)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.DATA_NOT_FOUND,
            message="Something went wrong"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response


if __name__ == "__main__":
    app.run(debug=True)
