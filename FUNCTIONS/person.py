def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person

hacker = build_person('logic','tenacity')
print(hacker)

def build_person(first_name,last_name,age = None):
    person = {'first':first_name,'last':last_name}

    if age:
        person['age'] = age
    return person

hacker = build_person('logic','tenacity',age=19)
print(hacker)