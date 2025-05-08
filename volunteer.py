class Volunteer:
    def __init__(self, resident_name, contact, available_dates=None):
        self.resident_name = resident_name
        self.contact = contact
        self.available_dates = available_dates if available_dates else []

    def add_availability(self, date):
        if date not in self.available_dates:
            self.available_dates.append(date)

    def __str__(self):
        dates = ', '.join(str(d) for d in self.available_dates) if self.available_dates else 'No availability set'
        return f"Volunteer: {self.resident_name}, Contact: {self.contact}, Available dates: {dates}"
