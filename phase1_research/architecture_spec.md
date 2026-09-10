```json
{
  "system_name": "Multi-Vendor Marketplace Backend",
  "database_models": [
    {
      "name": "Vendor",
      "fields": ["id", "user_id", "store_name", "status", "created_at", "updated_at"],
      "description": "Profile and status of a merchant on the marketplace."
    },
    {
      "name": "Product",
      "fields": ["id", "vendor_id", "title", "description", "price", "currency", "sku", "is_active", "created_at"],
      "description": "Catalog item associated with a specific vendor."
    },
    {
      "name": "InventoryReservation",
      "fields": ["id", "product_id", "order_item_id", "quantity", "expires_at", "status"],
      "description": "Temporary lock on inventory to prevent overselling during checkout processes."
    },
    {
      "name": "Order",
      "fields": ["id", "customer_id", "vendor_id", "total_amount", "status", "payment_status", "created_at"],
      "description": "Header record for a transaction between a customer and a vendor."
    },
    {
      "name": "OrderItem",
      "fields": ["id", "order_id", "product_id", "quantity", "unit_price"],
      "description": "Line items within an order."
    },
    {
      "name": "PaymentWebhookEvent",
      "fields": ["id", "stripe_event_id", "type", "payload", "status", "processed_at"],
      "description": "Log of Stripe webhooks for payment tracking and idempotency."
    }
  ],
  "api_endpoints": [
    {
      "method": "POST",
      "path": "/vendors",
      "description": "Onboard a new vendor store."
    },
    {
      "method": "GET",
      "path": "/vendors/:vendor_id/products",
      "description": "Retrieve the product catalog for a specific vendor."
    },
    {
      "method": "POST",
      "path": "/orders/checkout",
      "description": "Initiate checkout; reserves inventory locks and creates Stripe payment intent."
    },
    {
      "method": "POST",
      "path": "/webhooks/stripe",
      "description": "Handle Stripe payment webhooks (payment_intent.succeeded, etc.)."
    },
    {
      "method": "GET",
      "path": "/orders/:id",
      "description": "Retrieve order details and current inventory lock status."
    }
  ],
  "security_rules": [
    "Implement JWT-based authentication with role-based access control (RBAC) for Vendor vs. Customer roles.",
    "Enforce Idempotency Keys on the /orders/checkout endpoint to prevent duplicate inventory locks.",
    "Validate and process Stripe webhooks using signature validation to ensure payload authenticity.",
    "Set strict TTL (Time-To-Live) expiration on InventoryReservation locks to auto-release inventory if checkout is abandoned.",
    "Apply strict input validation on all product and pricing fields to prevent server-side injection."
  ]
}
```