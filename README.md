# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. 
Each assignment will build on the work done in the previous 
assignment(s). Ultimately, an entire system will be created to manage 
bank transactions for clients who have one or more bank accounts.

## Author

Rowan Mullin

## Assignment

Assignment 1: 2 classes were created to simulate clients and bank accounts.

Assignment 2: created 3 new BankAccount subclasses, savings, investment and chequing.

Assignment 3: we implemented 2 design patterns (observer and strategy) to setup notifs.

Assignment 4: we created a brand new gui for the bank system as well as logging.

Assignment 5: we implemented a sorting algorithm for accounts and made an installer with documentation.

## Encapsulation

Encapsulation was achieved in the BankAccount class, by making the 
attributes of the class private using name mangling, and creating the 
appropriate accessor methods and mutator methods to allow others to still 
access and change the attributes.

## Polymorphism

Polymorphism was used between the 3 new subclasses by overriding 
the `get_service_charges` method in each of the subclasses. This allowed 
the same method name to be used to calculate the service charges for each 
type of account, but with different implementations. 

## Strategy Pattern

I used the strategy pattern to design a common interface that I can then 
apply to all the bank accounts. This helps in a few ways, First it keeps 
the work of the fees solely to the interface, secondly if theres a new type
of account its much easier to implement, and lastly its easy to swap between
the options if i want to.

## Observer Pattern

I implemented the Observer pattern on the bank account and client classes so 
that the client can be notified about actions takin on their bank account(s).
The pattern helps with making it easy to update part of code with new information
and again helps decouple the work free from the classes its involved with. 

## Event-Driven Programming Paradigm

we use the event driven paradigm, through multiple aspects, we created buttons that respond by firing off signals when pressed; examples being the search button that finds the accounts linked to that client. we also setup slots that receive said signals and execute code, like the function that updates the GUI with the new account balance and the msg to update the csv file.

## Filtering

We implemented filtering into the search function of the application so that we can narrow down the results  we get back from a client search. The way we did this is by going through the bank accounts info 1 at a time and seeing if its related to the key the user is searching for, if its not related then the result is hidden because we know the user inst interested.