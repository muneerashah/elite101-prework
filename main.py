welcome = print("Welcome to the Instrument Info Inventory!!")
name = input('What is your name?  ')

print(' ')

birth_year = input(f'And {name}, what year were you born? ')


instruments = ['Flute','Saxophone','Trumpet','Trombone','Tuba','More Coming Soon!','EXIT',' ','Choices are case-sensitive!']

print(' ')
print(f"Alright, {name}, let's get started!")
print(' ')

inventory = 'Instrument Information Inventory:'

print(' ')
print(inventory)
print(' ')

for choice_list in instruments:
        print(choice_list)

print(' ')

print('Type "EXIT" if you wish to end this session!')

print(' ')

inst_choice = (f'{name}, what instrument would you like to learn about? ')
choice = input('Your Choice: ')
print(' ')

if choice == 'Flute':
    print('The Flute!')
    print(' ')
    print('The flute is a silver tube with about 8 keys!') 
    print('It is a soprano of the band and has one of the widest ranges from C4 to C7!')
    print('The flute is a very technical instrument despite being known for its pretty pitch')
    print(' ')

elif choice == 'Saxophone':
    print('The Saxophone!')
    print('')
    print('The saxophone is a woodwind instrument that uses a wood reed')
    print('Saxophones are mostly known for their jazz music and sweet sounds')
    print('The most known saxophone player is Kenny G')
    print('')
 
elif choice == 'Trumpet':
    print('The Trumpet!')
    print('')
    print('The trumpet is a member of the brass family, it is specifically a high brass instrument')
    print('The trumpet has three valves and a range of F#3 to E6! This crosses nearly 3 octaves!')
    print('Trumpets are known to be in popular jazz, marching, and various other genres')
    print('')

elif choice == 'Trombone':
    print('The Trombone!')
    print('')
    print('The trombone is a member of the brass family! It consists of a mouth piece, bell, and slide.')
    print('The slide of a trombone has 7 positions, these positions help change the pitch of notes!')
    print('Trombones are one of the most versatile instruments!')
    print('')

elif choice == 'Tuba':
    print('The Tuba!')
    print('')
    print('The tuba is the bass voice of the band, it handles keeping the background music in time')
    print('It is the biggest instrument and has 9 to 18 feet worth of brass piping')
    print('Tubas are one of the most underrated instruments, when played with expertise, it can be interesting !')
    print('')

elif choice == 'More Coming Soon!':
    print('Theres nothing here!')
    
elif choice == 'EXIT':
    print(f'Thank you for visiting the Inventory Info Inventory, {name}!! ')
    print(' ')

else:
    print('Invalid choice. Please start over')
    print(' ')
    
goodbye = input('Please type in "EXIT" to exit and start over to choose a new instrument!  ')

if goodbye == 'EXIT':
    print(' ')
    print(f'Thank you for visiting the Inventory Info Inventory, {name}!! ')
    print(' ')
    
elif goodbye == 'Exit':
    print(' ')
    print(f'Thank you for visiting the Inventory Info Inventory, {name}!! ')
    print(' ')
    
elif goodbye == 'exit':
    print(' ')
    print(f'Thank you for visiting the Inventory Info Inventory, {name}!! ')
    print(' ')
