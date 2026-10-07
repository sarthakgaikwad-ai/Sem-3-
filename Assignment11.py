import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

# Indexing
print("\nValue at index 2:", s[2])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())



'''Output
Series:
0    37
1    70
2    27
3    72
4    11
5    21
6    68
7    18
8     3
9    20
dtype: int64

Value at index 2: 27

Numbers greater than 50:
1    70
3    72
6    68
dtype: int64

Mean: 34.7
Median: 24.0
Minimum: 3
Maximum: 72
'''