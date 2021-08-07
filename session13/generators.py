from collections import namedtuple
from datetime import datetime
from itertools import islice
from typing import NamedTuple

# Create a namedtuple that can hold parking ticket info
ParkingTicket = namedtuple("ParkingTicket",
                          "summons_number, plate_id, registration_state, plate_type, issue_date,"
                          "violation_code, vehicle_body_type, vehicle_make, violation_description")

def get_named_tuple(row):
    """ This function creates a named tuple from the input data row
    If the column is a date, it is converted to a date type before storing in the tuple
    If the column is an integer, it is stored as an int in the tuple
    """
    try:
        cols = row.strip("\n").split(",")
        summons_number = int(cols[0]) # num
        plate_id = cols[1]
        registration_state = cols[2]
        plate_type = cols[3]
        issue_date = datetime.strptime(cols[4], '%m/%d/%Y').date()
        violation_code = int(cols[5]) # num
        vehicle_body_type = cols[6]
        vehicle_make = cols[7]
        violation_description = cols[8]
        return ParkingTicket(summons_number, plate_id, registration_state, plate_type, issue_date,
                             violation_code, vehicle_body_type, vehicle_make, violation_description)

    except Exception as ex:
        print("Exception while extracting to named tuple: ", ex)
        return None

def get_ticket_data(filename):
    """ This function creates a lazy iterator that will return a named tuple of the data in each row of input file. """
    with open(filename, 'r') as f:
        # Ignore header
        next(f)

        for line in f:
            yield get_named_tuple(line)


def violations_by_make(filename):
    """ This function calculate the number of violations by car make. """
    violations = {}
    data = get_ticket_data(filename)
    for row in data:
        if not row:
            continue

        if row.vehicle_make in violations:
            violations[row.vehicle_make] += 1
        else:
            violations[row.vehicle_make] = 1

    sorted_violations = dict(sorted(violations.items(), key=lambda x: x[1], reverse=True))

    return sorted_violations

if __name__ == "__main__":
    filename = "nyc_parking_tickets_extract-1.csv"
    data = get_ticket_data(filename)
    for row in islice(data, 0, 5):
        print("Row is: ", row)

    violations = violations_by_make(filename)
    print(violations)