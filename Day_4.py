flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100},
    "UK301": {"source": "Delhi", "dest": "Kolkata", "seats": 2, "price": 6000},
    "UK302": {"source": "Kolkata", "dest": "Delhi", "seats": 6, "price": 6200},
    "SG401": {"source": "Hyderabad", "dest": "Pune", "seats": 10, "price": 4000},
    "SG402": {"source": "Pune", "dest": "Hyderabad", "seats": 7, "price": 4100},
    "QP501": {"source": "Ahmedabad", "dest": "Delhi", "seats": 5, "price": 3500},
    "QP502": {"source": "Delhi", "dest": "Ahmedabad", "seats": 9, "price": 3600}
}

def search_flight(source, destination):
    for flight_no, details in flights.items():
        if details["source"].lower() == source.lower() and details["dest"].lower() == destination.lower():
            return flight_no
    return None

def display_flight(flight_no):
    details = flights[flight_no]
    print("\nFlight Number :", flight_no)
    print("Source :", details["source"])
    print("Destination :", details["dest"])
    print("Available Seats :", details["seats"])
    print("Price :", details["price"])

def book_ticket(flight_no, seats_required):
    if seats_required <= flights[flight_no]["seats"]:
        flights[flight_no]["seats"] -= seats_required
        print("\nBooking Confirmed")
        print("Seats Booked :", seats_required)
        print("Remaining Seats :", flights[flight_no]["seats"])
    else:
        print("\nBooking Failed")
        print("Not enough seats available")

# User Input
source = input("Enter Source Airport: ")
destination = input("Enter Destination Airport: ")

flight_no = search_flight(source, destination)

if flight_no:
    display_flight(flight_no)

    seats_required = int(input("Enter number of seats to book: "))
    book_ticket(flight_no, seats_required)

    print("\nUpdated Flight Details")
    display_flight(flight_no)
else:
    print("No flights available for the given route")
