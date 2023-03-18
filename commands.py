from main import db
from flask import Blueprint
from main import bcrypt
from models.corkboard import Corkboard
from models.rescues import Rescue
from models.users import User
from models.animals import Animal
# from models.rescues_animals import rescues_animals
from models.animals_rescues import animals_rescues
from models.responses import Response
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
    user2 = User.query.filter_by(email="user2@email.com").first()
    if not user2:
        user2 = User(
            name = "Karen Gum",
            email = "user2@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user2)
    
    user3 = User.query.filter_by(email="user3@email.com").first()
    if not user3:
        user3 = User(
            name = "Razor Jones",
            email = "user3@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user3)
    
    user4 = User.query.filter_by(email="user4@email.com").first()
    if not user4:
        user4 = User(
            name = "Maggie Molotov",
            email = "user4@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user4)
    
    user5 = User.query.filter_by(email="user5@email.com").first()
    if not user5:
        user5 = User(
            name = "Molly Russle",
            email = "user5@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
        db.session.add(user5)
    
    db.session.commit()
   
    # create the sample rescues
    # Check to see if rescue already exists
    rescue1 = Rescue.query.filter_by(name="Karen's Koala Sanctuary").first()
    if not rescue1:
        rescue1 = Rescue(
            # Attributes only, SQLAlchemy to manage ID
            name = "Karen's Koala Sanctuary",
            classification = "koalas only",
            town = "Brisbane",
            contact_number = "0410 111 111", 
            user_id = user2.id
        )
        db.session.add(rescue1)

    # Check to see if rescue already exists
    rescue2 = Rescue.query.filter_by(name="Razor's Reptile Lodge").first()
    if not rescue2:
        rescue2 = Rescue(
            # Attributes only, SQLAlchemy to manage ID at this stage
            name = "Razor's Reptile Lodge",
            classification = "reptiles",
            town = "Cairns",
            contact_number = "0410 222 222", 
            user = user3
        )
        db.session.add(rescue2)
    
    # Check to see if rescue already exists
    rescue3 = Rescue.query.filter_by(name="Maggie's Marsupial Madhouse").first()
    if not rescue3:
        rescue3 = Rescue(
            # Attributes only, SQLAlchemy to manage ID at this stage
            name = "Maggie's Marsupial Madhouse",
            classification = "marsupials",
            town = "Byron Bay",
            contact_number = "0410 333 333",
            user = user4
        )
        db.session.add(rescue3)
    
    # Check to see if rescue already exists
    rescue4 = Rescue.query.filter_by(name="Molly's Monotreme Rescue").first()
    if not rescue4:
        rescue4 = Rescue(
            # Attributes only, SQLAlchemy to manage ID at this stage
            name = "Molly's Montreme Rescue",
            classification = "monotremes",
            town = "Hobart",
            contact_number = "0410 444 444",
            user = user5
        )
        db.session.add(rescue4)

    # create the sample corkboard notice
    # Check to see if notice already exists
    corkboard1 = Corkboard.query.filter_by(notice="Activities for Volunteers").first()
    if not corkboard1:
        corkboard1 = Corkboard(
            # Attributes only, SQLAlchemy to manage ID at this stage
            notice = "Activities for Volunteers",
            where = "",
            description = "Here you can post activities for volunteers such as supply runs, working b's and cleanups",
            date = date.today(),
            status = "Open",
            user_id = admin_user.id
        )
    db.session.add(corkboard1)
    db.session.commit()
    response1 = Response(
    # set the attributes, not the id, SQLAlchemy will manage that for us
    response = "users can post responses if they'd like to assist with the volunteer activity.",
    user_id = admin_user.id,
    corkboard = corkboard1
    )
    # Add the object as a new row to the table
    db.session.add(response1)
    # Check to see if Koala already exists
    koala = Animal.query.filter_by(name="koala").first()
    if not koala:
        animal1 = Animal(
            name = "koala",
            classification = "marsupial"
        )
        db.session.add(animal1)
    # Check to see if Kangaroo already exists
    kangaroo = Animal.query.filter_by(name="kangaroo").first()
    if not kangaroo:
        animal2 = Animal(
            name = "kangaroo",
            classification = "marsupial"
        )
        db.session.add(animal2)
    # Check to see if Echidna already exists
    echidna = Animal.query.filter_by(name="echidna").first()
    if not echidna:
        animal3 = Animal(
            name = "echidna",
            classification = "monotreme"
        )
        db.session.add(animal3)
    # Check to see if Crocodile already exists
    crocodile = Animal.query.filter_by(name="crocodile").first()
    if not crocodile:
        animal4 = Animal(
            name = "crocodile",
            classification = "reptile"
        )
        db.session.add(animal4)

    db.session.commit()

    # # Check if rescues have already been associated with animals
    # if not db.session.query(rescues_animals).first():
    #     # Associate animals with rescues
    #     rescue1.animals = [animal1]
    #     rescue2.animals = [animal4]
    #     rescue3.animals = [animal1, animal2]
    #     rescue4.animals = [animal3]

    #     db.session.commit()

    #     print("Associations seeded")
    # else:
    #     print("Rescues have already been associated with animals, skipping seeding")
    # Check if rescues have already been associated with animals
    if not db.session.query(animals_rescues).first():
        # Associate animals with rescues
        animal1.rescues = [rescue1, rescue3]
        animal2.rescues = [rescue3]
        animal3.rescues = [rescue4]
        animal4.rescues = [rescue2]

        db.session.commit()

        print("Associations seeded")
    else:
        print("Animals have already been associated with rescues, skipping seeding")



        
    print("Tables seeded")
    
# drop the tables client command
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 