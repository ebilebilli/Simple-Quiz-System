# E-commerce Platform: Microservices Architecture Overview

This document provides a comprehensive overview of the microservices architecture for our e-commerce platform. The system is designed with independent services, each responsible for a specific business capability, communicating asynchronously via an event-driven model (e.g., RabbitMQ).

## Core Principles

* **Decentralized:** Each service is an independent unit with its own repository and deployment pipeline.
* **Asynchronous Communication:** Services primarily communicate by sending and listening to events, ensuring low coupling and high resilience.
* **Event-Driven:** Key business actions (e.g., `order.created`, `product.updated`) generate events that other services can subscribe to.

---

## Services Overview

### 1. User Service
Handles all user-related information, acting as the identity provider for the entire system.
* **Direct Relations:**
    * **Order Service:** Requires user ID to identify who placed an order.
    * **Comment Service:** Requires user ID to identify the comment's author.
    * **Shop Service:** Maintains a `OneToOne` relationship with a user who owns a shop.
* **Events Sent:** `user.created`, `shop.created`

### 2. Shop Service
Manages information for sellers and their shops.
* **Direct Relations:**
    * **Product Service:** Assigns products to specific shops.
    * **Order Service:** Determines which shop an order belongs to for fulfillment.
    * **Analytics Service:** Provides shop-specific sales and revenue data.
* **Events Sent:** `shop.created`, `shop.updated`

### 3. Product Service
Manages all product-related data, including products, categories, variations, and images uploaded by shop owners.
* **Direct Relations:**
    * **Warehouse Service:** Manages stock based on `product_variation_id`.
    * **Order Service:** Provides item price and details for order creation.
    * **Comment Service:** Allows users to leave reviews on products.
* **Events Sent:** `product.created`, `product.updated`, `product.deleted`

### 4. Warehouse (Inventory) Service
Manages stock and inventory levels.
* **Direct Relations:**
    * **Product Service:** Stores stock levels for each product variant.
    * **Order Service:** Decreases stock when an order is placed.
* **Events Sent:** `stock.decreased`, `stock.increased`
* **Events Listened to:** `order.cancelled` (to restore stock)

### 5. Order Service
Manages the entire cart and order lifecycle, from checkout to shipment.
* **Direct Relations:**
    * **User Service:** Identifies the user placing the order.
    * **Product Service:** Fetches product details and pricing.
    * **Warehouse Service:** Reduces stock during order creation.
    * **Payment Service:** Initiates and tracks payments.
* **Events Sent:** `order.created`, `order.paid`, `order.cancelled`, `order.shipped`

### 6. Payment Service
Handles all payment processing.
* **Direct Relations:**
    * **Order Service:** Associates payments with a specific order.
* **Events Sent:** `payment.success`, `payment.failed`
* **Events Listened to:** `order.created` (to initiate payment flow)

### 7. Comment Service
Manages user reviews and comments on products.
* **Direct Relations:**
    * **User Service:** Identifies the author of a comment.
    * **Product Service:** Identifies the product being reviewed.
* **Events Sent:** (Optional) `comment.created` for analytics.

### 8. Analytics Service
Provides statistics and dashboards for shop owners and platform administrators. This service is primarily event-driven.
* **Events Listened to:** `order.created`, `order.paid`, `order.cancelled`, `payment.success`, `payment.failed`, `user.created`, `shop.created`, `comment.created`, `cart.updated`, `cart.checked_out`

### 9. Shop Cart Service
Manages the user's shopping cart and the checkout process.
* **Direct Relations:**
    * **User Service:** Verifies the user adding items.
    * **Shop Service:** Validates the shop ownership of products.
    * **Product Service:** Checks product existence and price.
    * **Order Service:** Initiates order creation on checkout.
    * **Warehouse Service:** Checks stock availability during checkout.
* **Events Sent:** `cart.created`, `cart.updated`, `cart.checked_out`, `cart.deleted`
* **Events Listened to:** `stock.decreased`, `stock.increased`, `order.cancelled`, `product.deleted`, `product.updated`, `user.deleted`, `shop.deleted`

### 10. Admin Visual Content Service
Manages **site-wide visuals**, such as homepage banners, sliders, and marketing visuals, controlled **only by admins**.
* **Direct Relations:** None with shop owners or general users.
* **Events Listened to:** `visual_content.admin_uploaded`, `visual_content.admin_deleted`
* **Events Sent:** `visual_content.uploaded`, `visual_content.deleted`

### 11. Product Media Sub-Service
Handles **product images uploaded by shop owners**.
* **Direct Relations:**
    * **Product Service:** Stores and serves product images.
* **Events Listened to:** `product.created`, `product.updated`
* **Events Sent:** `product_image.uploaded`, `product_image.deleted`

---

## Service Relationships Diagram

```mermaid
graph TD
    subgraph Services
        A[User Service]
        B[Shop Service]
        C[Product Service]
        D[Warehouse Service]
        E[Order Service]
        F[Payment Service]
        G[Comment Service]
        H[Analytics Service]
        I[Shop Cart Service]
        J[Admin Visual Content Service]
        K[Product Media Service]
    end

    A -- "Requires user info" --> E
    A -- "Requires user info" --> G
    A -- "OneToOne relationship" --> B
    A -- "Verifies user" --> I

    B -- "Assigns products" --> C
    B -- "Determines order shop" --> E
    B -- "Provides data" --> H
    B -- "Verifies ownership" --> I

    C -- "Manages stock" --> D
    C -- "Provides price & ID" --> E
    C -- "Allows reviews" --> G
    C -- "Verifies product" --> I
    C -- "Stores images" --> K

    D -- "Reduces stock" --> E
    D -- "Holds stock info" --> C
    D -- "Verifies stock" --> I

    E -- "Fetches details" --> C
    E -- "Reduces stock" --> D
    E -- "Handles payments" --> F
    E -- "Requires user ID" --> A
    E -- "Creates order from cart" --> I

    F -- "Associates payment" --> E

    G -- "Identifies author" --> A
    G -- "Identifies product" --> C

    H -- "Collects data via events" --> E
    H -- "Collects data via events" --> F
    H -- "Collects data via events" --> A
    H -- "Collects data via events" --> B
    H -- "Collects data via events" --> G
    H -- "Collects data via events" --> I
    H -- "Collects data via events" --> J
    H -- "Collects data via events" --> K

    I -- "Verifies user" --> A
    I -- "Verifies shop" --> B
    I -- "Verifies product" --> C
    I -
