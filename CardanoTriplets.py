import math
flag = 0
for a in range(1,1000):
	for b in range(1,1000):
		for c in range(1,1000):
			if(a+b+c <= 1000):
				x = a-b*math.sqrt(c)

    				if (x > 0):
        				y = math.pow(x, float(1)/3)    
    				else:
        				y = -math.pow(abs(x), float(1)/3)

		    		z = math.pow(a+b*math.sqrt(c), float(1)/3.0) + y
				if(str(z) == "1.0"):
					flag = flag+1
					print(a,b,c)

print(flag)
