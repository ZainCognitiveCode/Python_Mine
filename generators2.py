# yield generator return krta ha ur execution ko suspend kr deta ha, next values tak.
def my_generator():
    for i in range(5000):
        yield i
        
gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for k in gen:
    print(k)

# generator sy memory bhi free hoti ha. ye moka pr value ko memory mein store krta ha. generators are lazy. which means they generate values only when required.

        
