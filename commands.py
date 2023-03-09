from main import db
from flask import Blueprint
from main import bcrypt
from models.corkboard import Corkboard
from models.rescues import Rescue
from models.users import User
from datetime import date

db_commands = Blueprint("db", __name__)
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("seed")
def seed_db():
    from datetime import date
    # create the sample rescues
    rescue1 = Rescue(
        # Attributes only, SQLAlchemy to manage ID
        name = "Karen's Koala Sanctuary",
        classification = "koala's only",
        town = "Brisbane"
    )
    db.session.add(rescue1)

    rescue2 = Rescue(
        # Attributes only, SQLAlchemy to manage ID at this stage
        name = "Razor's Reptile Lodge",
        classification = "Reptiles",
        town = "Cairns"
    )
    db.session.add(rescue2)

    # create the sample corkboard notice

    notice1 = Corkboard(
        # Attributes only, SQLAlchemy to manage ID at this stage
        notice = "Activities for Volunteers",
        description = "Here you can post activities for volunteers such as supply runs, working b's and cleanups",
        date = date.today(),
        status = "Open"
    )
    db.session.add(notice1)

    admin_user = User(
        name = "Lars Jurly",
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    db.session.add(admin_user)

    user1 = User(
        name = "Samantha Puddingstone",
        email = "user1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user1)
    
    db.session.commit()
    print("Table seeded") 

# drop the tables client command
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 