## JamesLister_T2A2 
# WILDLIFE RESCUE API (WRAPI)<br>
<br>

## <u> ABOUT WRAPPI;</U>
<br>

The Wildlife Rescue API or "WRAPI" is being developed to give those interested in wildlife conservation a platform to communicate with one another as well as for those interested in establishing their own rescue. For those establishing their own rescue, they will be able to add a rescue and determine the species specialisation of that rescue. This is turn will help to establish and build a data base where a user can ultimately find a suitable rescue depending on the animal in need based on location. Finally the added feature of the app will be a corkboard for notifications where users will have the ability to post notices in regards to volunteer activities such as supply runs, clean ups, working B's etc. The problem this app is trying to solve is that with societies growing conservational conscience more and more people would like to become involved in protecting and caring for our wildlife. Many of these rescue organisations are just 1 or 2 man operations so there is no reason more people can't become involved, and if not to go as far as setting up a rescue but to assist with volunteering their time to those who already have.(R1) 

This is a problem that needs solving because currently there is not central hub for this specific type of application. Sure there are more established conservationists organisations, but it's harder to locate the smaller mum and pop rescues short of trawling through the typical social media postings of gum tree and face book. Having a REST API with a growing data base of these rescues and those interested in volunteering will afford people the opportunity to help and give them insights into the accessibility of our native wildlife's welfare operations as opposed to it being too hard, too far or not the right species. (R2)  

Postgres, the database system that this Flask Restful API has been structured around was chosen in part due to it's excellent performance and scalability. It's excellent security features which include support for encryption, row-level security and access controls were also another key reason for choosing postgres to work alongside flask's built in support for authentication and authorisation. Flexibility is another important factor in determining the use of postgres and flask as the flexible nature of postgres, supporting a wide range of data types and advanced features make it a great database system to run side by side with flasks flexible micro web framework. Finally the primary use of SQL (structured query language) programming language for interacting with the database is a huge draw card as it is a powerful, widely adopted language that works hand in hand with flask-SQLalchemy. Utilising SQL also helps in maintaining security and data integrity by enforcing constraints such as primary and foreign keys. The main drawbacks of using this database system would be complexity of development as it's challenging to work with the tools as a new developer and might have taken longer in comparison to some more intuitive database systems. Another drawback could be performance as it may not be the best choice for heavy traffic without optimisation. Finally, the maintenance and cleansing of the data and the database can be more intensive than other systems especially as the application becomes more complex and customized. Overall however, used in conjunction with flask and associated 3rd party applications, postgres is an excellent choice in database system for this particular application. (R3)

Object-Relational Mapping, or ORM, is a programming approach that converts a relational database management system's 'tables into object-oriented programming structures. A high level of abstraction to a relational database is provided by an ORM tool, which enables developers to interface with databases using common object-oriented fundamentals such as classes, schemas, objects, and methods. To outline the key functionalities of the ORM approach is firstly, the object-oriented model and the database schema are mapped by the ORM. This is done by utilising the metadata that explains how objects are saved in the database. In comparison to SQL, ORM offers a higher level of abstraction. Using a different object-oriented syntax, developer can query with ORM and return the results as objects. Another key functionality is caching, ORM utilises frequently used data in memory to reduce the number of queries and finally transaction management which means database operations can be grouped into singular atomic transactions which either succeed or fail as a group in a unit. The main benefits of an ORM are developer productivity, portability, security and performance. The ORM approach reduces the amount of code a developer needs to write enhancing productivity. By eliminating the need to write code over and over when switching between database management systems the ORM model increases portability. Overall the ORM approach is an invaluable method to enlist when working with relational databases as it offers a higher-level abstraction over the database, which can increase performance, security, portability, and productivity. (R4)

Just to go into detail on the 3rd party packages and services that are utilised in the app before you install them. The flask associated packages are used heavily and all of these can be viewed in the requirements.txt but we'll focus on the main ones. Flask-SQLAlchemy is used for the high level abstraction on the SQL programming language though postgres, bcrypt for the password hashing and encryption, flask-marshmallow for the schemas and object serialisation into json and Flask-JWT-Extended for the authorisation through use of bearer tokens. The only 3rd party service the app really utilises is when it loads in the current date when a user adds a corkboard notice. (R7)


## <u>INSTRUCTIONS ON HOW TO USE WRAPPI;</U>

### 1. Initialise postgres with wrapi_db database and user "wrapi_dev" with password "password123"

<br>Mac Users:
```
psql
```
Linux & WSL Users:
```
sudo -u postgres psql
```
And create the database in psql:
```
CREATE DATABASE wrapi_db;
```
Connect to the database:
```
\c wrapi_db;
```
Create the user to manage the wrapi_db database:
```
CREATE USER wrapi_dev WITH PASSWORD '123456';
```
Grant all permissions to db_dev:
```
GRANT ALL PRIVILEGES ON DATABASE wrapi_db TO wrapi_dev;
```
Finally, change owner of wrapi_db database to wrapi_dev:
```
ALTER DATABASE wrapi_db OWNER to wrapi_dev;
```
and exit postgres:
```
\q
```
### 2. Set up virtual environment and install packages from requirements text.
Create virtual environment if you don't already have one.
``` 
python3 -m venv .venv
```
Activate virtual environment:
```
source .venv/bin/activate
```
Install packages from requirements.txt:
```
pip install -r requirements.txt
```
### 3. Create the tables and seed the sample data and activate flask.

In the terminal with the virtual environment activated:<br>
create the table objects:
```
flask db create
```
Seed the sample data:
```
flask db seed
```
activate flask:
```
flask run
```

<br>

### 4. Now you are ready to manipulate the database through insomnia or postman via the following route end points.
<br>

## <u>END POINTS;</u>

### 1. **POST** REGISTER/CREATE USER - localhost:5000/auth/register<br>
```json
{"name": "Insert Name Here",
"email": "insertemail@email.com",
"password": "InsertPassword"}
```
**This registers/creates new user with bcrypt encrypted password hashing and JWT bearer token.*

### 2. **POST** LOGIN - localhost:5000/auth/login
```json
{"email": "existinguseremail@email.com",
"password": "ExistingPassword"}
```
**This returns bearer token for use on user specific functionality. Bearer token last 1 day before it expires.*

### 3. **GET** USERS - localhost:5000/users

**This returns all users in database and displays their associated rescues (if any).*

### 4. **DELETE** USERS BY ID - localhost:5000/users/ID
**Deletes user and all associated data, requires bearer token and can only be performed by the user themselves or the admin. Also deletes associated corkboards and rescues. (Doesn't delete associated animals as generally they will always be associated with other rescues)*

### 5. **POST** CREATE NEW RESCUE - localhost:5000/rescues
```json
{"name": "Insert Name of Rescue",
"classification": "Insert Classification",
"town": "Insert Town",
"contact_number": "1800 INSERT NUMBER"}
```
**This creates a rescue under the ID of the associated user (bearer access token required to determine user)*

### 6. **GET** RESCUES - localhost:5000/rescues

**This returns all rescues in database and lists all of the associated animals.*


### 7. **GET** RESCUE BY ID - localhost:5000/rescues/ID

**This return the specific rescue determined by ID and lists it's associated animals.*

### 8. **GET** SEARCH RESCUE BY TOWN OR CLASSIFICATION - localhost:5000/rescues/search?town=town or/ classification=classification

**This allows user to search for rescues by town or classification and is case insensitive.*

### 9. **PUT** UPDATE RESCUE BY ID - localhost:5000/rescues/ID
```json
{"name": "Update Name of Rescue",
"classification": "Update Classification",
"town": "Update Town",
"contact_number": "1800 UPDATE NUMBER"}
```
**This updates the specified rescue by ID (bearer access token of associated user required)*

### 10. **POST** ADD ANIMAL TO RESCUE BY ID - localhost:5000/rescues/ID/animals
```json
{"name": "Name of Animal",
"classification": "Classification"}
```
**This adds the species to the specified rescue by ID (bearer access token of associated user required) It also adds to an overall animals table which can have associations with other rescues.*

### 11. **DELETE** ANIMAL FROM RESCUE BY ID - localhost:5000/rescues/ID/animals
```json
{"name": "Name of Animal"}
```
**This deletes the species from the specified rescue by ID (bearer access token of associated user required) If the animal doesn't have associations with any other rescues it will be deleted from the database entirely. If it has associations with other rescues it will only be deleted from the associated rescue.*

### 12. **DELETE** RESCUE BY ID - localhost:5000/rescues/ID
**The associated user or the admin can delete the rescue by ID.*

### 13. **GET** ANIMALS - localhost:5000/animals
**This returns all animals in the database along with their classification and associated rescue information.*

### 14. **GET** ANIMALS BY ID - localhost:5000/animals/ID
**This returns the animal in the database corresponding to the animal ID*

### 15. **GET** SEARCH ANIMALS BY NAME OR CLASSIFICATION - localhost:5000/animals/search?name=name or/ classification=classification
**This allows user to search for animals by name or classification and is case insensitive. Returns the animal and classification along with any rescue details it's associated with.*

### 16. **DELETE** ANIMALS BY NAME OR CLASSIFICATION WITH NO RESCUE ASSOCIATIONS - localhost:5000/animals/delete?name=name or/ classification=classification
**Generally as the data within the database expands it will be uncommon for an animal to no longer be associated with a rescue which is why the animals aren't deleted even when a rescue is. This method can be used to clean up any stray animals that are no longer associated with any rescues by name or classification*

### 17. **DELETE** ALL ANIMALS WITH NO RESCUE ASSOCIATIONS - localhost:5000/animals/delete-all
**Again, it would be uncommon for an animal to longer be associated with a rescue. This method will clean up all of the data from the animals table if in case there are stray animals no longer associated with any rescues.* 


### 18. **GET** CORKBOARD NOTICES - localhost:5000/corkboards
**This returns all corkboard notices in the database along with associated user name and any responses.

### 19. **GET** CORKBOARD NOTICE BY ID - localhost:5000/corkboards/ID
**This returns the corkboard notice in the database corresponding to the ID*

### 20. **GET** SEARCH CORKBOARD NOTICES BY STATUS - localhost:5000/corkboard/search?status=status
**This allows user to search for corkboard notices by status and is case insensitive. Returns any notices with matching status along with user details and any responses.*

### 21. **POST** NEW CORKBOARD NOTICE - localhost:5000/corkboards
```json
{"notice": "Title of notice",
"where": "Location/ Rescue Organisation",
"description": "description of notice",
"status": "status"}
```
**This creates a corkboard notice under the ID of the associated user (bearer access token required to determine user). Automatically assigns the current date.*

### 22. **POST** RESPONSE TO CORKBOARD NOTICE BY ID - localhost:5000/ID/responses
```json
{"response": "Insert Response"}
```
**This allows users to respond to notices and responses will be attached to the notice determined by corkboard ID.*

### 23. **PUT** UPDATE CORKBOARD NOTICE BY ID - localhost:5000/corkboards/ID
```json
{"notice": "Update Title of notice",
"where": "Update Location/ Rescue Organisation",
"description": "Update description of notice",
"status": "Update status"}
```
**This updates the specified corkboard notice by ID (bearer access token of associated user required)*

### 24. **DELETE** CORKBOARD NOTICE BY ID - localhost:5000/corkboards/ID
**The associated user or the admin can delete the rescue by ID.*<br>
<br>

## <u> INFORMATION ABOUT WRAPPI_DB DATABASE'S RELATIONS;</U>
So if we're to go into the projects models and define the relationships they have with one another we should firstly focus on the most important part which is the relationship between Rescue and Animal. The Rescue model has a relationship with the User model through a foreign key, however the relationship with the Animal model is through join table "animals-rescues";
```python
class Rescue(db.Model):
    __tablename__= "rescues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())
    town = db.Column(db.String())
    contact_number = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animals = db.relationship("Animal", secondary=animals_rescues, back_populates="rescues", lazy="dynamic")
``` 
the join table is defined with both Foreign Keys animal_id and rescue_id, like so;
```python
animals_rescues = db.Table('animals_rescues',
    db.Column('animal_id', db.Integer, db.ForeignKey('animals.id')),
    db.Column('rescue_id', db.Integer, db.ForeignKey('rescues.id')))
```
and the Animal model like the Rescue model, has the secondary db.relationship with animals_rescues and back_populates itself;
```python
class Animal(db.Model):
    __tablename__= "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())
    rescues = db.relationship("Rescue", secondary=animals_rescues, back_populates="animals", lazy="dynamic")
```
The User model has relationships with the Rescue model, the Corkboard model and Response model through backrefs db.relationships with cascade="all, delete" abstraction to ensure that users can be deleted even with associated data.
```python
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    rescues = db.relationship("Rescue", backref="user", cascade="all, delete")
    corkboards = db.relationship("Corkboard", backref="user", cascade="all, delete")
    responses = db.relationship("Response", backref="user", cascade="all, delete")
```
Finally the Corkboard and Response models are both related back to the User model by foreignkey user_id however the Response model has a relationship to the Corkboard model through foreign key also. 
```python
class Corkboard(db.Model):
    __tablename__= "corkboards"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    notice = db.Column(db.String())
    where = db.Column(db.String())
    description = db.Column(db.String())
    status = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    responses = db.relationship("Response", backref="corkboard", cascade="all, delete")
```
```python
class Response(db.Model):
    __tablename__= "responses"
    id = db.Column(db.Integer,primary_key=True) 
    response= db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    corkboard_id = db.Column(db.Integer, db.ForeignKey("corkboards.id"), nullable=False)
``` 
(R8)

<br>
Now to go into some detail about the database tables and the relationships they have with one another we can start with the users table which has one to many relationships with the rescues table and the corkboards table. The users model allows for two levels of authorisation, one being the admin user who has top level authorisation and the other being general users who really only have authorisation over the rescues and corkboards they created. The rescues table has a many to many relationship with the animals table through a join table "animals_rescues". Finally corkboards table has a many to many relationship with the responses table where many users can post responses to many corkboard notices. (R9)

## <u>WRAPI ENTITY RELATIONSHIP DIAGRAM <br>
<br>

![WRAPI ERD](./docs/wrapi_ERD.drawio.png)

## <u>WRAPI PROJECT MANAGEMENT TASK ALLOCATION AND TRACKING <br>

To track and allocate the various tasks undertaken in the project a trello board was used with a kanban workflow which is an agile methodology designed to help visualise work, limit work-in-progress and maximize efficiency. I also used a git hub repository to manage the version control. First in the initial stages of the project development Design & Research tasks were mapped out along side a backlog of tasks I'd like to include in the applications development. Upon deciding that the approach mapped out in the back log and the design area were viable and relevant, they were moved to the "To-Do" area. These were then in turn moved to the "Doing" area as I was working on the specific task. Next, was moved into the code review area, then testing where it would remain until I was ready to test that part of the application. Finally when I was reasonably satisfied the aspect was functioning without errors I moved it into "Done". You can visit my trello board at - https://trello.com/b/RMD2Ap9Y/wildlife-rescue-api <br> also the github repository at https://github.com/JamJuiceCreative/JamesLister_T2A2 

![Kanban Board](./docs/trello_board.png)