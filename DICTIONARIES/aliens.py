#1


alien_0 = {'color':'blue','points':15}
alien_1 = {'color':'red','points':10}
alien_2 = {'color':'green','points':5}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#2

# make an empty list for storing aliens
aliens = []

#make 30 blue aliens
for alien_number in range(30):
    new_alien = {'color':'blue','points':5,'speed':'slow'}
    aliens.append(new_alien)

#show the first 5 aliens

for alien in aliens[:5]:
    print(alien)

# show how many aliens have been created

print(f"Total number of aliens:{len(aliens)}")



#3

# make an empty list for storing aliens
aliens = []

#make 30 blue aliens
for alien_number in range(30):
    new_alien = {'color':'blue','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'blue':
        alien['color'] = 'green'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

































































