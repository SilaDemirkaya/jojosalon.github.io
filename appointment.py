from datetime import datetime, timedelta
 
class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour
 
    def get_appt_type_desc(self):
        appt_types = {
            0: "Available",
            1: "Mens Cut $50",
            2: "Ladies Cut $80",
            3: "Mens Colouring $50",
            4: "Ladies Colouring $120"
        }
        return appt_types.get(self.appt_type, "Invalid Appointment Type")
 
    def get_end_time_hour(self):
        return self.start_time_hour + 1
 
    def schedule(self, client_name, client_phone, appt_type):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type
 
    def cancel(self):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0
 
    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour}"
 
    def __str__(self):
        start_time = datetime.strptime(f"{self.start_time_hour}:00", "%H:%M").strftime("%I:%M %p")
        end_time = (datetime.strptime(f"{self.start_time_hour}:00", "%H:%M") + timedelta(hours=1)).strftime("%I:%M %p")
        return f"{self.client_name.ljust(20)} {self.client_phone.ljust(15)} {self.day_of_week.ljust(9)} {start_time} - {end_time} {self.get_appt_type_desc()}"