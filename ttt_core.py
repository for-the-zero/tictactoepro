def fillN(pg,next):
	rt = []
	for i in [0,1,2,3,4,5,6,7,8]:
		if pg[i] == 'N':
			#input(i)
			#input(pg)
			tmp = pg[:]
			#input(tmp)
			#input(pg)
			tmp[i] = next
			#input(tmp)
			rt.append(tmp)
			#input(rt)
	return rt

def isover(pg):
    def issame(lst):
        if pg[lst[0]] == pg[lst[1]] == pg[lst[2]] and pg[lst[0]] != 'N':
            return pg[lst[0]]
        else:
            return None
    
    for i in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if issame(i) is not None:
            return issame(i)
    
    if 'N' not in pg:
        return 'T'
    else:
        return None
