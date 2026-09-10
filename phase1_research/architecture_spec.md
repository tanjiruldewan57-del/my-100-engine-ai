```yaml
system_name: GlobalInvoicePro

database_models:
  - name: Organization
    fields:
      - id: string (UUID, PK)
      - name: string
      - tax_id: string
      - currency: string
      - created_at: timestamp
    relationships:
      has_many: Client, Invoice, Payment, User

  - name: User
    fields:
      - id: string (UUID, PK)
      - organization_id: string (FK)
      - email: string
      - password_hash: string
      - role: enum (admin, accountant, viewer)
    relationships:
      belongs_to: Organization

  - name: Client
    fields:
      - id: string (UUID, PK)
      - organization_id: string (FK)
      - name: string
      - email: string
      - address: string
      - tax_id: string
      - billing_cycle: enum (monthly, quarterly, annual)
    relationships:
      belongs_to: Organization
      has_many: Invoice

  - name: Invoice
    fields:
      - id: string (UUID, PK)
      - organization_id: string (FK)
      - client_id: string (FK)
      - invoice_number: string
      - status: enum (draft, pending, paid, overdue, voided)
      - subtotal: decimal
      - tax_amount: decimal
      - total: decimal
      - due_date: date
      - created_at: timestamp
    relationships:
      belongs_to: Organization, Client
      has_many: InvoiceLineItem, Payment

  - name: InvoiceLineItem
    fields:
      - id: string (UUID, PK)
      - invoice_id: string (FK)
      - description: string
      - quantity: decimal
      - unit_price: decimal
      - tax_rate: decimal
    relationships:
      belongs_to: Invoice

  - name: Payment
    fields:
      - id: string (UUID, PK)
      - organization_id: string (FK)
      - invoice_id: string (FK)
      - amount: decimal
      - method: enum (credit_card, bank_transfer, paypal)
      - status: enum (success, failed, pending)
      - gateway_reference: string
      - paid_at: timestamp
    relationships:
      belongs_to: Organization, Invoice

api_endpoints:
  - method: POST
    path: /api/v1/auth/login
    description: Authenticate user and return JWT token
  - method: GET
    path: /api/v1/invoices
    description: List invoices with pagination and filtering by status/date
  - method: POST
    path: /api/v1/invoices
    description: Create a new draft invoice
  - method: GET
    path: /api/v1/invoices/{id}
    description: Retrieve detailed invoice information
  - method: PUT
    path: /api/v1/invoices/{id}
    description: Update draft invoice details
  - method: POST
    path: /api/v1/invoices/{id}/process-payment
    description: Initiate payment via gateway and update status
  - method: GET
    path: /api/v1/invoices/{id}/pdf
    description: Generate and stream PDF document for the invoice
  - method: GET
    path: /api/v1/clients
    description: List clients associated with the organization
  - method: POST
    path: /api/v1/clients
    description: Create a new client profile
  - method: POST
    path: /api/v1/webhooks/payment-callback
    description: Receive asynchronous payment status updates from gateway

security_rules:
  - Enforce JWT-based authentication for all endpoints except /auth/login and /webhooks/payment-callback
  - Implement Row-Level Security ensuring users can only access data belonging to their Organization
  - Sign webhook payloads with HMAC-SHA256 to prevent tampering
  - Store PII (client emails, tax IDs) encrypted at rest using AES-256
  022 - Rate limit payment processing endpoints to