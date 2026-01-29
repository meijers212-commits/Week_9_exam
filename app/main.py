from fastapi import FastAPI
from db_init import init_database
from dal import *

app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    res = get_customers_by_credit_limit_range()
    return res

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    res = get_orders_with_null_comments()
    return res

@app.get("/q3/customers-first-5")
def customers_first_5():
    res = get_first_5_customers()
    return res

@app.get("/q4/payments-total-average")
def payments_total_average():
    res = get_payments_total_and_average()
    return res

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    res = get_employees_with_office_phone()
    return res

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    res  = get_customers_with_shipping_dates()
    return res

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    res = get_customer_quantity_per_order()
    return res

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern(pattern: str = "son"):
    res = get_customers_payments_by_lastname_pattern(pattern)
    return res
