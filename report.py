import datetime

class ParkReport:
    def __init__(self, resident_name, description, date=None):
        self.resident_name = resident_name
        self.description = description
        self.date = date if date else datetime.date.today()

    def __str__(self):
        return f"[{self.date}] Report by {self.resident_name}: {self.description}"
