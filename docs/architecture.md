# Arquitetura — BarberFlow SaaS

O BarberFlow é um SaaS multi-tenant construído com Django + Django REST Framework, PostgreSQL e Redis.

---

# 🔧 1. Componentes Principais

## Backend
- Django 5
- Django REST Framework
- Multitenancy manual via middleware
- Gunicorn
- Docker + docker-compose

## Banco de Dados
- PostgreSQL 15
- Uso de schemas separados por tenant (opcional) ou FK direta (implementação atual)

## Cache / Filas
- Redis 7

---

# 🏗️ 2. Estrutura de Pastas

saas-barberflow/
│── config/ # Configurações globais
│── core/ # Utilidades e permissões
│── tenants/ # Modelo Establishment e lógica multi-tenant
│── apps/ # Apps da camada de negócio
│── public_api/ # Endpoints públicos
│── static/
│── templates/
│── tests/
│── docs/

yaml
Copiar código

---

# 🔄 3. Fluxo de uma Request

```mermaid
flowchart LR
A[Request] --> B[Middleware Multi-Tenant]
B --> C[Identifica tenant pelo header X-Tenant]
C --> D[Roteamento DRF]
D --> E[View / Service]
E --> F[Model Tenant-Aware]
F --> G[Resposta JSON]
🏛️ 4. Serviço Multi-Tenant
Cada request passa pelo middleware:

Lê o header X-Tenant

Busca o tenant no banco

Salva o tenant em request.tenant

Todos os services usam tenant para filtrar dados

🗂️ 5. Apps do Sistema
App	Responsabilidade
clients	Clientes
employees	Funcionários
services	Serviços oferecidos
scheduling	Agendamentos
tenants	Estabelecimentos (controle do SaaS)

💾 6. Modelos Principais
Veja o diagrama em models_diagram.png.

🚀 7. Escalabilidade
Pode evoluir para schemas PostgreSQL por tenant

Pode usar fila Celery para confirmações de agendamento

Pode subir N instances Gunicorn com Nginx reverso