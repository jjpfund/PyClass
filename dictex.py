#welcome to the thunderdome

sentence = ('All your base are belong to us')

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) //2

print
print(' ' * left_margin + '+'    + '-' * (box_width-2) +' +')
print(' ' * left_margin + '|   ' + '-' * text_width   +'  |')
print(' ' * left_margin + '-   ' + '+' * text_width   +'  -')
print(' ' * left_margin + '|   ' +       sentence     +'  |')
print(' ' * left_margin + '-   ' + '+' * text_width   +'  -')
print(' ' * left_margin + '|   ' + '-' * text_width   +'  |')
print(' ' * left_margin + '+'    + '-' * (box_width-2) +' +')
print


print('Connecting... \n')

#A simple phonebook database

#access granted?
Database = [
    ['cnayak', '8224'], ['cnash', '2960']
    ]
usrnm = input('\nUsername: ')

import getpass
pin = getpass.getpass('Password:') #used getpass instead of input to avoid echo

if[usrnm, pin] in Database:
    print('\n...Connected\n\nAccess Granted...')
    if usrnm.endswitch('cnayak'):
        print('\nWelcome Adam Smith\n')
    else:
        print('\nWelcome Chris Nash')

    people = {
        'Adam Smith': {
            'phone':'1234',
            'addr':'21 top hill'
        },
        'Beth': {
            'phone':'4567',
            'addr':'22 baskerville' 
        },
        'Sherlock': {
            'phone':'7890',
            'addr':'22nd st london'
        },
    }
    else:
        print('Access Denied')

'''
descriptive labels for phone and addr used for printing output

    labels = {
        'phone':'phone number',
        'addr':'address'
    }

    name = input('Name: ')

    request = input('phone number (p) or address (a)? ')

#use correct key
    if request == 'p' : key = 'phone'
    if request == 'a' : key = 'addr'

#only print if name is valid key
    if name in people: print ("%s's %s is %s" % (name, labels[key], people[name]*\[key]))
'''
