def human(x):
    return x in ['Socrates', 'Plato', 'Aristotle']

def mortal(x):
    return human(x)

def is_mortal(x):
    if human(x):
        return True
    return False

person = 'Socrates'
print(f"{person} is mortal: {is_mortal(person)}")
