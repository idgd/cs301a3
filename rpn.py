def rpn(func):
	n = func.split()
	try:
		s = []
		for f in n:
			if f == '+':
				a = s.pop()
				b = s.pop()
				s.append(a + b)
			elif f == '-':
				a = s.pop()
				b = s.pop()
				s.append(a - b)
			elif f == '*':
				a = s.pop()
				b = s.pop()
				s.append(a * b)
			elif f == '/':
				a = s.pop()
				b = s.pop()
				s.append(a / b)
			else:
				s.append(float(f))
	except:
		print("invalid RPN function")
	try:
		return(str(s[0]))
	except:
		return("invalid RPN function")
