import csv
from collections import namedtuple
from itertools import islice
import functools
from datetime import date, datetime


PersonalInfo = namedtuple("PersonalInfo", "ssn, first_name, last_name, gender, language")
Employment = namedtuple("Employment", "employer, department, employee_id, ssn")
Vehicles = namedtuple("Vehicles", "ssn, vehicle_make, vehicle_model, model_year")
UpdateStatus = namedtuple("UpdateStatus", "ssn, last_updated, created")
FullDetails = namedtuple("FullDetails", "ssn, first_name, last_name, gender, language, "
                                        "employer, department, employee_id, "
                                        "vehicle_make, vehicle_model, model_year, "
                                        "last_updated, created")
cutoff_date = date(2017, 3, 1) #3/1/2017)

int_columns = {"employee_id", "model_year"}
date_columns = {"last_updated", "created"}


def read_file(filename, tuple_type=None):
    """ This function takes a filename and a namedtuple type, and returns an iterator
    The iterator returns each row as a named tuple as passed in the input """

    with open(filename) as f:
        # Ignore header
        next(f)

        rows = csv.reader(f, delimiter=',', quotechar='"')
        #yield from map(convert_to_tuple, rows, [tuple_type]) # Need to map tuple_type to a list of same length..
        yield from map(functools.partial(convert_to_tuple, tuple_type=tuple_type), rows)


def convert_to_tuple(row, tuple_type):
    """ This function takes a row and a namedtuple type, and returns a named tuple representation for the given data """
    obj = tuple_type(*row)
    return obj


def get_iterators():
    # emp_file, personal_file, vehicle_file, status_file
    """This function creates iterators for each file """
    emp_iter = read_file("employment.csv", Employment)
    personal_iter = read_file("personal_info.csv", PersonalInfo)
    vehicle_iter = read_file("vehicles.csv", Vehicles)
    update_iter = read_file("update_status.csv", UpdateStatus)
    return emp_iter, personal_iter, vehicle_iter, update_iter


def combine_data(emp_data, personal_data, vehicle_data, update_data):
    """ This function creates a combined dataset from four files: employment, personal_info, vehicles, and update_status
    Data from file is converted into an iterator which returns a named tuple. These are then combined to form one data row per ssn
    ** Assumption: Each file is ordered by ssn, and all ssns match. i.e. no missing or extra records
    """
    # emp_data, personal_data, vehicle_data, update_data = get_iterators()

    for emp, personal, vehicle, status in zip(emp_data, personal_data, vehicle_data, update_data):
        if (emp.ssn != personal.ssn) or (emp.ssn != vehicle.ssn) or (emp.ssn != status.ssn):
            print("SSNs don't seem to be in order. Redo")
            raise Exception("SSNs in the files are not in order / missing SSNs")
        else:
            try:
                #2017-10-07T00:14:42Z
                last_updated = datetime.strptime(status.last_updated,'%Y-%m-%dT%H:%M:%SZ')
                created_date = datetime.strptime(status.created, '%Y-%m-%dT%H:%M:%SZ')
                full_details = FullDetails(
                    emp.ssn, personal.first_name, personal.last_name, personal.gender, personal.language,
                    emp.employer, emp.department, emp.employee_id,
                    vehicle.vehicle_make, vehicle.vehicle_model, int(vehicle.model_year),
                    last_updated, created_date)

                yield full_details
            except Exception as ex:
                print("Exception while combining data record: ", ex)
                yield None


def data_cleanup():
    """ This function is called in case the data in all the files is not ordered correctly by ssn,
    and therefore cannot be combined in one combined zip iteration"""
    pass


def filter_date(combined_iter, cutoff_date):
    """This function filters out stale records from the dataset """
    # combined_iter = combine_data()
    filtered_records = filter(lambda x: x.last_updated.date() >= cutoff_date, combined_iter)
    yield from filtered_records


def vehicle_make_by_gender():
    """This function sorts vehicle makes by gender, and returns the top vehicle makes for each gender """
    emp_data, personal_data, vehicle_data, update_data = get_iterators()
    combined_iter = combine_data(emp_data, personal_data, vehicle_data, update_data)
    current_data = filter_date(combined_iter, cutoff_date)

    vehicle_makes = {} # {'Male': {'m1': count1, 'm2': count2}, ...}
    for data in current_data:
        """FullDetails = namedtuple("FullDetails", "ssn, first_name, last_name, gender, language, "
                                        "employer, department, employee_id, "
                                        "vehicle_make, vehicle_model, model_year, "
                                        "last_updated, created")"""
        if data.gender not in vehicle_makes:
            vehicle_makes[data.gender] = {}

        if data.vehicle_make not in vehicle_makes[data.gender]:
            vehicle_makes[data.gender][data.vehicle_make] = 1
        else:
            vehicle_makes[data.gender][data.vehicle_make] += 1

    # Sort the data
    sorted_vehicle_data = {}
    for gender, count_dict in vehicle_makes.items():
        sorted_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
        sorted_vehicle_data[gender] = sorted_dict

    return sorted_vehicle_data



if __name__ == "__main__":

    # Testing employment data
    print("\n --- Employment data check --")
    emp_data = read_file("employment.csv", Employment)
    for emp in islice(emp_data, 3):
        print(emp)

    # Testing personal data
    print("\n --- Personal data check --")
    personal_data = read_file("personal_info.csv", PersonalInfo)
    for person in islice(personal_data, 3):
        print(person)

    # Testing vehicle data
    print("\n --- Vehicle data check --")
    vehicle_data = read_file("vehicles.csv", Vehicles)
    for vehicle in islice(vehicle_data, 3):
        print(vehicle)

    # Testing update data
    print("\n --- Status data check --")
    update_data = read_file("update_status.csv", UpdateStatus)
    for status in islice(update_data, 3):
        print(status)

    print("\n --- Combined data check --")
    full_data = combine_data(emp_data, personal_data, vehicle_data, update_data)
    # for full in islice(full_data, 1000):
    for full in islice(full_data, 3):
        print(full)

    print("\n --- Filtered  Date check --")
    yy = filter_date(full_data, cutoff_date)
    for y in islice(yy, 2):
        print("Filtered date: ", y)

    print("\n --- Vehicle makes per gender check --")
    sorted_vehicle_makes = vehicle_make_by_gender()
    for gender, makes in sorted_vehicle_makes.items():
        print(f"Gender: {gender}, counts={makes}")