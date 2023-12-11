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