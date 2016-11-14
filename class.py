#test program to print out date
months=['january','febuary','march','april','may','june','july','august','september','october','november','december']

#list with 1 ending

endings=['st','nd','rd'] + 17 *['th'] + ['st','nd','rd'] + 17 *['th'] + ['st']

year = input("Enter current year: ")
month = input('Enter current month: ')
day = input('Enter current day: ')

month_number = int(month)
day_number = int(day)

#subtract 1 from input to get correct index
month_name = months[month_number-1]
original = day + endings[day_number-1]

print(month_name + " " + original + ", " + year)

#This is the end
