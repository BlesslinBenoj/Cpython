def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

hacker = get_formatted_name('logic','tenacity')
print(hacker)


def get_formatted_name(first_name,middle_name,last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

hacker = get_formatted_name('logic','aka','tenacity')
print(hacker)

def get_formatted_name(first_name,last_name,middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()
hacker = get_formatted_name('logic','tenacity')
print(hacker)

hacker = get_formatted_name('logic','aka','tenacity')
print(hacker)
























