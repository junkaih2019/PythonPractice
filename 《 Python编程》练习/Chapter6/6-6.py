favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

investigate_name = ('jen', 'phil')
for name in favorite_languages.keys():
    if name in investigate_name:
        print("Thank you, " + name.title() + "!")
    else:
        print(name.title() + ", Would you like to take a poll?")
