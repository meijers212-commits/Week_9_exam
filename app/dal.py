from typing import List, Dict, Any
from db import get_db_connection

# q1
def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT customerName, creditLimit FROM `customers` WHERE creditLimit > 100000 or creditLimit < 10000"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q2
def get_orders_with_null_comments():
    """Return orders that have null comments."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT orderNumber , comments FROM `orders` where comments IS NULL ORDER BY orderDate "
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q3
def get_first_5_customers():
    """Return the first 5 customers."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT customerName, contactLastName, contactFirstName FROM `customers` ORDER BY contactLastName LIMIT 5;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q4
def get_payments_total_and_average():
    """Return total and average payment amounts."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT SUM(amount) as total_amount , AVG(amount) as avg_amount , max(amount) as max_amount , min(amount) as min_amount FROM `payments`;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q5
def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT employees.firstName, employees.lastName, offices.phone FROM `employees` LEFT JOIN offices on offices.officeCode = employees.officeCode"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q6
def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query ="""SELECT customers.customerName , orders.shippedDate FROM customers
            LEFT JOIN orders ON (customers.customerNumber = orders.customerNumber);"""
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q7
def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """SELECT customers.customerName,orderdetails.quantityOrdered FROM `customers` 
            INNER JOIN orders ON(customers.customerNumber =orders.customerNumber)
            INNER JOIN orderdetails ON (orders.orderNumber = orderdetails.orderNumber)
            ORDER BY customers.customerName;"""
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# q8
def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """SELECT customers.customerName as customer_name ,employees.firstName as contact_name , SUM(payments.amount) as sum_amount FROM `customers`
            INNER JOIN employees ON (customers.salesRepEmployeeNumber = employees.employeeNumber)
            INNER JOIN payments ON (customers.customerNumber = payments.customerNumber)
            WHERE customers.contactFirstName LIKE '%mu%' or customers.contactFirstName LIKE '%ly%'
            GROUP BY customers.customerName , employees.firstName;"""
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
