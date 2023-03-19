from main import User, Session, engine


local_session = Session(bind=engine)

# returns all object in our database
# to limit use [:4]
users = local_session.query(User).all()[:4]
# print all objects
users = local_session.query(User).all()
for user in users:
    print(user.username)

# query for one object
Akoatem = local_session.query(User).filter(User.username == "Akoatem").first()
print(Akoatem)