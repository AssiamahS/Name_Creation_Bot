import random

def generate_name():
    syllables = ["Al", "Be", "Ca", "De", "El", "Fi", "Go", "Ha", "Io", "Ja", "Ki", "Lo", "Ma", "Ni", "Op", "Pa", "Qi", "Ro", "Sa", "Ti", "Ul", "Vi", "Wo", "Xi", "Ya", "Zo"]
    name = random.choice(syllables) + random.choice(syllables).lower()
    return name

def generate_names(count):
    names = set()
    while len(names) < count:
        names.add(generate_name())
    return list(names)

# Generate 30 names
assistant_names = generate_names(30)
for name in assistant_names:
    print(name)
