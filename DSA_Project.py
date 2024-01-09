from SIR_Model import *
from SI_Model import *

choice = ""
while True:
    choice = input("Enter SI for SI model, SIR for SIR model, and exit to exit: ")
    
    if choice == "SI":
        transmission_chance = float(input("Enter transmission chance: "))
        number_of_people = int(input("Enter number of people: "))
        connections_per_person = int(input("Enter connections per person: "))
        connection_chance = float(input("Enter connection chance: "))
        Create_Random_SI(transmission_chance, number_of_people, connections_per_person, connection_chance)

    elif choice == "SIR":
        transmission_chance = float(input("Enter transmission chance: "))
        number_of_people = int(input("Enter number of people: "))
        connections_per_person = int(input("Enter connections per person: "))
        connection_chance = float(input("Enter connection chance: "))
        time_to_recover = int(input("Enter time to recover: "))
        Create_Random_SIR(transmission_chance, number_of_people, connections_per_person, connection_chance, time_to_recover)

    elif choice == "exit":
        break

    else:
        print("Try again")

    