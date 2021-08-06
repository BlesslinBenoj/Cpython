def greet_users(names):
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)

usernames = ['beno','jerry','abino']
greet_users(usernames)