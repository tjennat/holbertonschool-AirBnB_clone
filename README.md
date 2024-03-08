# AirBnB Command Interpreter

This project is a command-line interface (CLI) tool developed as the first step towards building an AirBnB clone. The purpose of this tool is to manage AirBnB objects such as users, states, cities, places, etc., through various commands executed in the terminal.

## Command Interpreter

The command interpreter allows users to perform the following actions:

- Create a new object (e.g., User, Place)
- Retrieve an object from a file, database, etc.
- Perform operations on objects (e.g., count, compute stats)
- Update attributes of an object
- Destroy an object

### How to Start

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the command `./console.py` to start the command interpreter.

### How to Use

Once the command interpreter is running, you can enter commands to interact with AirBnB objects. The general syntax for commands is as follows:


Here are some examples of commands you can use:

- `create <class>`: Creates a new instance of the specified class.
- `show <class> <id>`: Displays information about the specified instance.
- `update <class> <id> <attribute> <value>`: Updates the specified attribute of an instance.
- `destroy <class> <id>`: Deletes the specified instance.
- `all <class>`: Displays all instances of the specified class.
- `quit` or `EOF`: Exits the command interpreter.

### Examples

1. Create a new user:

2. Show information about a specific place with ID 123:

3. Update the price attribute of a place with ID 456:

4. Destroy a user with ID 789:

5. Display all cities:

## Next Steps

This command interpreter serves as the foundation for building the complete AirBnB clone. In future steps, additional features such as HTML/CSS templating, database storage, API integration, and front-end development will be implemented.

For more information and detailed usage instructions, refer to the documentation and project resources.

**Note:** This project is part of a series of projects aimed at building a full-fledged AirBnB clone. Each subsequent project will build upon the functionalities implemented in this command interpreter.
