def main():
    appointments = create_weekly_calendar()
    load_scheduled_appointments(appointments)

    running = True
    while running:
        choice = print_menu()

        if choice == '1':
            print('* Schedule an appointment *')
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
            print('* Find appointment by name *')
            client_name = input("Enter Client Name: ")
            print("Client Name         Phone          Day       Start     End       Type")
            print("-------------------------------------------------------------------------------------")
            show_appointments_by_name(appointments, client_name)

        elif choice == '3':
            print('* Print calendar for a specific day *')
            day_of_week = input("Enter the day of the week: ")
            print(f"Appointments for {day_of_week}")
            print("Client Name         Phone          Day       Start     End       Type")
            print("-------------------------------------------------------------------------------------")
            show_appointments_by_day(appointments, day_of_week)

        elif choice == '4':  # Cancel an Appointment
            print('* Cancel an appointment *')
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
            print('* Exit the system *')
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


if _name_ == "_main_":
    main()