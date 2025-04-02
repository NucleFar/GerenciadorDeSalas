from src.static.models.bloco import BlocoCreate, BlocoResponse

class BlocoCrud:
    def __init__(self, db):
        self.collection = db["blocos"]  # Coleção de blocos no MongoDB

    async def criar_bloco(self, bloco: BlocoCreate) -> BlocoResponse:
        bloco_dict = bloco.model_dump()  # Converte o modelo Pydantic para dict
        result = await self.collection.insert_one(bloco_dict)

        if result.inserted_id:
            return BlocoResponse(id=str(bloco.nome), **bloco_dict)
        raise Exception("Erro ao criar o bloco no banco de dados.")
    