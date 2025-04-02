O código foi desenvolvido na versão 3.12.8 de python (Use nesta versão para evitar incompatibilidade!) <br>
O código está utilizando FastAPI e MongoDB como solicitado.

---

Requisitos que infelizmente não foram atendidos (Para não perder seu tempo):

---

Regra de Compartilhamento de Espaços <br>
o    Se uma sala de um curso estiver livre, outros cursos podem reservá-la. <br>
o    Restrições podem ser aplicadas (exemplo: laboratórios exclusivos para determinados cursos). <br>
o    Reservas recorrentes devem ser permitidas (exemplo: toda segunda-feira das 8h às 10h por um semestre). <br>
o    Endpoint para gerar relatório com estatísticas de uso das salas (mais reservadas, horários de pico, taxa de ocupação). <br>
•    Autenticação e segurança (bônus): Implementação de autenticação JWT para coordenadores. <br>
•    Testes automatizados (bônus): Testes unitários para garantir funcionamento da API. <br>

---

Como iniciar o app:

Bom, existem duas maneiras de rodar este app: <br>
Opção 1: Esta opção você não necessita de alterar nada, basta subir o docker-compose no terminal antes, e após isso, rodar o start.py que rodará a env.

Opção 2: Esta opção tira a necessidade de ter que passar pela etapa de rodar o app.py. O arquivo docker-compose.yml está com uma linha comentada(Justamente para ela não ser executada), caso você queira que o app já inicie junto com o docker você necessitaria apenas de remover o comentário da porta no docker-compose.yml.

Exemplo:

---

Ele está assim: <br>
#ports: <br>
    #  - "8000:8000"  # Porta para acessar a FastAPI <br>

---

Basta deixar assim: <br>
ports: <br>
      - "8000:8000"  # Porta para acessar a FastAPI <br>

---

Após fazer isso é só subir o docker-compose no terminal e o aplicativo estará rodando sem a necessidade do start.py. Deixei as duas opções porquê eu gosto de usar a primeira, não sei, são etapas para mim, mas acho que a segunda é algo mais "viável", ambas as duas não tem muita diferença.

---

Vou deixar registrado aqui como eu fiz no PostMan as rotas:

Primeiro defina o baseURL do postman como: http://localhost:8000

Após isso teremos as rotas: <br>

Rota para criar um bloco: <br>
Método: Post <br>
Url: {{baseURL}}/blocos/ <br>

---

Body: <br>
{ <br>
    "nome": "H", <br>
    "identificador": "H1", <br>
    "cursos": ["EngenhariaDeSoftware", "Medicina"], <br>
    "salas": ["H100", "H101"] <br>
} <br>

---

Rota para criar uma sala (Dentro de um bloco): <br>
Método: Post <br>
Url: {{baseURL}}/blocos/{bloco}/salas/ <br>
(Deve colocar um bloco no lugar de {bloco}, por exemplo): {{baseURL}}/blocos/H/salas/ <br>

---

Body: <br>
{ <br>
    "bloco_id": "H", <br>
    "nome_e_número": "H102", <br>
    "capacidade": "80", <br>
    "recursos": ["ar-condicionado", "datashow"] <br>
} <br>

---

Rota para criar uma reserva: <br>
Método: Post <br>
Url: {{baseURL}}/reservar/ <br>

---

Body: <br>
{ <br>
    "bloco": "F", <br>
    "numero_sala": 301, <br>
    "data_inicio": "2025-04-06T18:00", <br>
    "data_fim": "2025-04-06T21:00", <br>
    "nome_coordenador": "Natasha", <br>
    "motivo": "Preciso para dar uma aula!", <br>
    "frequencia": "1", <br>
    "dia_da_semana": "segunda", <br>
    "numero_de_ocorrencias": "1" <br>
} <br>

---

Rota para verificar disponibilidade: <br>
Método: Post <br>
Url: {{baseURL}}/disponibilidade/ <br>

---

Body: <br>
{ <br>
    "bloco": "F", <br>
    "numero_sala": 301, <br> 
    "data_inicio": "2025-04-06T18:00", <br>
    "data_fim": "2025-04-06T21:00" <br>
} <br>

---

Rota para cancelar uma reserva própria (nota-se que você precisa do id da reserva que é dado na resposta da requisição ao criar uma reserva): <br>
Método: Delete <br>
Url: {{baseURL}}/cancelar/{id_da_reserva} <br>
Exemplo: {{baseURL}}/cancelar/67e3880968b7e0d59fdd88af <br>
Body: None <br>

---

Rota para simular o envio de notificações: <br>
Método: Get <br>
Url: {{baseURL}}/notificacoes/ <br>
Body: None <br>

---

Apenas isso e o programa já funcionará, bom, agora que você chegou até aqui, você pode ler apenas se quiser.
Eu gostaria de agradecer pela oportunidade, como um estudante da RocketSeat e aluno que acabou de ingressar no 1° período, eu gostei demais da experiência de tentar desenvolver um projeto real, realmente, foi um grande desafio para mim, apesar de não ter realmente conseguido ter desenvolvido completamente, eu sinto que eu me sai muito bem. Ainda não havia usado a FastAPI nem o MongoDB e foi muito boa a experiência de tentar aprender tudo em tão pouco tempo e desenvolver. Ainda que eu não passe eu imagino que isso já é mais um passo pro meu desenvolvimento, pra sentir a pressão de como "seria" o trabalho real e gostaria de dizer que foi divertido. Queria ressaltar que eu só tô vendo a aula de MVC agora que meu tempo já esgotou, então, espero que não tenha afetado tanto a organização do meu projeto. Espero ter outras oportunidades de aprender, estudar e praticar mais, como a desta vez.