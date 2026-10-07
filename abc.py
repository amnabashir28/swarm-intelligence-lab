import random
random.seed(59)   

def f(x):
    return (x - 7) ** 2 + 4  

def fitness(x):
    return 1 / (1 + f(x))      

# Initial food sources
sources = [random.uniform(0, 14) for _ in range(5)]

# Number of trials since a source last improved
trials = [0 for _ in range(5)]

# Abandon a source after this many failed trials
limit = 8

iterations = 40

for it in range(iterations):

    # Employed bee phase
    for i in range(5):

        k = random.choice([j for j in range(5) if j != i])

        # Create a new candidate solution
        phi = random.uniform(-1, 1)
        candidate = sources[i] + phi * (sources[i] - sources[k])

        # Keep candidate within the search range
        candidate = max(0, min(14, candidate))

        if fitness(candidate) > fitness(sources[i]):
            sources[i], trials[i] = candidate, 0
        else:
            trials[i] += 1

    # Scout bee phase
    for i in range(5):

        if trials[i] > limit:
            sources[i] = random.uniform(0, 14)
            trials[i] = 0

# Find the best solution
best_source = min(sources, key=f)

print("Final Sources:")
for source in sources:
    print(round(source, 4))

print("\nBest solution:", round(best_source, 4))
print("Minimum value:", round(f(best_source), 4))