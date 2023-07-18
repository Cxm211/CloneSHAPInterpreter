def backtrack(res, temp, nums, start) :
	res.append(temp [:])
	for i in range(start, len(nums)) :
		temp.append(nums [i])
		backtrack(res, temp, nums, i + 1)
		temp.pop()


def backtrack(res, temp, nums, start) :
	res.append([])
	for i in temp :
		res [- 1].append(i);
	for i in range(start, len(nums)) :
		temp.append(nums [i])
		backtrack(res, temp, nums, i + 1)
		temp.pop()

