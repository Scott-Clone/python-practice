
def reverse_list(string):

    def reverse(l, r):

        if l < r: 
            string[l], string[r] = string[r], string[l]
            reverse(l + 1, r - 1)
    reverse(0, len(string) -1)


print(reverse_list(list('hello')))



