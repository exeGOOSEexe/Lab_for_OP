import os,datetime,math
from count_points_in_circle import count_points_in_circle
from time_ti import time_to_get,time_strart,time_closed,toFixed
fi = (os.listdir())
files = fi
if "input.txt" in files:
    f = open("input.txt",'r')
    h = open("output.txt",'a')
    time_hours_min = time_to_get()
    time_hours_max = time_strart()
    time_min_gi = time_closed()
    r = f.readline(); r = int(r)
    x = f.readline()
    x0 = x[0]; x0 = int(x0)
    y0 = x[1]; y0 = int(y0)
    count = count_points_in_circle(r, x0, y0)
    h.writelines(str(time_hours_min) + " " + str(time_hours_max))
    h.writelines("\n" + str(count))
    h.writelines("\n" + str(toFixed(time_min_gi,2)))