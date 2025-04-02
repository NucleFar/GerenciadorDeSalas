from typing import Dict
from fastapi import HTTPException
from .http_unprocessable_entity import HttpUnprocessableEntity
from .http_bad_request import HttpBadRequest
from .http_not_found import HttpNotFound

def handle_errors(error: HTTPException) -> Dict:
    # Verifica se o erro é uma instância das classes customizadas de erro
    if isinstance(error, (HttpUnprocessableEntity, HttpBadRequest, HttpNotFound)):
        return {
            'status_code': error.status_code,
            'body': {
                'errors': [{
                    'title': error.__class__.__name__,  # Usando o nome da classe para o título
                    'detail': error.detail  # Corrigido para 'detail' ao invés de 'message'
                }]
            }
        }

    # Para outros erros genéricos, como um erro interno do servidor
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                'title': "Server Error!",
                'detail': str(error)  # Inclui a mensagem de erro como texto
            }]
        }
    }
