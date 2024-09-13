'''
Given a string, print all the different substrings that can be generated
'''

def printSubStrings(s):
 
    # To store distinct output subStrings
    us = set();
 
    # Traverse through the given String and
    # one by one generate subStrings beginning
    # from s[i].
    for i in range(len(s)):
 
        # One by one generate subStrings ending
        # with s[j]
        ss = "";
        for j in range(i, len(s)):
            ss = ss + s[j];
            us.add(ss);
         
    # Print all subStrings one by one
    for str in us:
        print(str, end=" ");


# Driver code
if __name__ == '__main__':
    str = "aaabc";
    printSubStrings(str);
