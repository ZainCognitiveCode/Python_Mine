# REGULAR EXPRESSION

import re

pattern = r"[A-Z]ain"
# ab ye r ka mtlab raw string ha. ur hum [] mein koi cheez de skty han ky is trha ho,ur agay aisay words hon to wo search kr day ga humain. 
text = '''I am Zain and I am doing Coding. Zain is a good boy and he will be an Ai Engineer. he is Dain'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)

for match in matches:
    print(match.span())
    print(text[match.span()[0] :match.span()[1]])


# match ki type tuple ha.