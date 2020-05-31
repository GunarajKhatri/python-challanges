#Find sum of all multiples of 3 or 5 below 1000
#mf=>multiple of 5
#mt=>multiple of 3
#tmf=>total multiple of 5
#tmt=>total multiple of 3
tmf=0
tmt=0
for i in range(1,1000):
	mf=5 * i
	mt=3* i
	if mf < 1000:
		tmf=tmf+mf
	if mt < 1000:
		tmt=tmt+mt
total=tmf+tmt

print(total)