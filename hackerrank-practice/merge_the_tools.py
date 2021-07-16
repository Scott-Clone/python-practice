def merge_the_tools(string, k):
    x = [list(dict.fromkeys(string[i:i+k])) for i in range(0, len(string), k)]
    
    for i in x:

        print(''.join(i))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
