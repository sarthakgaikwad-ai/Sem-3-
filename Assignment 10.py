import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

# Indexing
print("\nFirst element:")
print(s[0])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

#output
# Series:
# 0    45
# 1    72
# 2    18
# 3    91
# 4    34
# 5    63
# 6    27
# 7    88
# 8    51
# 9    12
# dtype: int64

# First element:
# 45

# Numbers greater than 50:
# 1    72
# 3    91
# 5    63
# 7    88
# 8    51
# dtype: int64

# Mean: 50.1
# Median: 48.0
# Minimum: 12
# Maximum: 91
