# Over-engineered Caesser's Cypher Hello-World MVC
Example for an over engineered model view controller in python

The user can input a message, which the application encrypts using a Caesar's cipher the message "Hello Username" with a random shift.
The encrypted message is then passed to the view component, which displays it in the console.
The shift value for Caesar's cipher can be adjusted in the controller component by having the user input a number.
In case the user guesses the correct shift value, the application will congratulate the user.

### What is an MVC?
MVC - Model View Controller

The Model-View-Controller (MVC) is an architectural pattern that separates an application into three main logical components: 

- Model - Application core, data and business logic -> responsible for maintaining data
- View - Representation of data -> takes data from the model and renders it
- Controller -> User input receiver -> glues together model and view

Each of these components are built to handle specific development aspects of an application. MVC is one of the most frequently used industry-standard web development framework to create scalable and extensible projects.

### How to run
1. Clone the repository
2. Run the main.py file in the root directory
    ```bash
    python main.py
    ```
3. Follow the instructions in the console