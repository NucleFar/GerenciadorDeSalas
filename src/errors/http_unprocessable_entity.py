from fastapi import HTTPException

class HttpUnprocessableEntity(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=422, detail=detail)