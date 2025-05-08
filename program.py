from report import ParkReport
from volunteer import Volunteer

class ParkCleanlinessProgram:
    def __init__(self):
        self.reports = []
        self.volunteers = []

    def submit_report(self, resident_name, description):
        report = ParkReport(resident_name, description)
        self.reports.append(report)
        print(f"Thank you, {resident_name}, for reporting the issue.")

    def add_volunteer(self, resident_name, contact, available_dates=None):
        volunteer = Volunteer(resident_name, contact, available_dates)
        self.volunteers.append(volunteer)
        print(f"Thank you, {resident_name}, for volunteering!")

    def list_reports(self):
        if not self.reports:
            print("No cleanliness reports yet.")
        else:
            print("Current cleanliness reports:")
            for report in self.reports:
                print(" - " + str(report))

    def list_volunteers(self):
        if not self.volunteers:
            print("No volunteers registered yet.")
        else:
            print("Registered volunteers:")
            for volunteer in self.volunteers:
                print(" - " + str(volunteer))

    def summary(self):
        print("=== Park Cleanliness Program Summary ===")
        print(f"Total reports: {len(self.reports)}")
        print(f"Total volunteers: {len(self.volunteers)}")
        print("---------------------------------------")