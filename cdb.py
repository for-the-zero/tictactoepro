import ttt_core as tc

# 生成井字棋盘面
# 一个盘面列表是9个字符串，N是空
# tc.isover判断胜负平，无返回代表没结束
# tc.fillN 返回所有可以下的位置的盘面
# 包括tc.fillN、rt、pgs，列表的每一项都是一个盘面列表

# 有bug
def create():
	rt = [] # 返回的列表
	pgs = [['N','N','N','N','N','N','N','N','N']] #待处理盘面
	pgs += tc.fillN(pgs[0],'X')
	pgs.remove(pgs[0])
	#input(pgs)
	cp = 0
	while True:
		if pgs == []: #没有待处理后退出
			break

		if tc.isover(pgs[0]) != None: # 判断
			tmp = pgs[0]
			tmp += tc.isover(pgs[0]) # 结尾加上tc.isover的返回值
			rt += tmp
			pgs.remove(pgs[0])
			continue

		if pgs[0].count('X') > pgs[0].count('O'):
			# 填充O后的盘面添加到待处理
			pgs += tc.fillN(pgs[0],'O')
		else:
			# 填充X后的盘面添加到待处理
			pgs += tc.fillN(pgs[0],'X')
		pgs.remove(pgs[0])
		#input(pgs)
		cp += 1
		if cp == 1000:
			cp = 0
			print(pgs)
			input(rt)

def create2():
    rt = []  # 返回的列表
    pgs = [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']]  # 待处理盘面
    pgs += tc.fillN(pgs[0], 'X')
    pgs.remove(pgs[0])
    
    cp = 0
    while True:
        if len(pgs) == 0:  # 没有待处理盘面时退出
            break
        
        if tc.isover(pgs[0]) is not None:  # 判断胜负
            tmp = pgs[0]
            tmp += [tc.isover(pgs[0])]  # 结尾加上tc.isover的返回值
            rt.append(tmp)
            pgs.remove(pgs[0])
            continue
        
        if pgs[0].count('X') > pgs[0].count('O'):
            # 填充O后的盘面添加到待处理
            pgs += tc.fillN(pgs[0], 'O')
        else:
            # 填充X后的盘面添加到待处理
            pgs += tc.fillN(pgs[0], 'X')
        pgs.remove(pgs[0])
        
        '''
        # 测试代码是否正常运行
        cp += 1
        if cp == 50000:
            cp = 0
            print(pgs)
            input(rt)
        '''
    return rt

def create3():
    rt = {'X':0,'O':0,'T':0}  # 返回的列表
    pgs = [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']]  # 待处理盘面
    pgs += tc.fillN(pgs[0], 'X')
    pgs.remove(pgs[0])
    
    cp = 0
    while True:
        if len(pgs) == 0:  # 没有待处理盘面时退出
            break
        
        if tc.isover(pgs[0]) is not None:  # 判断胜负
            tmp = pgs[0]
            tmp += [tc.isover(pgs[0])]  # 结尾加上tc.isover的返回值
            rt[tc.isover(pgs[0])] += 1
            pgs.remove(pgs[0])
            continue
        
        if pgs[0].count('X') > pgs[0].count('O'):
            # 填充O后的盘面添加到待处理
            pgs += tc.fillN(pgs[0], 'O')
        else:
            # 填充X后的盘面添加到待处理
            pgs += tc.fillN(pgs[0], 'X')
        pgs.remove(pgs[0])
        
        # 测试代码是否正常运行
        #cp += 1
        #if cp == 50000:
        #    cp = 0
        #    input(rt)
    return rt

if __name__ == '__main__':
	#print(create3())
	formatted_str = '\n'.join(str(item) for item in create2())
	filename = 'pgstxt.txt'
	with open(filename, 'w') as file:
		file.write(formatted_str)