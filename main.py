#############################################
#                  TODO                     #
#                 debug!                    #
#                                           #
#############################################
#
# BUG:
#
# 点击下棋后棋盘未更新甚至未运算
# 即时棋盘更新，robot也没有下棋
#
# 注：streamlit run main.py 启动






import streamlit as st
import dbh as rdb
import ttt_core as tc
import random as rd

#################################

def stvar_r(name):
	if name not in st.session_state:
		st.session_state[name] = 0
	return st.session_state[name]
def stvar_w(name,value):
	st.session_state[name] = value

#################################

def pgtomd(ipg):
	global pg
	for i in range(len(ipg)):
		if ipg[i] == 'N':
			ipg[i] = ''
	pg = f"""
	|.{ipg[0]}.|.{ipg[1]}.|.{ipg[2]}.|
	|:--:|:--:|:--:|
	|.{ipg[3]}.|.{ipg[4]}.|.{ipg[5]}.|
	|.{ipg[6]}.|.{ipg[7]}.|.{ipg[8]}.|
	"""


#################################
#########初始化变量###############
#################################

if 'playeris' not in st.session_state:
	st.session_state['playeris'] = 'X'
if 'robotis' not in st.session_state:
	st.session_state['robotis'] = 'O'
if 'mode' not in st.session_state:
	st.session_state['mode'] = 1
if 'ipg' not in st.session_state:
	st.session_state['ipg'] = ['N','N','N','N','N','N','N','N','N']
	pgtomd(['N','N','N','N','N','N','N','N','N'])

################################


# mode 1我方概率大 2对方概率小 3我方可行性多 4对方可行性少
# 其它模式还没做
def robot(nowpg):
	mode = stvar_r('mode')
	allpg = tc.fillN(nowpg,stvar_r('robotis'))
	nbs = []
	for thispg in allpg:
		cond = {}
		dbkeys = ['0','1','2','3','4','5','6','7','8']
		for i in range(len(thispg)):
			if thispg[i] == 'N':
				pass
			else:
				cond[dbkeys[i]] = thispg[i]
		#print(cond)
		cond['f'] = stvar_r('robotis')
		r_ways = rdb.get_data_num('pgsdb.db','pgs',cond)
		cond['f'] = 'T'
		t_ways = rdb.get_data_num('pgsdb.db','pgs',cond)
		cond['f'] = stvar_r('playeris')
		p_ways = rdb.get_data_num('pgsdb.db','pgs',cond)
		#print(r_ways,t_ways,p_ways)
		nbs.append([r_ways,t_ways,p_ways])

	if mode == 1:
		tmpcprlst = []
		if rd.randint(0,1) == 0:
			for i in range(len(nbs)):
				tmpcprlst.append(nbs[i][0])
			stvar_w('ipg',allpg[tmpcprlst.index(max(tmpcprlst))])
		else:
			for i in range(len(nbs)):
				tmpcprlst.append(nbs[i][0] + nbs[i][1])
			stvar_w('ipg',allpg[tmpcprlst.index(max(tmpcprlst))])

	elif mode == 2:
		...
	elif mode == 3:
		...
	elif mode == 4:
		...
	else:
		print('???')







def afterplayer(nextstepplayer):
	global isthatover
	global whoover
	tmp = stvar_r('ipg')[:]
	if tmp[nextstepplayer] == 'N':
		tmp[nextstepplayer] = stvar_r('playeris')
		stvar_w('ipg', tmp)
		game_status = tc.isover(tmp)
		if game_status is None:
			robot(stvar_r('ipg'))
			tmp = stvar_r('ipg')
			game_status = tc.isover(tmp)
			if game_status is None:
				robot(stvar_r('ipg'))
			else:
				isthatover = True
				if game_status == 'T':
					whoover = '平!'
				else:
					whoover = game_status + '胜!'
		else:
			isthatover = True
			if game_status == 'T':
				whoover = '平!'
			else:
				whoover = game_status + '胜!'
	pgtomd(stvar_r('ipg'))







#############################################
#################### UI #####################
#############################################
rst1, rst2, rst3 = st.columns([1, 1, 5])
with rst1:
	st.markdown("重新开始：")
with rst2:
	if st.button('X', disabled=False):
		stvar_w('ipg',['N','N','N','N','N','N','N','N','N'])
		stvar_w('robotis','O')
		stvar_w('playeris','X')
		pgtomd(stvar_r('ipg'))
with rst3:
	if st.button('O', disabled=False):
		stvar_w('ipg',['N','N','N','N','N','N','N','N','N'])
		stvar_w('robotis','X')
		stvar_w('playeris','O')
		robot(stvar_r('ipg'))
		pgtomd(stvar_r('ipg'))

mode = st.slider("模式(机器人视角)：1我方概率大 2对方概率小 3我方可行性多 4对方可行性少", 1, 4, 1, 1)
if mode:
	stvar_w('mode',mode)
	#print(stvar_r('mode'))

st.markdown("---")

isthatover = False
whoover = 0
with st.form("go"):
	nextstepplayer = st.slider("位置：", 0, 8, 0, 1)
	if st.form_submit_button("下棋"):
		afterplayer(nextstepplayer)
		st.markdown(pg)
		st.markdown('---')
		if isthatover:
			stvar_w('ipg',['N','N','N','N','N','N','N','N','N'])
			st.markdown('# **' + whoover + '**')
