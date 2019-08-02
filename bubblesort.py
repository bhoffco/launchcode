def bubble_sort(alist):
    # TODO your code here
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0  # Number of swaps made
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                num_swaps = num_swaps + 1
        if num_swaps == 0:
            is_sorted = True
    return alist
