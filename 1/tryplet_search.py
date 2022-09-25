arr  = [int(i) for i in input("Enter the list values separated by a space: ").split()]
a, b, c = [int(i) for i in input("Enter a, b, c values separated by a space: ").split()]
cntr = 0

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                cntr += 1

print(cntr)