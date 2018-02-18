def rpn(func):
	n = func.split()
	try:
		s = []
		for f in n:
			if f == '+':
				s = [sum(s)]
			elif f == '-':
				n = s[0]
				for g in s[1:]:
					n -= g
				s = [n]
			elif f == '*':
				n = s[0]
				for g in s[1:]:
					n *= g
				s = [n]
			elif f == '/':
				n = s[0]
				for g in s[1:]:
					n /= g
				s = [n]
			else:
				s.append(int(f))
	except:
		print("invalid RPN function")
	return(str(s[0]))
