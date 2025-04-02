from fastapi import HTTPException

class HttpInternalServerError(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=500, detail=detail)
        self.detail = detail
        self.name = 'InternalServerError'
