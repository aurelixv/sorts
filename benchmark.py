import random
import time
import pandas as pd
from merge_sort import merge_sort
from insertion_sort import insertion_sort

def randomVector(i):
    vector = []
    for x in range(i):
        vector.append(random.randint(1, 1000000))

    return vector

# Creates a new empty dataframe
benchmark = pd.DataFrame()

# Benchmark the algorithms n times, with the vector size increasing 10**n
for x in range(1, 21):
    size = 100*x

    print('Creating vector with ' + str(size) + ' random numbers...')
    A = randomVector(size)

    print('Merge Sorting the vector...')
    start = time.process_time()
    merge_sort(A)
    end = time.process_time()
    elapsed = end - start
    print('Done in ' + str(elapsed) + ' seconds.')

    benchmark = benchmark.append({'Vector Size' : int(size), 'Time' : elapsed, 'Algorithm' : 'Merge Sort'}, ignore_index=True)

    print('Insert Sorting the vector...')
    start = time.process_time()
    insertion_sort(A)
    end = time.process_time()
    elapsed = end - start   
    print('Done in ' + str(elapsed) + ' seconds.')

    benchmark = benchmark.append({'Vector Size' : int(size), 'Time' : elapsed, 'Algorithm' : 'Insertion Sort'}, ignore_index=True)

print(benchmark)

benchmark.to_csv('benchmark.csv')
