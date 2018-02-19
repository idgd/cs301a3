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
				s.append(float(f))
	except:
		print("invalid RPN function")
	try:
		return(str(s[0]))
	except:
		return("invalid RPN function")
