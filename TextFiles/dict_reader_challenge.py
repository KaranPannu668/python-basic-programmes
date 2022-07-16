import csv
from fileinput import filename

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    
    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ').casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break