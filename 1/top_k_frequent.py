nums  = [int(i) for i in input("Enter the list values separated by a space: ").split()]
k = int(input("Enter k value: "))

num_dict = {}

for num in nums:
    num_dict[num] = 1 + num_dict.get(num, 0)

freq_dict = {}

for num, freq in num_dict.items():
    if freq not in freq_dict:
        freq_dict[freq] = [num]
    else:
        freq_dict[freq].append(num)

result = []

for i in range(len(nums), 0, -1):
    if i in freq_dict:
        if len(freq_dict[i]) + len(result) >= k:
            result += freq_dict[i][:k-len(result)]
            break
        result += freq_dict[i]

print(result)