# Movie-ticketing-system
Functionalities Requirements:
------------------------------------------------ PART 1 ------------------------------------------------
In this part, your program can perform some simple interactions with users (i.e., the box office cashiers
or the managers):
1. Display a message asking the user to enter the customer’s name.
2. Display a message asking the user to enter the movie’s name. In this part, you can assume the
movie to be entered is always a valid movie.
3. Display a message asking the user to enter the ticket type the customer chooses. In the system,
there are 5 ticket types for customers to choose from: adult, child, senior, student, concession.
In this part, you can assume the ticket type to be entered is always a valid ticket type.
4. Display a message asking the quantity of the tickets ordered by the customer. In this part, you
can assume the quantity to be entered is always a positive integer, e.g., 1, 2, 3 ...
5. Calculate the total cost for the customer including the discount fee and booking fee (see No. 6,
7 and 8 below). The total cost is equal to the total ticket cost – discount fee + the booking fee.
6. The unit price for the ticket types adult, child, senior, student, concession are 25.0, 19.5, 17.0,
20.5, and 20.5, respectively. All the movies have the same ticket price structure. The total ticket
cost for a particular ticket type is equal to the price of that ticket type multiplying with the
ticket quantity. For example, if the quantity ordered by the customer is 2, the ticket type is
adult, then the total ticket cost is 25 x 2 = 50$.
7. For customers that are in the rewards program, 20% discount will apply. No discount for
customers that are not in the rewards program. The discount fee is computed based on the total
ticket cost. For example, if the total ticket cost is 50$, then the discount fee is 20% x 50 = 10$.
8. For all customers, for all ticket types, the booking fee is 2 x the ticket quantity. For example,
if the quantity ordered by the customer is 2, then the booking fee is 2 x 2 = 4$.
9. The total cost will be displayed as a formatted message to the user, e.g.,
------------------------------------------------------------------------------
Receipt of <customer_name>
------------------------------------------------------------------------------
Movie: <movie_name>
Ticket type: <ticket_type>
Ticket unit price: <ticket_unit_price>
Ticket quantity: <ticket_quantity>
------------------------------------------------------------------------------
Discount: <discount_fee>
Booking fee: <booking_fee>
Total cost: <total_cost>
10. In the program, you should have some lists (or dictionaries or other data types) to store the
names of all customers, the names of the customers that are in the rewards program, the
available movies, the available ticket types, the prices of those ticket types. You can assume
the customer names, the movie names, and the ticket types are all unique and case sensitive.
11. When a new customer orders a ticket(s), your program will add the customer's name to the
customer list. Also, when any customer orders a ticket, your program will check if they are in
the rewards program; if they are not in the rewards program, your program will display a
message asking if they want to register to be in the rewards program. If yes, then your program
will add the customer's name to the rewards program. The discount fee is applied immediately
after the customer is added to the rewards program. In this part, you can assume the answer
entered is always either y or n (meaning yes or no, respectively).
12. Your program needs to be initialized with the following customers: Mary (a customer in the
rewards program), and James (a customer not in the rewards program). Your program also
needs to be initialized with the following movies: Avatar, Titanic, and StarWar.
13. Note: in the requirements No. 10 & 11, we use the term 'list' when describing the customer list,
the customer in the rewards program list, etc. But you can use other data types to store this
information such as dictionaries and other data types. Make sure you think and analyse the
requirements in detail so that you can choose the most appropriate/suitable data types.
------------------------------------------------ PART 2 ------------------------------------------------
In this part, your program can: 
(a) perform some additional requirements compared to PART 1, and
(b) be operated using a menu.
First, compared to the requirements in PART 1, now your program will have the following features:
i. Each movie is associated with a number of seats. After each purchase, the number of available
seats for the purchased movie needs to be updated accordingly. Your program needs to be
initialized with 50 tickets per each movie.
ii. Handle invalid inputs from users:
a. Display an error message if the movie entered by the user is not a valid movie. When this
error occurs, the user will be given another chance, until a valid movie is entered.
b. Display an error message if the ticket type entered by the user is not a valid ticket type. When
this error occurs, the user will be given another chance, until a valid ticket type is entered.
c. Display an error message if the ticket quantity is 0, negative, not an integer, or exceed the
number of available seats. When this error occurs, the user will be given another chance, until
a valid quantity is entered.
d. Display an error message if the answer by the user is not y or n when asking if the customer
wants to join the rewards program. When this error occurs, the user will be given another
chance, until a valid answer (i.e., y, n) is entered.
Second, your program will be operated using a menu. A menu-driven program is a computer program
in which options are offered to the users via the menu. Your program will have the following options:
Purchase a ticket, add movies, display existing customers information, display existing movies
information, exit the program (please see Section 5 in this document regarding an example of how the
menu program might look like). Below are the specifications of the options:
1. Purchase a ticket: this option includes all the requirements from 1 to 13 in PART 1 and the
requirements i to ii in the first part of PART 2.
2. Add movies: this option displays a message asking if users want to add a list of movies. The
movies must be entered as a list that separates by commas with the following format: movie_1,
movie_2, movie_3, ... For example, users can enter the input: Titanic, Avenger, Frozen to add
the movies Titanic, Avenger, and Frozen. If a movie is new, then the movie and its initial
numbers of seats (50) will be added to the data collection of the program. If a movie is an
existing movie, your program will print a message saying this is an existing movie, so it does
not do anything. You can assume the movie names are always unique, and each movie name is
a single word with no space nor commas. You can assume users always enter the correct
formats (i.e., using commas to separate the movie names), but note that users can enter multiple
spaces before/after the commas.
3. Display existing customers information: this option displays on screen all existing customers
and their rewards program information (whether they're in or not in the rewards program). The
messages are flexible (your choice), but they should show all the information required.
4. Display existing movies information: this option displays all the movies with their numbers of
available seats. The messages are flexible (your choice), but they should show all the
information required.
5. Exit the program: this option allows users to exit the program.
Note that in your program, when a task (option) is accomplished, the menu will appear again for the
next task.
------------------------------------------------ PART 3 ------------------------------------------------
In this part, your menu program is equipped with some advanced features. Note, some features maybe
very challenging.
1. In this part, in the "Purchase a ticket" option, your program will allow customers to purchase
multiple ticket types in one order. To do so, your program will ask users to input a list of ticket
types, and then a list of the ticket quantities that correspond to the ticket types in the previous
list. The items in these two lists are separated by commas. For example, users can enter a list
of ticket types: adult, child, senior and then a list of ticket quantities: 2, 1, 1, meaning that users
want to purchase 2 adult tickets, 1 child ticket, and 1 senior ticket. You can assume the number
of ticket types entered is the same as the number of ticket quantities entered. Note that, in this
option, if the user only enters one ticket type and one ticket quantity as in the previous 2 parts,
then your program will still work as normal (as in PART 2). Besides, your program needs to
handle invalid inputs. Specifically, if the lists contain any invalid ticket type or ticket quantity
(0, negative, not integers, or total quantities in the list exceeds the number of available seats),
then your program will display a message saying the corresponding list is not valid, and the
user will be given another chance (re-enter the lists), until all valid ticket types and ticket
quantities are entered. The formatted message for the receipt is as follows.
------------------------------------------------------------------------------
Receipt of <customer_name>
------------------------------------------------------------------------------
Movie: <movie_name>
Ticket type: <ticket_type>
Ticket unit price: <ticket_unit_price>
Ticket quantity: <ticket_quantity>
...............
Ticket type: <ticket_type>
Ticket unit price: <ticket_unit_price>
Ticket quantity: <ticket_quantity>
------------------------------------------------------------------------------
Discount: <discount_fee>
Booking fee: <booking_fee>
Total cost: <total_cost>
2. The menu also has an option "Display the most popular movie" to display the movie with the
maximum money (total cost) purchased by users to date and the amount of money it was
purchased. If there are multiple movies with the same maximum money purchased, you can
display only one movie or all movies, it's your choice.
3. The menu now has an option "Display all movie record". The option will display a table
displaying all the previous purchases of all movies, including the ticket types and the quantity
for each ticket type they purchased and the total cost (including all the fees). An example table
is as follows.
adult child senior student concession Revenue
Titanic 12 3 8 10 4 720.5
Avatar 15 7 5 14 6 924.6
StarWar 14 8 6 11 5 860.8