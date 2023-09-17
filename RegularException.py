import re
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ.
gmail.com
1234567890
123-456-789
123.456.789
cat 
bat 
mat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinsons
Mr. T
'''
print('\tTab') #\t aik tab jitni space deta ha.
print(r'\rTab') #agar ik r laga dein to ye normal treat karay ga \t ko ur koi space nhi de ga.

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print(text_to_search[0:3])

# pattern = re.compile(r'\.') Ye . ko is  trha find krty han.
# pattern = re.compile(r'gmail\.com') kisi link ko match krna ho to . ky bad website ki extension deni ha. jaisy .com 
# pattern = re.compile(r'.') sb chezon ko file mein match krny ky liye ye . only use hota ha.
# ye sb net pr hain.

# with open('Fil_text.txt', 'r') as f:
#     contents = f.read() 

#     matches = pattern.finditer(contents)

# for match in matches:
#     print(match)


pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


pattern = re.compile(r'[1-5]') #from 1 to 5
pattern = re.compile(r'[a-zA-Z]') #from a to z and including A to Z
pattern = re.compile(r'[^a-zA-Z]') # ab ye inky elawa baki sb ko match karay ga, ^ ki waja sy. 
pattern = re.compile(r'[^b]at') # ye srf bat ko match nhi karay ga. 
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # ye aisy digits ko match karay ga jo 3 3 ky pairs mein hn. 
pattern = re.compile(r'{3}') # exact number ko match karay ga. 
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') 

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

pattern = re.compile(r'[a-zA-Z0-9._-+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9.+]+')

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
urls= ''' https://www.google.com 
            https://www.youtube.com 
            '''
subbed_urls = pattern.sub(r'\2\3',urls)
print(subbed_urls)

matches = pattern.findall(text_to_search) #(findall) ye srf exact match ko find krta ha.
# finditer sab ko match kr skta ha. ur yahi sb sy acha ha. 



