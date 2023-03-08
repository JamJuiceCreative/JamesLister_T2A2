# create the tables client command
@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

# @app.cli.command("seed")
# def seed_db():
#     from datetime import date
#     # create the card object
#     card1 = Card(
#         # set the attributes, not the id, SQLAlchemy will manage that for us
#         title = "Start the project",
#         description = "Stage 1, creating the database",
#         status = "To Do",
#         priority = "High",
#         date = date.today()
#     )
#     # Add the object as a new row to the table
#     db.session.add(card1)

#     card2 = Card(
#         # set the attributes, not the id, SQLAlchemy will manage that for us
#         title = "SQLAlchemy and Marshmallow",
#         description = "Stage 2, integrate both modules in the project",
#         status = "Ongoing",
#         priority = "High",
#         date = date.today()
#     )
#     # Add the object as a new row to the table
#     db.session.add(card2)

#     admin_user = User(
#         email = "admin",
#         password = bcrypt.generate_password_hash("password123").decode("utf-8"),
#         admin = True
#     )
#     db.session.add(admin_user)

#     user1 = User(
#         email = "user1",
#         password = bcrypt.generate_password_hash("123456").decode("utf-8")
#     )
#     db.session.add(user1)
    
#     # commit the changes
#     db.session.commit()
#     print("Table seeded") 

# drop the tables client command
@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 