import string 

def print_rangoli(n):
    # your code goes here
    
    letters = string.ascii_lowercase[0:n]
    
    x = [(('-'.join(letters[i:n])[::-1] + '-'.join(letters[i:n])[1:])).center(n*4-3, '-') for i in range(n)]
    
    print('\n'.join(x[::-1]+x[1:]))
