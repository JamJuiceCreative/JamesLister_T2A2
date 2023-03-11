from main import db
from flask import Blueprint
from main import bcrypt
from models.corkboard import Corkboard
from models.rescues import Rescue
from models.users import User
from models.animals import Animal
from models.rescues_animals import rescues_animals
from datetime import date


db_commands = Blueprint("db", __name__)
@db_commands.cli.command("create")
def create_db():

    db.create_all()
    print("Tables created")

@db_commands.cli.command("seed")
def seed_db():
    # Check if users exist before creating them
    admin_user = User.query.filter_by(email="admin@email.com").first()
    if not admin_user:
    # Users are created first
        admin_user = User(
            name = "Lars Jurly",
            email = "admin@email.com",
            password = bcrypt.generate_password_hash("password123").decode("utf-8"),
            admin = True
        )
        db.session.add(admin_user)
    user1 = User.query.filter_by(email="user1@email.com").first()
    if not user1:
        user1 = User(
            name = "Karen Gum",
            email = "user1@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user1)
    
    user2 = User.query.filter_by(email="user2@email.com").first()
    if not user2:
        user2 = User(
            name = "Razor Jones",
            email = "user2@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user2)
    
    user3 = User.query.filter_by(email="user3@email.com").first()
    if not user3:
        user3 = User(
            name = "Maggie Molotov",
            email = "user3@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user3)
    
    user4 = User.query.filter_by(email="user4@email.com").first()
    if not user4:
        user4 = User(
            name = "Molly Russle",
            email = "user4@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user4)
    
    db.session.commit()
   
    # create the sample rescues
    # Check to see if rescue already exists
    rescue1 = Rescue.query.filter_by(name="Karen's Koala Sanctuary").first()
    if not rescue1:
        rescue1 = Rescue(
            # Attributes only, SQLAlchemy to manage ID
            name = "Karen's Koala Sanctuary",
            classification = "Koalas Only",
            town = "Brisbane",
            user_id = user1.id
        )
        db.session.add(rescue1)

    # Check to see if rescue already exists
    rescue2 = Rescue.query.filter_by(name="Razor's Reptile Lodge").first()
    if not rescue2:
        rescue2 = Rescue(
            # Attributes only, SQLAlchemy to manage ID at this stage
            name = "Razor's Reptile Lodge",
            classification = "Reptiles",
            town = "Cairns",
            user = user2
        )
        db.session.add(rescue2)
    
    # Check to see if rescue already exists
    rescue3 = Rescue.query.filter_by(name="Maggie's Marsupial Madhouse").first()
    if not rescue3:
        rescue3 = Rescue(
            # Attributes only, SQLAlchemy to manage ID at this stage
            name = "Maggie's Marsupial Madhouse",
            classification = "Marsupials",
            town = "Byron Bay",
            user = user3
        )
        db.session.add(rescue3)
    
    # Check to see if rescue already exists
    rescue4 = Rescue.query.filter_by(name="Molly's Monotreme Rescue").first()
    if not rescue4:
        rescue4 = Rescue(
            # Attributes only, SQLAlchemy to manage ID at this stage
            name = "Molly's Montreme Rescue",
            classification = "Monotremes",
            town = "Hobart",
            user = user4
        )
        db.session.add(rescue42)

    # create the sample corkboard notice
    # Check to see if notice already exists
    notice1 = Corkboard.query.filter_by(notice="Activities for Volunteers").first()
    if not notice1:
        notice1 = Corkboard(
            # Attributes only, SQLAlchemy to manage ID at this stage
            notice = "Activities for Volunteers",
            description = "Here you can post activities for volunteers such as supply runs, working b's and cleanups",
            date = date.today(),
            status = "Open",
            user_id = admin_user.id
        )
        db.session.add(notice1)
    # Check to see if Koala already exists
    koala = Animal.query.filter_by(name="Koala").first()
    if not koala:
        animal1 = Animal(
            name = "Koala",
            classification = "Marsupial"
        )
        db.session.add(animal1)
    # Check to see if Kangaroo already exists
    kangaroo = Animal.query.filter_by(name="Kangaroo").first()
    if not kangaroo:
        animal2 = Animal(
            name = "Kangaroo",
            classification = "Marsupial"
        )
        db.session.add(animal2)
    # Check to see if Echidna already exists
    echidna = Animal.query.filter_by(name="Echidna").first()
    if not echidna:
        animal3 = Animal(
            name = "Echidna",
            classification = "Monotreme"
        )
        db.session.add(animal3)
    # Check to see if Crocodile already exists
    crocodile = Animal.query.filter_by(name="Crocodile").first()
    if not crocodile:
        animal4 = Animal(
            name = "Crocodile",
            classification = "Reptile"
        )
        db.session.add(animal4)

    db.session.commit()

    # Check if rescues have already been associated with animals
    if not db.session.query(rescues_animals).first():
        # Associate animals with rescues
        rescue1.animals = [animal1]
        rescue2.animals = [animal4]
        rescue3.animals = [animal1, animal2]
        rescue4.animals = [animal3]

        db.session.commit()

        print("Table seeded")
    else:
        print("Rescues have already been associated with animals, skipping seeding")

# drop the tables client command
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 