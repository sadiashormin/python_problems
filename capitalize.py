def capitalize(s):
	for x in s.split():
		s = s.replace(x, x.capitalize())
	return s
string = raw_input()
capitalized_string = capitalize(string)
print capitalized_string