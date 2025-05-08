import datetime

def parse_dates(input_str):
    dates = []
    if input_str:
        for d in input_str.split(','):
            try:
                date_obj = datetime.datetime.strptime(d.strip(), "%Y-%m-%d").date()
                dates.append(date_obj)
            except ValueError:
                print(f"Invalid date format ignored: {d.strip()}")
    return dates
