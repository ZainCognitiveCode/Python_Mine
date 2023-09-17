# from python 3.6. newly introduced

# string formatting problem

letter = "Hey my name is {0} and I am from {1}"
country = "India"
name = "Zain"
print(letter.format(name,country))
# agr mein country phly likh deta to ye ghalat ho jata.
# isko fix krny ky liye number de skty han {} mein

print(f"Hey my name is {name} and I am from {country}")
# aaab hum f string ky zariye name ur country daal skty han numbers ki jaga.

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.0999))

# is say hum 2 decimal places tk ja skty han
# is trha neechy dekho

price = 49.099999
txt1 = f"For only {price:.2f} dollars!"
print(txt1)

# hum numbers ko string mein print krwa skty han
print(type(f"{2*30}"))


