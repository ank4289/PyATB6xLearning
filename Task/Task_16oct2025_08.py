load_time=float(input("enter load time of webpage"))

if load_time < 4 and load_time >=4.2:
    print("Page load is to slow")
elif load_time <=  3 and load_time >1:
    print("Page load on normal speed")
elif load_time < 10 and load_time >= 10:
    print("Page is opening dam slow")
else:
    print("page will not open")