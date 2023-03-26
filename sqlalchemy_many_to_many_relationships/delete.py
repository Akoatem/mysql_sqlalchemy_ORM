from main import Product, Customer, session

customer = session.query(Customer).filter(Customer.id == 1).first()
product = session.query(Product).filter(Product.id == 13).first()

customer.products.remove(product)

session.commit()