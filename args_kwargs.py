#def function_name_print(a,b,c,d):
 #   print(a,b,c,d)

def funargs(normal,*args, **kwargs):
    print(normal)
    # print(type(args))
    # print(args[0])
    for item in args:
        print(item)
    print("\nNow I would like to introduce\n")   
    for  key, value  in kwargs.items():
        print(f"{key} is a {value}")

# ab koi naya banda ata ha ur apna name add krny ka kehta ha, lakin humny to srf 4 argument kahay han,ur hum 5 nhi kr skty.kyunky agr hum 5th argument de bhi dein to agar 100 banday agaye to hum argument kis trha dein gay.
    
#function_name_print("Harry", "Zain","Bilal", "Hassan")


har = ["Harry", "Zain","Bilal", "Hassan", "hasni", "The Programmer"]
normal = "this is a normal"
kw = {"Rohan": "Monitor", "Zaan": "Instructor", "Bila": "Gandu"}
funargs(normal,*har, **kw)
# ab *har ka matlab ha ky jo bhi saray ky saray arguments han wo pass ho jain gay. ye as a tuple jata ha.
# ab mein loop chalany ky baad jitny name add krta jaon ga to ye add hoty jain gay.
# hum phir normal argument bhi de skty han.

# ur aik fun fact ky hum *args ko *zain bhi likh skty han.
# agar hum normal argument ko star wali ky baad dalain gy function argument mein to error de ga.
# pehly normal, phir *args ur phir **kwargs dalo.
# *args ur **kwargs optionaal ha.

# ab zaroori nhi ky hum **kwargs likhain, bas showe hona chahiye.


