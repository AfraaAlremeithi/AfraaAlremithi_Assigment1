class Passenger:
    def __init__(self, lastName, firstName, ticketNumber, seatNumber, electronicTicket, departureCity, destination):
        self.lastName = lastName
        self.firstName = firstName
        self.ticketNumber = ticketNumber
        self.seatNumber = seatNumber
        self.electronicTicket = electronicTicket
        self.departureCity = departureCity
        self.destination = destination

    # Setters and getters
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setTicketNumber(self, ticketNumber):
        self.ticketNumber = ticketNumber

    def getTicketNumber(self):
        return self.ticketNumber

    def setSeatNumber(self, seatNumber):
        self.seatNumber = seatNumber

    def getSeatNumber(self):
        return self.seatNumber

    def setElectronicTicket(self, electronicTicket):
        self.electronicTicket = electronicTicket

    def getElectronicTicket(self):
        return self.electronicTicket

    def setDepartureCity(self, departureCity):
        self.departureCity = departureCity

    def getDepartureCity(self):
        return self.departureCity

    def setDestinationCity(self, destination):
        self.destination = destination

    def getDestinationCity(self):
        return self.destination

class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, gate, terminal):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate
        self.terminal = terminal

    # Setters and getters
    def setFlightNumber(self, flight_number):
        self.flight_number = flight_number

    def getFlightNumber(self):
        return self.flight_number

    def setDepartureTime(self, departure_time):
        self.departure_time = departure_time

    def getDepartureTime(self):
        return self.departure_time

    def setArrivalTime(self, arrival_time):
        self.arrival_time = arrival_time

    def getArrivalTime(self):
        return self.arrival_time

    def setGate(self, gate):
        self.gate = gate

    def getGate(self):
        return self.gate

    def setTerminal(self, terminal):
        self.terminal = terminal

    def getTerminal(self):
        return self.terminal


class BoardingPassSystem:
    def __init__(self):
        self.boardingPass = None

    def generatePass(self): #generate boarding pass
        pass

    def updatePass(self):   #update boarding pass
        pass


class BoardingPass:
    def __init__(self, passenger, flight, boardingTime, till):
        self.passenger = passenger
        self.flight = flight
        self.boardingTime = boardingTime
        self.till = till

    # Setters and getters
    def setPassenger(self, passenger):
        self.passenger = passenger

    def getPassenger(self):
        return self.passenger

    def setFlight(self, flight):
        self.flight = flight

    def getFlight(self):
        return self.flight

    def setBoardingTime(self, boardingTime):
        self.boardingTime = boardingTime

    def getBoardingTime(self):
        return self.boardingTime

    def setTill(self, till):
        self.till = till

    def getTill(self):
        return self.till

# Passengers object
passenger1 = Passenger("Smith", "James", 629, "09A", "5A6BCD78", "CHICAGO ORD", "NEW YORK JFK")
passenger2 = Passenger("Afraa", "Alremeithi", 655, "22B", "84NB1S62", "CHICAGO ORD", "NEW YORK JFK")

# Flight object
flight1 = Flight("NA4321", "11:40", "13:30", "03", "2")
flight2 = Flight("NA4321", "11:40", "13:30", "03", "2")

#Pass object
pass1 = BoardingPass(passenger1, flight1, "11:20", "11:40")
pass2 = BoardingPass(passenger2, flight2, "11:20", "11:40")
# Display details of pass1
print("NATIONAL AIRLINES FIRST CLASS")
print("Passenger 1 Boarding Pass:")
print(f"Name: {pass1.getPassenger().getFirstName()} {pass1.getPassenger().getLastName()}, Departure City: {pass1.getPassenger().getDepartureCity()}, Destination City: {pass1.getPassenger().getDestinationCity()}")
# Display details of pass2
print("NATIONAL AIRLINES FIRST CLASS")
print("Passenger 2 Boarding Pass:")
print(f"Name: {pass2.getPassenger().getFirstName()} {pass2.getPassenger().getLastName()}, Departure City: {pass2.getPassenger().getDepartureCity()}, Destination City: {pass2.getPassenger().getDestinationCity()}")
