Rs_time_Millisecond=[1200,1500,1000]

def rs_time(x):
    return x/1000
rstime=list(map(rs_time,Rs_time_Millisecond))
rstime=list(map(lambda x:x/1000,Rs_time_Millisecond))

print(rstime)