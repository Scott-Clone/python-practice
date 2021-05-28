def points_cover_sort(arr):
    ''' arr is a list containing elemnets to be sorted
    with maximum 1 unit length between and two pairs of 
    elements from a given group '''

    cover_list = []
    i = 0
    n = len(arr) - 1
    while i < n:
        [l, r] = [arr[i], (arr[i] + 1)]

        cover_list.append([l,r]) 
        print(i)
        print(cover_list)
        i += 1

        while i <= n and arr[i] <= r: 
            print(i)
            i += 1

    return cover_list

print(points_cover_sort([5, 5.5, 5.8, 6, 7, 8, 9]))