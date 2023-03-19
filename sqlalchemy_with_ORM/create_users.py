from main import User, Session, engine, User

# create a dictionary list of users

users = [
    {
        "username": "Besson",
        "email": "besson@gmail.com"
    }, {
        "username": "Tesson",
        "email": "tesson23@gmail.com"
    }, {
        "username": "Ben56",
        "email": "ben53@gmail.com"
    }, {
        "username": "John23",
        "email": "john35@gmail.com"
    }, {
        "username": "suh364",
        "email": "suh884@gmail.com"
    },
]
# to create local session to connect database
# Call the engine class using bind
local_session = Session(bind=engine)
# Create user to be added into the database
# new_user = User(username="Akoatem", email="dsjhdjs@gmail.com")

# to add new user to the database
# local_session.add(new_user)

# local_session.commit()

for u in users:
    new_user = User(username=u["username"], email=u["email"])

    local_session.add(new_user)
    local_session.commit()
