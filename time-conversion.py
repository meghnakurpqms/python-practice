

time = input().strip()
if time.endswith('AM'):
    res = time[:8]
    min = (int(time[:2]))
    if (min == 12):
        min = 0
    if(min%10>0):
        res = '0' + str(min) + time[2:8]
    else:
        res = str(min).center(2, '0') + time[2:8]



if time.endswith('PM'):
    min = (int(time[:2]) + 12) % 24
    if (min == 0):
        min = 12
    res = str(min).center(2, '0') + time[2:8]

print(res)

# f.close()
