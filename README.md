# OnlineMarketPlaceAPI

**Software Requirements Specification (SRS)**

**1. Introduction**

The Online Marketplace API is a backend service that powers an online marketplace platform allowing users to buy and sell products. The application is built using Python, utilizing FastAPI for building the API endpoints, Pandas for data manipulation, and SQLAlchemy for interacting with the database.


**2. Functional Requirements**

**i). User Authentication:**
**.** Users can register for an account by providing necessary details (username, email, password).
**.** Registered users can log in securely using their credentials.
**.** Authentication tokens (JWT) are issued upon successful login for subsequent API access.


**ii). Product Management:**

**.**  Sellers can add new products to sell by providing product details (name, description, price, category, quantity).
**.**  Sellers can update existing product information or remove products from the platform.

**iii). Search and Browse:**
**.** Users can search for products based on various criteria such as name, category, price range, etc.
**.** Products can be browsed through paginated API endpoints.

**iv).Shopping Cart:**
**.** Users can add products to their shopping cart, update quantities, and remove items.
**.** The shopping cart persists across sessions for authenticated users.

**v). Order Management:**
**.** Users can place orders for products in their shopping cart.
**.** Sellers can view and manage orders for their products, including order status updates and order fulfillment.

**vi). User Reviews:**
**.** Users can leave reviews and ratings for products they have purchased.
**.** Reviews are displayed along with product information.

**3. Non-Functional Requirements**

**i) Performance:**
**.** The system should handle a large number of concurrent users and requests efficiently.
**.** Response times should be optimized to provide a seamless user experience.

**ii) Security:**
**.** User authentication and authorization should be implemented securely to prevent unauthorized access.
**.** Input validation and sanitation should be enforced to prevent injection attacks and other security vulnerabilities.

**iii) Scalability:**
**.** The system should be designed to scale horizontally to accommodate increased traffic and data volume.
**.** Load balancing and caching mechanisms should be implemented for performance and scalability.



**Software Design Document (SDD)**



**1. System Architecture**

**The system follows a three-tier architecture:**

**i) Presentation Layer:** Implemented using FastAPI to provide RESTful API endpoints.
**ii) Application Layer:** Contains business logic for user authentication, product management, shopping cart, order management, and user reviews.
**iii) Data Access Layer:** Utilizes: SQLAlchemy for interacting with the relational database (e.g., PostgreSQL, MySQL).


**2. Database Schema**
**.** The database schema includes tables for users, products, orders, and reviews.
**. Relationships:**
**.** Users can have multiple orders and reviews.
**.** Products can be associated with multiple orders and reviews.

**3. API Design**

**.** The API endpoints are designed to follow RESTful principles using FastAPI:

**i)** **'/register':** POST method for user registration.

**ii)**  **'/login':** POST method for user login.

**iii)** **'/products':** GET method to retrieve all products or search products.

**.iv)** **'/products/{product_id}':** GET method to retrieve details of a specific product.

**v)** **'/cart':** GET method to retrieve the user's shopping cart or POST method to update the cart.

**vi)** **'/orders':** POST method to place an order.

**vii)** **'/orders/{order_id}':** GET method to retrieve order details.

**viii)** **'/reviews:'** POST method to leave a review for a product.

**ix)** **'/reviews/{product_id}':** GET method to retrieve reviews for a specific product.

**4. Implementation Details**

**i) Python Libraries:** FastAPI for building the API, Pandas for data manipulation (if necessary), SQLAlchemy for database interaction.

**ii) Authentication:** User passwords are hashed and stored securely. JWT tokens are used for session management.

**iii) Concurrency:**  FastAPI supports asynchronous programming, allowing for concurrent requests handling.

**iv) Deployment:** The application can be deployed on a web server using ASGI (Asynchronous Server Gateway Interface).
   






