# JamesLister_T2A2
## WILDLIFE RESCUE API (WRAPI)<br>
<br>

The Wildlife Rescue API or "WRAPI" is being developed to give those interested in wildlife conservation a platform to communicate with one another as well as for those interested in establishing their own rescue. For those establishing their own rescue, they will be able to add a rescue and determine the species specialisation of that rescue. This is turn will help to establish and build a data base where a user can ultimately find a suitable rescue depending on the animal in need based on location. Finally the added feature of the app will be a corkboard for notifications where users will have the ability to post notices in regards to volunteer activities such as supply runs, clean ups, working B's etc. The problem this app is trying to solve is that with societies growing conservational conscience more and more people would like to become involved in protecting and caring for our wildlife. Many of these rescue organisations are just 1 or 2 man operations so there is no reason more people can't become involved, and if not to go as far as setting up a rescue but to assist with volunteering their time to those who already have.(R1) 

This is a problem that needs solving because currently there is not central hub for this specific type of application. Sure there are more established conservationists organisations, but it's harder to locate the smaller mom and pop rescues short of trawling through the typical social media postings of gum tree and face book. Having a REST API with a growing data base of these rescues and those interested in volunteering will afford people the opportunity to help and give them insights into the accessibility of our native wildlife's welfare operations as opposed to it being too hard, too far or not the right species. (R2)  

Postgres, the database system that this Flask Restful API has been structured around was chosen in part due to it's excellent performance and scalability. It's excellent security features which include support for encryption, row-level security and access controls were also another key reason for choosing postgres to work alongside flask's built in support for authentication and authorisation. Flexibility is another important factor in determining the use of postgres and flask as the flexible nature of postgres, supporting a wide range of data types and advanced features make it a great database system to run side by side with flasks flexible micro web framework. Finally the primary use of SQL (structured query language) programming language for interacting with the database is a huge draw card as it is a powerful, widely adopted language that works hand in hand with flask-SQLalchemy. Utilising SQL also helps in maintaining security and data integrity by enforcing constraints such as primary and foreign keys. The main drawbacks of using this database system would be complexity of development as it's challenging to work with the tools as a new developer and might have taken longer in comparison to some more intuitive database systems. Another drawback could be performance as it may not be the best choice for heavy traffic without optimisation. Finally, the maintenance and cleansing of the data and the database can be more intensive than other systems especially as the application becomes more complex and customized. Overall however, used in conjunction with flask and associated 3rd party applications, postgres is an excellent choice in database system for this particular application. (R3)

* R4 Identify and discuss the key functionalities and benefits of an ORM<br>

Object-Relational Mapping, or ORM, is a programming approach that converts a relational database management system's 'tables into object-oriented programming structures. A high level of abstraction to a relational database is provided by an ORM tool, which enables developers to interface with databases using common object-oriented fundamentals such as classes, schemas, objects, and methods. To outline the key functionalities of the ORM approach is firstly, the object-oriented model and the database schema are mapped by the ORM. This is done by utilising the metadata that explains how objects are saved in the database. In comparison to SQL, ORM offers a higher level of abstraction. Using a different object-oriented syntax, developer can query with ORM and return the results as objects. Another key functionality is caching, ORM utilises frequently used data in memory to reduce the number of queries and finally transaction management which means database operations can be grouped into singular atomic transactions which either succeed or fail as a group in a unit. The main benefits of an ORM are developer productivity, portability, security and performance. The ORM approach reduces the amount of code a developer needs to write enhancing productivity. By eliminating the need to write code over and over when switching between database management systems the ORM model increases portability. Overall the ORM approach is an invaluable method to enlist when working with relational databases as it offers a higher-level abstraction over the database, which can increase performance, security, portability, and productivity.

* R5 Document all endpoints for your API

* R6 An ERD for your app


* R7 Detail any third party services that your app will use


* R8 Describe your projects models in terms of the relationships they have with each other


* R9 Discuss the database relations to be implemented in your application


* R10 Describe the way tasks are allocated and tracked in your project


Database Permissions -  Name = wrapi_db
                        Owner = wrapi_dev
                        Password = password123