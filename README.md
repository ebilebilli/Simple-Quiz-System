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
