s = "hashtable"
arr = [0] * 26

for i in range(len(s)):
	arr[ord(s[i]) - ord('a')] += 1

ch = 'e'

print("The count of", ch, "is", arr[ord(ch) - ord('a')])
print(arr)