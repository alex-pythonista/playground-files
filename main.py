age = 26
name = "I am Reza"
pi = 3.1416
isMarried = False

# list
lst = [1, 2, "alex", 1.78]
lst.insert(2, 10)
print(type(lst))

# tuple
tpl = (1, 2, "alex", 1.78)

# set
st = {1, 2, "alex", 3.19}

# disctionaries

# object, JSON
aboutMe = {
    'name': 'reza',
    'age': 26,
    'isMarried': False,
    'favoriteNumbers': [1, 3, 5, 7],
    'familyMembers': {
        'father': 'A',
        'mum': 'B',
        'siblings': {
            's1': 'X',
            's2': 'Y'
        }
    }
}
print(type(aboutMe))