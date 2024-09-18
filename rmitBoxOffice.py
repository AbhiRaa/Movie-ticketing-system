# Fundamental Programming Assignment 1
# Student Name: Abhinav.
# Student Number: s3977487
# Highest part attempted: Part 3


# Data structures 
ticket_unit_price = {'adult' : 25.0, 'child' : 19.5, 'senior' : 17.0, 'student' : 20.5, 'concession' : 20.5}    # Price metric
movies_available = {'Avatar' : 50, 'Titanic' : 50, 'StarWar' : 50}    # List of all movies with total seats available
customer_names = ['Mary', 'James']     # Customer names that comes to buy tickets at the RMIT box office
reward_program_customer_list = ['Mary']   # Discount on total ticket cost applied for those customers who are in this rewards program
movies_revenue = {} # Nested dictinary to store all history of purchases on run time and also store revenue - 


# Initialize booking fee multiplier and discount percentage
booking_fee_multiplier = 2
discount = 0.2      # 20% discount


# Function to get the name of movie from the customer and valid that movie exists or not
def get_movie(customer_name):
    movie_name = input("Hello " + customer_name + "! Please enter the name of the movie you are looking for [enter a valid name only, e.g. Avatar]:    ")
    while movie_name not in movies_available:
        print("Sorry, that movie is not available. Please choose from the following options :    ")
        print(list(movies_available.keys()))
        movie_name = input("Please enter available movie name :    ")

    # Check for seat availability
    if movies_available[movie_name] <= 0:
        print("Sorry, no more seats are available for this movie")
        movie_name = get_movie(customer_name)

    return movie_name

# Function to calculate discount fee
def calculate_discount(total_ticket_cost, is_rewards_member):
    if is_rewards_member:
        discount_amount = discount * total_ticket_cost
        return discount_amount
    else:
        return 0
    

# Function to calculate booking fee
def calculate_booking(quantity):
    booking_fee = booking_fee_multiplier * quantity
    return booking_fee

# Function to add movies in the system
def add_movies(movies_list):
    existing_movie = []
    for movie in movies_list:
        if movie not in movies_available:
            movies_available[movie] = '50'
        else:
            existing_movie.append(movie)
    
    return existing_movie

# Function to purchase ticket 
def purchase_ticket():

    
    print("----------------Ticket Station----------------")
    customer_name = input("Hey there! Please enter your name [e.g. Huong]:      ")
    
    # Assuming that all customer name is unique
    while customer_name not in customer_names:
        customer_names.append(customer_name)

    # Ask for movie name
    movie_name = get_movie(customer_name)
    available_seats = movies_available[movie_name]

    # Ask for ticket types as comma seprated and checking that entered type is valid or not
    while True:
        ticket_type = input("Please enter the ticket types [enter a valid ticket type only, e.g. adult, child, senior, student, concession]:     ")
        ticket_types_list = ticket_type.split(',')
        
        # Remove leading/trailing whitespace from each value in the list
        refined_ticket_types_list = [value.strip() for value in ticket_types_list]
        
        # Comparing two sets to check if the input ticket types are valid not
        if set(refined_ticket_types_list).issubset(set(ticket_unit_price.keys())):
            break
        else:
            print("Sorry, ticket type is not valid. Please choose from the following options :     ")
            print(list(ticket_unit_price.keys()))

    # Ask for ticket quantity and validate for ticket quantities is valid or not
    while True:
        try:
            ticket_quantity = input("Please enter the ticket quantities [enter a positive interger only, e.g. 1, 2, 3]:       ")
            ticket_quantity_list = ticket_quantity.split(',')

            # Remove leading/trailing whitespace from each value in the list
            refined_ticket_quantity_list = [int(value.strip()) for value in ticket_quantity_list]

            # Sum of all ticket types quantity entered 
            total_quantity = sum(refined_ticket_quantity_list)

            if total_quantity <= 0:
                print("Invalid input: number of tickets must be a positive number")
                continue
            elif total_quantity > available_seats:
                print("Invalid input: number of tickets exceeds available seats, available number of seats are:     ", available_seats)
                continue
            else:
                break
        except ValueError:
            print("Invalid input: please enter a positive integer number of tickets")
            continue

    # First check if the customer is in the rewards program, if not ask if the customer wants to join it or not    
    if customer_name in reward_program_customer_list:
            is_rewards_member = True
    else:
        is_rewards_member = False
        reward_enroll = input("Hey " + customer_name + ", you are not in the rewards program. Would you like to join the rewards program [enter y or n]:        ")
        while reward_enroll not in ['y', 'n']:
                print("Sorry, that response is not valid. Please choose from the following options :     ")
                print(['y', 'n'])
                reward_enroll = input("Please enter valid response :     ")
        
        if reward_enroll == 'y':
            reward_program_customer_list.append(customer_name)
            is_rewards_member = True
            print("You have successfully joined the rewards program.")
            

    # Calculate total ticket cost, discount amount, and booking fee
    total_ticket_cost = 0
    for i in range(len(refined_ticket_types_list)):
        total_ticket_cost += ticket_unit_price[refined_ticket_types_list[i]] * refined_ticket_quantity_list[i]

    discount_amount = calculate_discount(total_ticket_cost, is_rewards_member)
    booking_fee = calculate_booking(total_quantity)
    total_cost = total_ticket_cost - discount_amount + booking_fee

    # Update available seats for the movie
    movies_available[movie_name] -= total_quantity

    # Display receipt to customer
    print("######################################################")
    print("                 Receipt of " + customer_name)
    print("######################################################")
    print("Movie :" + "                                      " + movie_name)
    for i in range(len(refined_ticket_types_list)):
        print("Ticket type :" + "                                " + refined_ticket_types_list[i])
        print("Ticket unit price :" + "                         ", ticket_unit_price[refined_ticket_types_list[i]])
        print("Ticket quantity :" + "                           ", refined_ticket_quantity_list[i])
        print("                    ---------------             ")

    print("######################################################")

    if discount_amount != 0.0:
        print("Discount :" + "                                  ", discount_amount)
    
    print("Booking fee :" + "                               ", booking_fee)
    print("Total cost :" + "                                ", total_cost)

    # Booking History:
    if movie_name not in movies_revenue:
        movies_revenue[movie_name] = {}
        
        # Initilize booking history with 0 values for the movie
        for original_ticket_type, _ in ticket_unit_price.items():
            movies_revenue[movie_name][original_ticket_type] = 0
            movies_revenue[movie_name]["total_cost"] = 0

    # Add current purchase to booking history
    for i in range(len(refined_ticket_types_list)):
        movies_revenue[movie_name][refined_ticket_types_list[i]] += refined_ticket_quantity_list[i]
    
    #  Adding total cost to booking history
    movies_revenue[movie_name]["total_cost"] += total_cost
        
    # Ask customer if they want to make another purchase
    another_purchase = input("Would you like to make another purchase? (y/n):   ")
    while another_purchase not in ['y', 'n']:
        another_purchase = input("Sorry, that response is not valid. Please choose from the following options (y/n):     ")
    if another_purchase == 'y':
        purchase_ticket()


# Function to display customers information table that already exists in the system
def display_customer_info():
    # List for reward customers information with respect to the customers list
    reward_program = []
    for customer in customer_names:
        if customer in reward_program_customer_list:
            reward_program.append('Yes')
        else:
            reward_program.append('No')

    # Define the column headers
    header = ["Customers", "Member"]

    # Print the header row
    print("{:<10} {:<10}".format(header[0], header[1]))

    # Print the separator row
    print("-" * 20)

    # Print the data rows
    for i in range(len(customer_names)):
        print("{:<10} {:<10}".format(customer_names[i], reward_program[i]))


# Function to display every movie name and seats available
def display_movies_info():
    # Get the maximum length of the keys and values
    max_key_length = max(len(str(key)) for key in movies_available.keys())
    max_value_length = max(len(str(value)) for value in movies_available.values())

    # Print the table headers
    print(f"{'Movie':<{max_key_length}}   {'Seats_left':<{max_value_length}}")
    print('-' * (max_key_length + max_value_length + 11))

    # Print each key-value pair as a row in the table
    for key, value in movies_available.items():
        print(f"{key:<{max_key_length}}   {value:<{max_value_length}}")

# Function to display popular movie as per revenue
def display_popular_movie():
    max_revenue = 0
    popular_movie = ""
    for movie, history in movies_revenue.items():
        if history["total_cost"] > max_revenue:
            max_revenue = history["total_cost"]
            popular_movie = movie

    print(popular_movie)

# Function to display movie purchase history and revenue
def display_movie_records():
    header_string = " " * 20
    for type, _ in ticket_unit_price.items():
        header_string += type + " "
    header_string += "Revenue"
    print(header_string)

    for movie, history in movies_revenue.items(): 
        movie_string = movie + " " * (22 - len(movie))
        for type, _ in ticket_unit_price.items():
            movie_string += str(history[type]) + "      "

        movie_string += str(history["total_cost"])
        print(movie_string)
            

# Function to display the menu and get customer choice
def show_menu():
    print("----------------Welcome to the RMIT box office!----------------")
    print("1. Purchase a ticket")
    print("2. Add movies")
    print("3. Display existing customers information")
    print("4. Display existing movies information")
    print("5. Display the most popular movie")
    print("6. Display all movie record")
    print("7. Exit")

    # Validate choices
    choice_list = ['1', '2', '3', '4', '5', '6', '7']
    choice = input("Enter your choice (1-7):      ")
    while choice not in choice_list:
        print("Sorry, this is not a valid option. Please choose from 1 to 7 :    ")
        choice = input("Please enter your choice again :    ")
    return choice

# Main driving loop for this ticketing system menu
while True:
    
    # Display the menu and get choice
    choice = show_menu()

    if choice == '1':
        purchase_ticket()
        continue
    
    if choice == '2':
        requested_movies = input("Enter the movies you want to add separated by comma :     ")
        requested_movies_list = requested_movies.split(',')

        # Remove leading/trailing whitespace from each value in the list
        requested_movies_list = [value.strip() for value in requested_movies_list]

        # Call to add the entered list of movies
        existing_movies = add_movies(requested_movies_list)
        if existing_movies != []:
            print("These movies already exists in the system :      ", existing_movies)

        continue

    if choice == '3':
        display_customer_info()
        continue
    
    if choice == '4':
        display_movies_info()
        continue
    
    if choice == '5':
        display_popular_movie()
        continue

    if choice == '6':
        display_movie_records()
        continue

    if choice == '7':
        break

print("Thank you for using the RMIT box office!")
