
from datetime import datetime


def main():
    try_again = True
    while try_again == True:
        date_string = input("Please enter a date in the format 'mm/dd/yy': ")
        date_list = date_string.split('/')

        month = date_list[0]
        day = date_list[1]
        year = date_list[2]

        if month > "12" or month < "01":
            print('Error, please re-enter the date!')

        if year != '13':
            print('Error! The year must be 2013')

        if len(year) > 2:
            print('Error! The year can only be 2 digits long!')

        else:
            print_date(month, day, year)
            try_again = False



def print_date(month, day, year):

# Convert to 2013 because 2013 is the only valid year
# for this program.


# Convert the number values to the actual month.

if month == '01':
    month = 'January'
if month == '02':
    month = 'February'
if month == '03':
    month = 'March'
if month == '04':
    month = 'April'
if month =='05':
    month = 'May'
if month == '06':
    month = 'June'
if month == '07':
    month = 'July'
if month == '08':
    month = 'August'
if month == '09':
    month = 'September'
if month =='10':
    month = 'October'
if month == '11':
    month = 'November'
if month == '12':
    month = 'December'


# Print the date in the correct format
print(month + " " + day + ',' + " " + year)


main()