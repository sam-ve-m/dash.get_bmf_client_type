from src.core.interfaces.service.bmf_client_enum.interface import (
    IBmfClientEnumService,
)
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.bmf_client_enum.repository import BmfClientEnumRepository


class BmfClientEnumService(IBmfClientEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = BmfClientEnumRepository.get_bmf_client_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response