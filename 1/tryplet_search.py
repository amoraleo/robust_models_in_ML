arr  = [3,0,1,1,9,7] #[1,1,2,2,3]
cntr = 0
a, b, c = 7, 2, 3 #0, 0, 1
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                cntr += 1
print(cntr)