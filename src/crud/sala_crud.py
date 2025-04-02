from src.static.models.sala import SalaCreate

class SalaCrud:
    def __init__(self, db):
        self.sala_collection = db["salas"]
        self.bloco_collection = db["blocos"]

    async def criar_sala_com_associacao(self, bloco_nome: str, sala: SalaCreate):
        # 1. Cria a sala
        sala_dict = sala.model_dump()
        sala_dict["bloco_nome"] = bloco_nome

        # 2. Insere a sala na coleção de salas
        result_sala = await self.sala_collection.insert_one(sala_dict)
        if result_sala.inserted_id:
            sala_id = str(result_sala.inserted_id)
            
            # 3. Atualiza a lista de salas do bloco
            await self.bloco_collection.update_one(
                {"nome": bloco_nome},
                {"$push": {"salas": sala_id}}
            )
            return {"message": "Sala criada e associada ao Bloco com sucesso!", "sala_id": sala_id}
        
        raise Exception("Erro ao criar a sala no banco de dados.")