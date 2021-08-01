#1

favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}

language = favourite_languages['beno'].title()
print(f"Beno 's Favourite language is {language}.")

#2

favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}

for name,language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

#3

favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}

for name in favourite_languages.keys():
    print(name.title())

#4

favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}

friends = ['beno','jerry']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")

#5
favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}
if 'erin' not in favourite_languages.keys():
    print("Erin.please take our poll!")

#6

favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


#7

favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby'}
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

#8
favourite_languages = {'beno':'javascript',
                       'jerry':'python',
                       'abino':'ruby',
                       'mastermind':'python'}
print("the following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

#9

languages = {'python','ruby','javascript','python'}
print(languages)

#10

favourite_languages = {
    'beno': ['python','javascript'],
    'jerry':['python','c'],
    'abino':['python','c++'],
}
for name,languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
    
































