# Literals is a raw data given in a variable. In python, there are various types
# Numeric literal
# String Literal
#Boolean Literal
# Special Literal

a = 0b1010 #Binary Literals
b = 100 #Decimal Literals
c = 0o310 #Octal Literals
d = 0x12c #HexaDecimal Literal
print(a,b,c,d)

# Float Literals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3
print(float_1,float_2,float_3)

# Complex Literal
# j is used to show imaginary part, while 0 is real part and  point value 3.14j is imaginary
x = 0+3.14j
print(x,x.imag,x.real)

# String Literals
string = 'This is python'
strings = "This is python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
# u is used to show unicode
raw_str = r"raw\n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# Boolean Literals
a = True + 4
# True is recognized as 1
b = False + 10

print(a)
print(b)

# Special Literal
a = None
print(a)

# We do not declare variables, we use them directly.
c = 34+45
# Variable declaration by using None.
k = None

