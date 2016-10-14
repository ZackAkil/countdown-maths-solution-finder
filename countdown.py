import sys
import copy

# get all unique order sets of a list (with replace)
def comb(ele, curr=[], depth=-1):
	tots = []
	depth = 0 if depth == -1 else depth
	if depth == len(ele)-1:
		for i in ele:
			tots.append(curr + [i]) 
	else:
		for i in ele:
			tots.extend(comb(ele,curr + [i],depth+1))
	return tots


# get all unique order sets of a list (with remove)
def nest(l):
	if len(l) == 1:
		return l
	stacks = []
	for n in l:
		g = nest([x for x in l if x != n])
		if len(g) == 1:
			g.insert(0,n)
			stacks.append(g)
		else:
			for v in g:
				v.insert(0,n)
			stacks.extend(g)
	return stacks

# apply calculation set to a set of nums: assert(len(calcs) == len(nums)-1)
def calc(funcs, nums):
	if len(nums)==1:
		return nums[0]
	else:
		return funcs.pop()[0](nums.pop(), calc(funcs,nums))

def doCal(op, nums):
	ops = copy.deepcopy(op)
	numsl = copy.deepcopy(nums)
	try:
		return calc(ops,numsl)
	except ZeroDivisionError:
		return None

# generate printable formula of equation
def drawCal(op, nums):
	return ' '.join(map(lambda a,b: str(a)+(b[1]+'('if b else')'*len(op)),nums[::-1],op[::-1])).replace(' ','')

def countDown(nums,target):
	ops = [(lambda a,b:a+b,'+'),(lambda a,b:a-b,'-'),(lambda a,b:a*1.0/b*1.0,'/'),(lambda a,b:a*b,'*')]
	allNums = nest(nums)
	allOps = comb(ops)
	results = []
	for num in allNums:
		for op in allOps:
			calResult = doCal(op,num)
			results.append((abs(target - calResult) if calResult else None ,calResult,drawCal(op,num)))
	return results

o = sorted(countDown([4,19,33,200,15],1208),key=lambda x: (x[0] is None, x[0]))

print o[:5]
print len([x for x in o if x[0]==0]), 'correct answers'
