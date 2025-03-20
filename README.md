# Banking System

A role-based banking application with secure authentication and authorization. The system includes login and registration for both **Admin** and **User** roles. Admins can perform **CRUD operations** on banking accounts and manage multiple tables.

---

## Features

### 🔐 Authentication & Authorization
- Role-based access control (**Admin & User**)
- Secure login and registration system

### 🏦 Admin Functionalities
- Manage user accounts (Create, Read, Update, Delete)
- Manage bank accounts and related details

### 👤 User Functionalities
- View personal account details
- Update personal information

---

## Database Schema

### **1. Account (Master Table)**
| Column          | Type     | Description             |
|----------------|---------|-------------------------|
| `id`           | Integer | Primary Key             |
| `branch_name`  | String  | Name of the bank branch |
| `account_number` | String | Unique account number  |
| `ifsc_code`    | String  | IFSC code of the branch |
| `bank_address` | String  | Branch address         |
| `account_type` | String  | Type of account        |

### **2. UserAccount (Extends Account)**
| Column         | Type     | Description                  |
|---------------|---------|------------------------------|
| `id`         | Integer | Primary Key (FK from Account) |
| `name`       | String  | User's full name              |
| `email`      | String  | User's email address          |
| `mobile_number` | String | User's contact number      |
| `address`    | String  | User's residential address    |

---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework (DRF)
- **Frontend:** React.js
- **Database:** PostgreSQL / MySQL
- **Authentication:** JWT / OAuth
- **Deployment:** Docker, AWS (Optional)

---

## Installation & Setup

### Clone the Repository and Set Up the Environment
```bash
git clone https://github.com/your-username/banking-system.git
cd banking-system

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```
