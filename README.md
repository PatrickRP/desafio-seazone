# 🏡 Seazone Backend Challenge

API desenvolvida em **FastAPI** para gerenciar **propriedades** e **reservas**, incluindo verificação de disponibilidade.  
O projeto foi criado com base no documento de **Requisitos Funcionais** fornecido no desafio.

---

## 📋 Requisitos Funcionais Implementados

- **Propriedades**
  - Cadastro de propriedade (`POST /properties`)
  - Listagem de propriedades (`GET /properties`)
  - Consulta de disponibilidade (`GET /properties/availability`)

- **Reservas**
  - Cadastro de reserva (`POST /reservations`)
  - Listagem de reservas (`GET /reservations`)

- **Regra de disponibilidade**
  - A API calcula a disponibilidade de uma propriedade entre duas datas,
    considerando reservas já existentes.

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.11](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/) (migrations)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker + Docker Compose](https://docs.docker.com/)

---

## 📦 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seazone-backend.git
cd seazone-backend
```

### 2. Configure o ambiente
Crie o arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/seazone
```

### 3. Suba os containers
```bash
docker-compose up --build -d
```

### 4. Aplique as migrations
Acesse o container da API:

```bash
docker exec -it seazone_api bash
```

Rode as migrations:
```bash
alembic upgrade head
```

### 5. Acesse a API
- URL base: [http://localhost:8000](http://localhost:8000)
- Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧩 Estrutura de Pastas

```bash
app/
├── main.py                 # Ponto de entrada da aplicação
├── models/                 # Models SQLAlchemy
│   ├── property.py
│   └── reservation.py
├── schemas/                # Schemas Pydantic
│   ├── property.py
│   └── reservation.py
├── routes/                 # Endpoints da API
│   ├── properties.py
│   └── reservations.py
├── database.py             # Configuração do banco
alembic/
├── versions/               # Arquivos de migration
docker-compose.yml
Dockerfile
.env
```

---

## 🧪 Exemplos de Requisição

### Criar uma propriedade
```bash
curl -X POST http://localhost:8000/properties/ -H "Content-Type: application/json" -d '{
  "title": "Casa de campo",
  "address_street": "Av Afonso Pena",
  "address_number": "2024",
  "address_neighborhood": "Jurere",
  "address_city": "Floripa",
  "address_state": "SC",
  "country": "Brazil",
  "rooms": 3,
  "capacity": 6,
  "price_per_night": 120.0
}'
```

### Listar propriedades
```bash
curl http://localhost:8000/properties/
```

### Verificar disponibilidade
```bash
curl "http://localhost:8000/properties/availability?property_id=1&start_date=2025-08-20&end_date=2025-08-25"
```

### Criar uma reserva
```bash
curl -X POST http://localhost:8000/reservations/ -H "Content-Type: application/json" -d '{
  "property_id": 1,
  "customer_name": "João Silva",
  "start_date": "2025-08-20",
  "end_date": "2025-08-23",
  "guests": 4
}'
```

### Listar reservas
```bash
curl http://localhost:8000/reservations/
```

---

## 👨‍💻 Autor

##### Patrick Rodrigues Paredes
Desafio Backend Jr - Seazone  
Desenvolvido com 💙 usando **FastAPI**
