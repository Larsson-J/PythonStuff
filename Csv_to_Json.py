import csv
import json

# directory for csv file
csvfile = open('C:\Users\Username\Projects\data.csv', 'r')

# directory for json file
jsonfile = open('C:\Users\Username\Projects\master.json', 'w')

# choosing the fieldnames (for this example suicide rates)
fieldnames = ("country", "year", "sex", "age", "suicides_no", "population", "suicides/100k pop",
              "country-year", "HDI for year", "gdp_for_year($)", "gdp_per_capita($)", "generation")

# completing the process
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')