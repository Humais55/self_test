def bubblesort(lst):
    n = len(lst)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

n = int(input("Enter number of elements: "))
LIST = []
for i in range(n):
    x = int(input("Enter elements: "))
    LIST.append(x)

print("Before sorting = ", LIST)

sort = bubblesort(LIST)

print("After sorting = ", sort)
