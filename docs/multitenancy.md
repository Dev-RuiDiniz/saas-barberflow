# Multitenancy — BarberFlow SaaS

O BarberFlow utiliza multitenancy baseado em **single database + tenant_id**.

---

# 🎯 Objetivo
Isolar dados por estabelecimento (barbearia/salão), permitindo:

- múltiplos estabelecimentos no mesmo servidor
- rota única de API
- isolamento de dados automático

---

# 🧠 Como funciona?

## 1. Identificação do Tenant
Toda request deve incluir:

X-Tenant: nome-do-estabelecimento

yaml
Copiar código

## 2. Middleware
Arquivo: `core/multitenancy_middleware.py`

Ele:
- Lê o header
- Consulta `tenants.Establishment`
- Atribui `request.tenant`
- Bloqueia acesso se o tenant não existir

---

# 🗃️ 3. Relacionamentos
Todos os modelos de negócio incluem:

```python
tenant = models.ForeignKey("tenants.Establishment", on_delete=models.CASCADE)
🧱 4. Garantias
Nenhum dado é criado sem tenant

Queries são sempre filtradas

Services sempre recebem tenant

🚀 5. Possíveis upgrades
Separar cada tenant em um schema PostgreSQL

Criar middleware de subdomínio (loja.barberflow.com)

Criar rotinas de migração automática por tenant

📌 6. Segurança
Um tenant nunca pode acessar outro tenant

Identificação acontece antes da view

Atualizações e deletes sempre verificam tenant_id

yaml
Copiar código

---

# 🛠️ **4. requests_examples.http**

Para testar via VSCode:

### **docs/requests_examples.http**
```http
### Listar clientes
GET http://localhost:8000/api/clients/
X-Tenant: barber1

### Criar cliente
POST http://localhost:8000/api/clients/
X-Tenant: barber1
Content-Type: application/json

{
  "name": "Maria",
  "phone": "11912345678"
}

### Criar agendamento
POST http://localhost:8000/api/scheduling/
X-Tenant: barber1
Content-Type: application/json

{
  "client": 1,
  "employee": 2,
  "service": 3,
  "datetime": "2025-02-10T10:00:00"
}