from faker import Faker
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from collections import namedtuple
from time import perf_counter


Person = namedtuple("Person", "age location blood_type")

def timed(reps):
	def decorator(fn):
		def inner(*args, **kwargs):
			total_elapsed = 0
			for i in range(reps):
				start = perf_counter()
				result = fn(*args, **kwargs)
				end = perf_counter()
				elapsed = end - start
				total_elapsed += elapsed

			avg_elapsed = total_elapsed / reps
			# print(f'Average time taken in {reps} iterations: {avg_elapsed}')
			return result, avg_elapsed
		return inner
	return decorator


def get_profiles(n, make_tuple=False):
    """
    This function generates n fake profiles containing the age, longitude, latitude and blood type
    It will return a list of either a named tuples or a dictionies, depending on the flag passed
    """
    Faker.seed(0)
    faker = Faker()
    btypes = ('A', 'B', 'O', 'AB')
    profiles = []

    for i in range(n):
        profile = faker.simple_profile()
        location = faker.latlng()

        birthdate = profile['birthdate']
        now = date.today()
        age = relativedelta(now, birthdate).years

        btype_sign = '+' if faker.pybool() else '-'
        btype = faker.random_element(elements=btypes)
        blood_type = btype_sign + btype

        if make_tuple:
           person = Person(age, location, blood_type)
        else:
            person = {'age': age, 'location': location, 'blood_type': blood_type}

        profiles.append(person)

    return profiles

@timed(10)
def get_summary_named_tuples(n, profiles):
    """
    This function calcuates the mean age, oldest age, latitude, longitude and max blood type
    where the input is a  list of named tuples
    """
    age = 0
    lat = 0
    lng = 0
    blood_type_counts = {}
    oldest = 0

    for profile in profiles:
        age += profile.age
        lat += profile.location[0]
        lng += profile.location[1]
        if profile.blood_type in blood_type_counts:
            blood_type_counts[profile.blood_type] = blood_type_counts[profile.blood_type] + 1
        else:
            blood_type_counts[profile.blood_type] = 1
        oldest = oldest if oldest >= profile.age else profile.age

    mean_age, lat, lng, max_bt = calculate(n, age, lat, lng, blood_type_counts)

    return mean_age, oldest, lat, lng, max_bt


@timed(10)
def get_summary_dict(n, profiles):
    """
        This function calcuates the mean age, oldest age, latitude, longitude and max blood type
        where the input is a list of dictionaries
    """
    age = 0
    lat = 0
    lng = 0
    blood_type_counts = {}
    oldest = 0

    for profile in profiles:
        age += profile['age']
        lat += profile['location'][0]
        lng += profile['location'][1]
        if profile['blood_type'] in blood_type_counts:
            blood_type_counts[profile['blood_type']] = blood_type_counts[profile['blood_type']] + 1
        else:
            blood_type_counts[profile['blood_type']] = 1
        oldest = oldest if oldest >= profile['age'] else profile['age']

    mean_age, lat, lng, max_bt = calculate(n, age, lat, lng, blood_type_counts)

    return mean_age, oldest, lat, lng, max_bt


def calculate(n, age, lat, lng, blood_type_counts):
    mean_age = age / n
    lat = lat / n
    lng = lng / n
    # max_bt_count = max(blood_type_counts.values())
    max_bt = max(blood_type_counts, key=blood_type_counts.get)
    # print(max_bt_count, blood_type_counts)
    return mean_age, lat, lng, max_bt


def profiles_summary_named_tuples(n=10000, debug=True):
    """
    This function takes n randomly generated profiles, and uses namedtuples to calculate
    the largest blood type, mean-current_location, oldest_person_age, and average age
    """
    profiles = get_profiles(n, make_tuple=True)
    result = get_summary_named_tuples(n, profiles)
    mean_age, oldest, lat, lng, max_bt = result[0]
    time_elapsed = result[1]

    if debug:
        print("\n ==== Profiles with Named Tuples function: === ")
        print("Mean age: ", mean_age)
        print("Oldest age: ", oldest)
        print(f'Latitude/Longitude: ({lat}, {lng}), ')
        # print("Blood type counts: ", blood_type_counts)
        print("Max blood type: ", max_bt)
        print("Time taken for named tuples: ", time_elapsed)

    return mean_age, oldest, lat, lng, max_bt, time_elapsed


def profiles_summary_dict(n=10000, debug=True):
    """
    This function takes n randomly generated profiles, and uses namedtuples to calculate
    the largest blood type, mean-current_location, oldest_person_age, and average age
    """
    profiles = get_profiles(n, make_tuple=False)
    result = get_summary_dict(n, profiles)
    mean_age, oldest, lat, lng, max_bt = result[0]
    time_elapsed = result[1]

    if debug:
        print("\n ==== Profiles with Dictionaries function: === ")
        print("Mean age: ", mean_age)
        print( "Oldest age: ", oldest)
        print(f'Latitude/Longitude: ({lat}, {lng}), ')
        # print("Blood type counts: ", blood_type_counts)
        print("Max blood type: ", max_bt)
        print("Time taken for dict: ", time_elapsed)

    return mean_age, oldest, lat, lng, max_bt, time_elapsed


def stock_market(n):
    """
    Create fake data (you can use Faker for company names) for imaginary stock exchange for
    top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies.
    Calculate and show what value the stock market started at, what was the highest value during the day,
    and where did it end. Make sure your open, high, close are not totally random.
    You can only use namedtuple. - 500  (including 10 test cases)

    """

    pass


