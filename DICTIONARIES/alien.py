#1

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#2
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#3
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#4
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#5
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


#6

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"original_position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"new position: {alien_0['x_position']}")

#7

alien_0 = {'color':'blue','points':3}
print(alien_0)
del alien_0['points']
print(alien_0)





















