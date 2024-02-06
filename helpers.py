
from typing import List, Optional
import requests
import csv
from io import StringIO

def get_survey_data(url: str) -> Optional[List[List[str]]]:
    """
    Fetches survey data from a given URL pointing to a CSV file and returns
    the rows in the CSV file as a list of lists of strings.

    Parameters:
    - url (str): The URL of the CSV file to fetch data from.

    Returns:
    - A list of lists of strings, where each inner list represents a row in the CSV file.
      Returns None if the request fails.

    Raises:
    - Prints an error message if the HTTP request failed.
    """
    response = requests.get(url)
    if response.status_code == 200:
        # Use StringIO to turn the text data into a file-like object
        data = StringIO(response.text)
        # Read the CSV data into a list of lists
        csv_data = list(csv.reader(data))
        return csv_data
    else:
        print(f"Failed to fetch data: status code {response.status_code}")
        return None


def create_csv(data, filename):
    """
    Writes the given data to a CSV file with UTF-8 encoding.

    This function takes a list of lists, where each inner list represents a row in the CSV,
    and writes it to a file specified by the filename parameter. The file is created or
    overwritten if it already exists. Each row in the data list is written as a row in the CSV file.

    Parameters:
    - data (List[List[str]]): A list of rows, with each row being a list of values representing a row in the CSV.
    - filename (str): The path to the file where the CSV data should be written. If the file exists, it will be overwritten.

    Returns:
    - None: The function writes to a file and does not return any value.

    Side effects:
    - Creates a new file or overwrites an existing file at the specified filename.
    - Writes the contents of `data` to the file in CSV format with UTF-8 encoding.
    """
    file_path = filename
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def print_heading_descriptions(heading_dic):
    for key, value in heading_dic.items():
        print(value + ":" + '\n\t' + key + '\n' )

heading_dic = {
    'Timestamp':'timestamp',
    'Who is your favorite music artist (broadly defined)?':'artist',
    'What physical height would you like to be?':'height',
    'If you had to live in the city, but could pick any city in the world, what city would you live in?':'city',
    'If you could have 30 minutes to talk with any person, living or dead, who would you pick?':'talk',
    'If you could travel to any location in the world for vacation, where would you go?':'vacation',
    'On a scale of 1 (gross) to five (awesome) how much do you like pizza?':'pizza',
    'Is Chicago-style deep dish actually pizza or is it really casserole?':'casserole',
    'What sport do you most enjoy watching?':'sport',
    'Which is the most difficult to spell?':'spell',
    'What is the optimal number of people to hang out with?':'hangout',
    'Do you think you talk more or less than the average person?':'talk',
    'If you had a time machine and could visit any year you like, which year would you pick?':'year',
    "What's you favorite inspirational quote? You don't need to do this from memory. Feel free to look something up and then paste it in here.":'quote',
    'What is the area code of your phone number?':'areacode',
    'What pet(s) did you have as a child?':'pets',
    'If you had to have one superpower, what would if be?':'superpower',
    'How many different pairs of shoes have you worn in the last week?': 'shoes'
}

def mimic_lecture_7():
    # specify the url of the csv
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRkK73xD192AdP0jZe6ac9cnVPSeqqbYZmSPnhY2hnY8ANROAOCStRFdvjwFoapv3j2rzMtZ91KXPFm/pub?gid=1559170894&single=true&output=csv"

    # get the data as a list of lists
    survey_data = get_survey_data(url)

    # reduce the header to something more manageable
    survey_data[0] = [heading_dic.get(x, x) for x in survey_data[0]]

    # create a csv to parallel the lecture
    create_csv(survey_data, 'survey.csv')
