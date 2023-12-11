from appointment import Appointment
from datetime import datetime, timedelta
import os

# Application logic:
def create_weekly_calendar():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hours_of_day = list(range(9, 17))
    calendar = [Appointment(day, hour) for day in days_of_week for hour in hours_of_day]
    return calendar

def load_scheduled_appointments(appointments):
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    load_appointments = input("Would you like to load previously scheduled appointments from a file (Y/N): ")
    if load_appointments.lower() != 'y':
        return

def load_scheduled_appointments(appointments):
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    load_appointments = input("Would you like to load previously scheduled appointments from a file (Y/N): ")
    
    if load_appointments.lower() == 'y':
        filename = input("Enter appointment filename: ")
        file_loaded = False
        while not file_loaded:
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                        appointment = find_appointment_by_time(appointments, day_of_week, int(start_time_hour))
                        if appointment:
                            appointment.schedule(client_name, client_phone, int(appt_type))
                    print(f"{len(lines)} previously scheduled appointments have been loaded.")
                    file_loaded = True
            except FileNotFoundError:
                filename = input("File not found. Re-enter appointment filename: ")



def print_menu():
    print("Jojo's Hair Salon Appointment Manager")
    print("=====================================")
    print(" 1) Schedule an appointment")
    print(" 2) Find appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) Cancel an appointment")
    print(" 9) Exit the system")
    return input("Enter your selection: ")