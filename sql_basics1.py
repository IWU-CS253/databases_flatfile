# note! the requests package should be installed in pycharm before you begin

from helpers import mimic_lecture_7, print_heading_descriptions, heading_dic
import csv, os

# ignore this, don't edit
if not os.path.isfile('survey.csv'):
    mimic_lecture_7()

# set True if you want to review the file heading descriptions
if False:
    print_heading_descriptions(heading_dic)

# this code mirrors CS50x 2024 lecture 7 code starting at 11:30
with open("survey.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    x, y, z = 0, 0, 0
    for row in reader:
        favorite = row["language"]

# test test test





