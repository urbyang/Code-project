from program import ParkCleanlinessProgram
from utils import parse_dates

def main():
    import datetime
    program = ParkCleanlinessProgram()

    while True:
        print("\nWelcome to Local Park Cleanliness Program")
        print("1. Submit cleanliness report")
        print("2. Volunteer for cleaning")
        print("3. View all reports")
        print("4. View all volunteers")
        print("5. View summary")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            name = input("Enter your name: ").strip()
            description = input("Describe the issue: ").strip()
            program.submit_report(name, description)

        elif choice == '2':
            name = input("Enter your name: ").strip()
            contact = input("Enter your contact info (phone/email): ").strip()
            available_dates = input("Enter available dates (YYYY-MM-DD) separated by commas, or leave blank: ").strip()
            dates_list = parse_dates(available_dates)
            program.add_volunteer(name, contact, dates_list)

        elif choice == '3':
            program.list_reports()

        elif choice == '4':
            program.list_volunteers()

        elif choice == '5':
            program.summary()

        elif choice == '6':
            print("Thank you for supporting local park cleanliness! Goodbye.")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
