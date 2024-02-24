# Ecommerce API with Django REST Framework

This project implements an Ecommerce API using Django REST Framework. It provides endpoints to manage products, orders, and order items.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:
git clone github.com/konstantine25b/Ecommerce_API
2. Install the dependencies:
pip install -r requirements.txt
3. Apply the migrations:
python manage.py migrate

## Endpoints

### Products

- **List Products**: `GET /api/products/`
- **Retrieve Product**: `GET /api/products/{id}/`
- **Create Product**: `POST /api/products/`
- **Update Product**: `PUT /api/products/{id}/`
- **Delete Product**: `DELETE /api/products/{id}/`

### Orders

- **List Orders**: `GET /api/orders/`
- **Retrieve Order**: `GET /api/orders/{id}/`
- **Create Order**: `POST /api/orders/`

### Order Items

- **List Order Items**: `GET /api/order-items/`
- **Retrieve Order Item**: `GET /api/order-items/{id}/`
- **Create Order Item**: `POST /api/order-items/`

## Authentication and Permissions

- Authentication is required for all endpoints except listing and retrieving products.
- Only authenticated users can perform actions related to orders and order items.

