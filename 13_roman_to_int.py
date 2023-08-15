# turn ramna to int
'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''

'''
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.'''

class Solution(object):
    def romanToInt(self, roman_str):
        # create a dict
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for i in range(len(roman_str)):
            # if [i] is the first one or smaller than previous
            if i == 0 or roman_dict[roman_str[i]] <= roman_dict[roman_str[i-1]]:
                num += roman_dict[roman_str[i]] # just add it
            else:
                # reduce twice to get rid off the extra adding time
                num += roman_dict[roman_str[i]] - 2*roman_dict[roman_str[i-1]]
        return num

solution = Solution()
s = 'III'
print(solution.romanToInt(s))
s = 'LVIII'
print(solution.romanToInt(s))
s = 'MCMXCIV'
print(solution.romanToInt(s))

# Logic
'''
Logic here is to add each element once
Then, if last element [i-1] is smaller then this one [i]
We reduce [i-1] twice
'''