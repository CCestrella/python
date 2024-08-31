import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_string = datetime.fromisoformat(iso_string)
    formatted_date = date_string.strftime('%A %d %B %Y')
    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    temp_in_fahrenheit = float(temp_in_fahrenheit)

    celsius = (temp_in_fahrenheit - 32)*5/9
    celsius = round(celsius,1)

    return celsius



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data =[float(num) for num in weather_data]
    
    if not weather_data:
        return 0 
    
    mean_value = sum(weather_data)/len(weather_data)
    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:
                # Convert elements to the correct types, if necessary
                date = row[0]
                min_temp = int(row[1])
                max_temp = int(row[2])
                data.append([date, min_temp, max_temp])
        return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers (strings or floats).
    Returns:
        The minimum value and its position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()   

    
    weather_data = [float(num) for num in weather_data]
    
    min_value = min(weather_data)
    min_index = len(weather_data) - 1 - weather_data[::-1].index(min_value)  # Find the last occurrence

    return min_value, min_index
    

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()  
    
    
    weather_data = [float(num) for num in weather_data]
    
    max_value = max(weather_data)
    max_index = len(weather_data) - 1 - weather_data[::-1].index(max_value)  # Find the last occurrence

    return max_value, max_index

def generate_summary(weather_data):
    
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No data available."

    # Extract the minimum and maximum temperatures for all days
    min_temps = [day[1] for day in weather_data]
    max_temps = [day[2] for day in weather_data]

    # Find the minimum and maximum temperatures and their corresponding dates
    min_temp, min_temp_day = find_min(min_temps)
    max_temp, max_temp_day = find_max(max_temps)

    # Convert the dates and temperatures to the required formats
    min_temp_date = convert_date(weather_data[min_temp_day][0])
    max_temp_date = convert_date(weather_data[max_temp_day][0])
    min_temp_c = format_temperature(convert_f_to_c(min_temp))
    max_temp_c = format_temperature(convert_f_to_c(max_temp))

    # Calculate the average of the minimum and maximum temperatures
    avg_min_temp = format_temperature(round(convert_f_to_c(calculate_mean(min_temps)), 1))
    avg_max_temp = format_temperature(round(convert_f_to_c(calculate_mean(max_temps)), 1))

    # Construct the summary string
    summary = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {min_temp_c}, and will occur on {min_temp_date}.\n"
        f"  The highest temperature will be {max_temp_c}, and will occur on {max_temp_date}.\n"
        f"  The average low this week is {avg_min_temp}.\n"
        f"  The average high this week is {avg_max_temp}.\n"
    )

    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for day in weather_data:
        date = convert_date(day[0]) 
        min_temp_c = convert_f_to_c(day[1])  
        max_temp_c = convert_f_to_c(day[2])  


        min_temp_str = format_temperature(min_temp_c)
        max_temp_str = format_temperature(max_temp_c)

       
        summary += f"---- {date} ----\n"
        summary += f"  Minimum Temperature: {min_temp_str}\n"
        summary += f"  Maximum Temperature: {max_temp_str}\n\n"

    return summary