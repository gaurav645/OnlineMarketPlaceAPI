# OnlineMarketPlaceAPI

**Software Requirements Specification (SRS)**

**1. Introduction**

The Online Marketplace API is a backend service that powers an online marketplace platform allowing users to buy and sell products. The application is built using Python, utilizing FastAPI for building the API endpoints, Pandas for data manipulation, and SQLAlchemy for interacting with the database.


**2. Functional Requirements**

**1. User Authentication:**
**.** Users can register for an account by providing necessary details (username, email, password).
**.** Registered users can log in securely using their credentials.
**.** Authentication tokens (JWT) are issued upon successful login for subsequent API access.


**2. Product Management:**

**.** Sellers can add new products to sell by providing product details (name, description, price, category, quantity).
**.** Sellers can update existing product information or remove products from the platform.

**3.Search and Browse:**
**.** Users can search for products based on various criteria such as name, category, price range, etc.
**.** Products can be browsed through paginated API endpoints.

**4.Shopping Cart:**
**.** Users can add products to their shopping cart, update quantities, and remove items.
**.** The shopping cart persists across sessions for authenticated users.

**5. Order Management:**
**.** Users can place orders for products in their shopping cart.
**.** Sellers can view and manage orders for their products, including order status updates and order fulfillment.

**6. User Reviews:**
**.** Users can leave reviews and ratings for products they have purchased.
**.** Reviews are displayed along with product information.



