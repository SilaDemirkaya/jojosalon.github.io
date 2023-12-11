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


def find_appointment_by_time(appointments, day_of_week, start_time_hour):
    # Convert inputs to the proper format (if necessary)
    day_of_week = day_of_week.lower()
    start_time_hour = int(start_time_hour)

    for appointment in appointments:
        # Convert appointment attributes to the same format as inputs
        if appointment.day_of_week.lower() == day_of_week and appointment.start_time_hour == start_time_hour:
            return appointment

    return None



def show_appointments_by_name(appointments, client_name):
    matching_appointments = [appointment for appointment in appointments if appointment.client_name and client_name.lower() in appointment.client_name.lower()]
    for appointment in matching_appointments:
        print(appointment)

def show_appointments_by_day(appointments, day_of_week):
    for appointment in appointments:
        if appointment.day_of_week.lower() == day_of_week.lower():
            client_name = getattr(appointment, 'client_name', '').ljust(20)
            client_phone = getattr(appointment, 'client_phone', '').ljust(15)

            start_time_formatted = f"{appointment.start_time_hour:02d}:00" if hasattr(appointment, 'start_time_hour') else ""
            end_time_formatted = f"{appointment.get_end_time_hour():02d}:00" if hasattr(appointment, 'get_end_time_hour') else ""

            appt_type_desc = appointment.get_appt_type_desc()
            # Remove the price part from the appointment type description
            appt_type_desc = appt_type_desc.split('$')[0].strip()

            print(f"{client_name} {client_phone} {appointment.day_of_week:10} {start_time_formatted} - {end_time_formatted}   {appt_type_desc}")


def save_scheduled_appointments(appointments, filename):
    try:
        with open(filename, 'w') as file:
            count = 0
            for appointment in appointments:
                if appointment.appt_type != 0:
                    file.write(appointment.format_record() + "\n")
                    count += 1
            print(f"{count} scheduled appointments have been successfully saved")
    except Exception as e:
        print(f"Error saving appointments: {e}")


def main():
    appointments = create_weekly_calendar()
    load_scheduled_appointments(appointments)

    running = True
    while running:
        choice = print_menu()

        if choice == '1':
            print('** Schedule an appointment **')
            day_of_week = input("What Day: ")
            start_time_hour = int(input("Enter start hour (24 hour clock): "))

            appointment = find_appointment_by_time(appointments, day_of_week, start_time_hour)

            # Check if the appointment slot is already booked
            if appointment and appointment.client_name:  # Assuming that a booked appointment has a client name
                print("Sorry, that time slot is booked already!")
            elif appointment:
                client_name = input("Client Name: ")
                client_phone = input("Client Phone: ")

                print('Appointment types')
                print('1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120')
                appt_type = int(input("Type of Appointment: "))

                if appt_type in [1, 2, 3, 4]:
                    appointment.schedule(client_name, client_phone, appt_type)
                    print(f"OK, {client_name}'s appointment is scheduled!")
                else:
                    print("Sorry that is not a valid appointment type!")
            else:
                print("Sorry that time slot is not in the weekly calendar!")



        elif choice == '2':
            print('** Find appointment by name **')
            client_name = input("Enter Client Name: ")
            print("Client Name         Phone          Day       Start     End       Type")
            print("-------------------------------------------------------------------------------------")
            show_appointments_by_name(appointments, client_name)

        elif choice == '3':
            print('** Print calendar for a specific day **')
            day_of_week = input("Enter the day of the week: ")
            print(f"Appointments for {day_of_week}")
            print("Client Name         Phone          Day       Start     End       Type")
            print("-------------------------------------------------------------------------------------")
            show_appointments_by_day(appointments, day_of_week)

        elif choice == '4':  # Cancel an Appointment
            print('** Cancel an appointment **')
            day_of_week = input("What day: ")
            start_time_hour = int(input("Enter start hour (24 hour clock): "))
            appointment = find_appointment_by_time(appointments, day_of_week, start_time_hour)

            if appointment:
                if appointment.client_name:
                    client_name_to_cancel = appointment.client_name
                    end_time_hour = appointment.get_end_time_hour()
                    appointment.cancel()
                    print(f"Appointment: {day_of_week} {start_time_hour:02d}:00 - {end_time_hour:02d}:00 for {client_name_to_cancel} has been cancelled!")
                else:
                    print("That time slot isn't booked and doesn't need to be cancelled")
            else:
                print("Sorry that time slot is not in the weekly calendar!")


        elif choice == '5':  # Save Scheduled Appointments
            save_scheduled_appointments(appointments)

        elif choice == '9':  # Exit the System
            print('** Exit the system **')
            save_appointments = input("Would you like to save all scheduled appointments to a file (Y/N)? ").strip().lower()

            while save_appointments == 'y':
                filename = input("Enter appointment filename: ")
                file_exists = os.path.exists(filename)

                if file_exists:
                    overwrite = input("File already exists. Do you want to overwrite it (Y/N)? ").strip().lower()
                    if overwrite != 'y':
                        continue  # Continue the loop, asking for a new filename
                try:
                    save_scheduled_appointments(appointments, filename)
                    break  # Break the loop once appointments are saved
                except Exception as e:
                    print(f"Error saving appointments: {e}")
                    break  # Break the loop in case of an error

            print("Good Bye!")
            running = False


if __name__ == "__main__":
    main()

 