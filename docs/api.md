# BarberFlow API Documentation

Documentação oficial da API REST do SaaS BarberFlow — sistema para salões e barbearias com arquitetura multi-tenant.

A API é construída com Django REST Framework. Cada requisição deve informar o tenant via header:

- `X-Tenant: <nome_do_estabelecimento>` (obrigatório)

**Autenticação**

No momento a autenticação pode ser por Token ou JWT (conforme configuração). Headers comuns para requisições autenticadas:

- `X-Tenant: <nome_do_estabelecimento>`
- `Authorization: Bearer <token>` (opcional dependendo do endpoint)

---

## Endpoints principais

Obs: todos os endpoints abaixo são relativos ao host (ex.: `https://api.example.com`).

### Clientes

- GET `/api/clients/` — lista clientes do tenant atual.
- POST `/api/clients/` — cria um cliente.

Exemplo (GET) — resposta:

```json
[
  {
    "id": 1,
    "name": "João Silva",
    "phone": "11999999999",
    "created_at": "2025-01-02T14:22:10Z"
  }
]
```

Exemplo (POST) — corpo:

```json
{
  "name": "Maria Santos",
  "phone": "11912345678"
}
```

---

### Funcionários

- GET `/api/employees/` — lista funcionários do tenant.
- POST `/api/employees/` — cria um funcionário.

Exemplo (POST) — corpo:

```json
{
  "name": "Carlos",
  "role": "barber",
  "phone": "11988884444"
}
```

---

### Serviços

- GET `/api/services/` — lista serviços disponíveis.
- POST `/api/services/` — cria um serviço.

Exemplo (POST) — corpo:

```json
{
  "name": "Corte Masculino",
  "duration_minutes": 30,
  "price": 40.0
}
```

---

### Agendamentos (Scheduling)

- GET `/api/scheduling/` — lista agendamentos do tenant.
- POST `/api/scheduling/` — cria um agendamento.

Exemplo (GET) — resposta:

```json
[
  {
    "id": 1,
    "client": 1,
    "employee": 2,
    "service": 3,
    "datetime": "2025-02-10T15:00:00",
    "status": "pending"
  }
]
```

Exemplo (POST) — corpo:

```json
{
  "client": 1,
  "employee": 2,
  "service": 3,
  "datetime": "2025-02-10T10:00:00"
}
```

---

### Tenant (Informações do estabelecimento)

- GET `/api/tenant/` — retorna informações do tenant atual.

Exemplo — resposta:

```json
{
  "id": 1,
  "name": "Barbearia do João",
  "slug": "barbearia-joao",
  "created_at": "2025-01-01T12:00:00Z"
}
```

---

## Códigos de status

| Código | Significado |
| ------: | :---------- |
| 200 | OK |
| 201 | Criado |
| 400 | Erro de validação |
| 401 | Não autenticado |
| 403 | Tenant não permitido |
| 404 | Não encontrado |

---

## Exemplos rápidos (REST Client / VSCode)

Copie estes exemplos para a extensão REST Client ou use ferramentas como `curl`/Postman.

```http
GET http://localhost:8000/api/clients/
X-Tenant: barber1

###

POST http://localhost:8000/api/scheduling/
X-Tenant: barber1
Content-Type: application/json

{
  "client": 1,
  "employee": 2,
  "service": 3,
  "datetime": "2025-02-10T10:00:00"
}
```
