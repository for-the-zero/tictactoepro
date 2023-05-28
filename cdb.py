import ttt_core as tc

def create():
	rt = []
	pgs = [['N','N','N','N','N','N','N','N','N']]
	pgs += tc.fillN(pgs[0],'X')
	pgs.remove(pgs[0])
	#input(pgs)
	cp = 0
	while True:
		if pgs == []:
			break

		if tc.isover(pgs[0]) != None:
			tmp = pgs[0]
			tmp += tc.isover(pgs[0])
			rt += tmp
			pgs.remove(pgs[0])
			continue

		if pgs[0].count('X') > pgs[0].count('O'):
			# O
			pgs += tc.fillN(pgs[0],'O')
		else:
			# X
			pgs += tc.fillN(pgs[0],'X')
		pgs.remove(pgs[0])
		#input(pgs)
		cp += 1
		if cp == 1000:
			cp = 0
			print(pgs)
			input(rt)

def create2():
    rt = []
    pgs = [['N','N','N','N','N','N','N','N','N']]
    pgs += tc.fillN(pgs[0], 'X')
    pgs.remove(pgs[0])
    cp = 0
    while True:
        if not pgs:
            break

        if tc.isover(pgs[0]) is not None:
            tmp = pgs[0] + [tc.isover(pgs[0])]
            rt.append(tmp)
            pgs.remove(pgs[0])
            continue

        if pgs[0].count('X') == pgs[0].count('O'):
            pgs += tc.fillN(pgs[0], 'X')
        else:
            pgs += tc.fillN(pgs[0], 'O')
        pgs.remove(pgs[0])
        cp += 1
        if cp == 10000:
            cp = 0
            print(pgs)
            input(rt)


if __name__ == '__main__':
	create2()