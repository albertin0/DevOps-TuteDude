import random

subjects = ["The cat", "A developer", "An astronaut", "The teacher", "My friend"]
verbs = ["eats", "builds", "writes", "discovers", "teaches"]
objects = ["a burger", "code", "a novel", "a planet", "students"]
adverbs = ["quickly", "carefully", "silently", "eagerly", "gracefully"]

# Generate meaningful-looking random sentences
def generate_sentence():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(adverbs)}."

# Write sentences to file
filename = 'meaningful_random_text.txt'
with open(filename, 'w') as file:
    for _ in range(10):
        file.write(generate_sentence() + '\n')

print(f"Random meaningful sentences written to '{filename}'")
