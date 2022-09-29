class InvalidParams(Exception):
    msg = "Jormungandr-Onboarding::w8_confirmation_param::Invalid params were sent"


class InternalServerError(Exception):
    pass


class ErrorOnDecodeJwt(Exception):
    msg = "Jormungandr-Onboarding::decode_jwt_and_get_unique_id::Fail when trying to get unique_id," \
          " jwt not decoded successfully"


class FailToFetchData(Exception):
    pass