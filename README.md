# AirBnB Clone - The Console

## Description:

The AirBnB clone project's goal is to build a simple copy of the Airbnb website, and to deploy it on a server.
The project is divided in 4 sub-projects:

- The console:
A command interpreter to manipulate data without a visual interface, like in a Shell.

- The Website:
The front-end that shows the final product to everybody (static and dynamic).

- The Database.

- An API:
Provides a communication interface between the front-end and your data (retrieve, create, delete, update them).

This README focuses on the 1st sub-project
(The Console).


# The Console


### Created to:
- Manage (create, update, destroy, etc) objects via a console / command interpreter.
- Store and persist objects to a file (JSON file).

### Learning objectives:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function


## Command interpreter

### How to start it:
1. Clone the git repository:
https://github.com/tomasgvgt/AirBnB_clone.git

2. Run the program:
./console.py


### How to use it:

| Command | Description | Usage | Example |
| ------- | ----------- | ----- | ------- |
| help | Shows documentation for each command. | `help <command>` | help create |
| quit | Exits the interpreter. | exit | exit |
| create | Creates a new instance of a class and saves it (to a JSON file) and prints the id. | `create <class name>` | create User |
| show | Prints the string representation of an instance based on the class name and id. | `show <class name> <id>` or `<class name>.show(<id>)` | show BaseModel 1234-1234-1234 |
| destroy |  Deletes an instance based on the class name and id (saves the change into the JSON file). | `destroy <class name> <id>` or `<class name>.destroy(<id>)` | destroy BaseModel 1234-1234-1234 |
| all | Prints all string representation of all instances based or not on the class name. | `all <class name>` | all BaseModel |
| update |  Updates an instance based on the class name and id by adding or updating attribute (saves the change into the JSON file). | `update < class name > < id > < attribute > <value>` or `<class name>.update(<id>, <attribute name>, <attribute value>)` | update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" |
| count | Retrieves the number of instances of a class. | `<class name>.count()` | User.count() |

## Classes

- BaseModel
- User
- City
- Amenity
- State
- Place
- Review

## FileStorage

Flow of serialization and descerialization to save and reload all the instances created.

`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`

# Tests

All files, classes and functions were tested with Unittests.
Check the tests folder for all the test files.


# Authors

- Luis Carvajal Villa
- Tomas Gomez Velez
