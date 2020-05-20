def change_string(strn: str) -> str:
	strn = strn * 5
	return strn

strn = "keio"
print("before function, strn ==", strn)
strn2 = change_string(strn)
print("after function,  strn ==", strn)
print("                strn2 ==", strn2)
