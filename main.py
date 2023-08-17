#############################################
#                  TODO                     #
#               写robot算法                  #      #nmd sublimetext怎么对不齐
#                                           #
#############################################

import streamlit as st
import time

def stvar_r(name):
	if name not in st.session_state:
		st.session_state[name] = 0
	return st.session_state[name]
def stvar_w(name,value):
	st.session_state[name] = value

#################################
#########初始化变量###############
#################################

if 'playeris' not in st.session_state:
	st.session_state['playeris'] = 'X'
if 'robotis' not in st.session_state:
	st.session_state['robotis'] = 'O'
if 'mode' not in st.session_state:
	st.session_state['mode'] = 1

################################

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

# mode 1我方概率大 2对方概率小 3我方可行性多 4对方可行性少
def robot(nextstepplayer,mode):
	...

def afterplayer(nextstepplayer):
	global ipg
	ipg[nextstepplayer] = stvar_r('playeris')
	pgtomd(ipg)

ipg = ['N','N','N','N','N','N','N','N','N']
pgtomd(ipg)





#############################################
#################### UI #####################
#############################################
rst1, rst2, rst3 = st.columns([1, 1, 5])
with rst1:
	st.markdown("重新开始：")
with rst2:
	if st.button('X', disabled=False):
		ipg = ['N','N','N','N','N','N','N','N','N']
		stvar_w('robotis','O')
		stvar_w('playeris','X')
		pgtomd(ipg)
with rst3:
	if st.button('O', disabled=False):
		ipg = ['N','N','N','N','N','N','N','N','N']
		stvar_w('robotis','X')
		stvar_w('playeris','O')
		pgtomd(ipg)

mode = st.slider("模式(机器人视角)：1我方概率大 2对方概率小 3我方可行性多 4对方可行性少", 1, 4, 1, 1)
if mode:
	stvar_w('mode',mode)
	print(stvar_r('mode'))

st.markdown("---")

with st.form("go"):
	nextstepplayer = st.slider("位置：", 0, 8, 0, 1)
	if st.form_submit_button("下棋"):
		afterplayer(nextstepplayer)
		st.markdown(pg)
		st.markdown('---')
