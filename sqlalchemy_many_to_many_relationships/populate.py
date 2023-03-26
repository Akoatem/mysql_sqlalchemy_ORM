from main import session, Product, Customer

# customer1 = Customer(name='Ben')
# customer2 = Customer(name='Coline')
# customer3 = Customer(name='Sam')

# associate these items to a particular customer

customer = session.query(Customer).filter(Customer.id == 1).first()
customer2 = session.query(Customer).filter(Customer.id == 1).first()
customer3 = session.query(Customer).filter(Customer.id == 1).first()

# for a particular customer to have all the products
product = Product(name='Eggs', price=300)
product2 = Product(name='Fish Oil', price=100)
product3 = Product(name='white rice', price=600)

customer2.products.append(product)
customer2.products.append(product2)
customer2.products.append(product3)

# session.add_all(
#     [customer, customer2, customer3]
# )
session.commit()
print(customer.products)
