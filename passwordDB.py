#program to allow user to enter database

database = [['Cindy', '1234'], ['Adam', '5678']]

usr = input('Enter Username: ')
pin = input('Enter pin: ')
if [usr, pin] in database: print('Access Granted')
else: print('Access Denied')
