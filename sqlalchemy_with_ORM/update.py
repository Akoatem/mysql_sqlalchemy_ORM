from main import Session, User, engine

local_session = Session(bind=engine)


user_to_update = local_session.query(User).filter(User.username == "Akoatem").first()

user_to_update.username = "Samson"
user_to_update.email = "samson@gmail.com"

local_session.commit()