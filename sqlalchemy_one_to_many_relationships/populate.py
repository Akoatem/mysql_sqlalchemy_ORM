from main import Post, User, session

# One to many relationship
# new_user = User(
#     username="Peter23",
#     email="Peter23@gmail.com"
# )
#
# session.add(new_user)
# session.commit()

# create users
users=[
    {
        "username":"jerry",
        "email":"jerry@company.com"
    },
     {
        "username":"jordan",
        "email":"jordan@company.com"
    }, {
        "username":"jackson",
        "email":"jackson@company.com"
    }, {
        "username":"jarden",
        "email":"j@company.com"
    }, {
        "username":"john",
        "email":"john@company.com"
    }, {
        "username":"jack",
        "email":"jack@company.com"
    },
]


posts = [
    {
        "title": "Path to become a software developer or web developer",
        "content": "There are lists of programming languages to enable you to become a software engineer"
    },
    {
        "title": "Learn Java",
        "content": "Jave is my first language"
    },
    {
        "title": "Learn C Language",
        "content": "C programming is the most difficult and interesting language"
    },
    {
        "title": "Learn Python",
        "content": "Python is the best because everything is about object"
    },
    {
        "title": "Learn javascript",
        "content": "Javascript is also very important for front end"
    },
    {
        "title": "Learn HTML",
        "content": "HTML is also very important for front end"
    },
    {
        "title": "Learn CSS",
        "content": "CSS is also very good for decoration and styling of your html codes"
    },
]

user=session.query(User).filter(User.id==6).first()

for u in users:
    new_user = User(username=u["username"], email=u["email"])

    session.add(new_user)

    session.commit()

    print(f"Added {u['username']}")

for post in posts:
    new_post = Post(
        title=post['title'],
        content=post['content'],
        author=user
    )

session.add(new_post)
session.commit()
print(f"Post CREATED {post['title']}")

# To access a post

post=session.query(Post).filter(Post.id==1).first()
print(post.author)
print(user.posts)