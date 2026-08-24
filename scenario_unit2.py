#Q5 
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    max_length = 0  
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
            else:
                dp[i][j] = 0  
    
    return max_length

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = longest_common_substring(string1, string2)
print("Length of the longest common substring:", result)

