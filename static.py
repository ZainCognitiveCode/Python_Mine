# Static

# humaray pass 2 trha ky variable hotay han.
# 1. instance variable
# iski value hr object ky liye different hoti ha. jaisy pin,balance.


# 2. static variable/ class variable

# har object ky liye is variable ki value different ha, jaisy kisi cutsomer ka serial number.
# jaisy kisi group of students ki degree same ha lakin cgpa different ha,to unki degree static ha. cgpa instance varialbe ho ga.

# instance variable constructor ky andar hoty han,ur static bahir hotay han

from class1 import Atm
c1 = Atm()
c1.sno

# counter ka value same rehta ha, mean agr ik plus hua to wo 2 hi show ho ga.
# last value counter same hi rahay ge.

# humain static variable isliye zaroorat hoti ha kyunky kuch chezain static hoti han.
Atm.get_counter()
# isky bad error aye ga,kyunky counter self expect kr rha ha,lakin humnay usko Atm(class name) ky zariye access kia ha.

