import streamlit as st
import time

def pgtomd(ipg):
    global pg
    pg = f"""
    |0={ipg[0]}|1={ipg[1]}|2={ipg[2]}|
    |:--:|:--:|:--:|
    |3={ipg[3]}|4={ipg[4]}|5={ipg[5]}|
    |6={ipg[6]}|7={ipg[7]}|8={ipg[8]}|
    """

def afterplayer(nextstepplayer):
    global ipg
    bar = st.progress(0.0)
    for percentage in range(20):
        time.sleep(0.1)
        bar.progress(percentage * 0.05 + 0.05)
        ipg[nextstepplayer] = 'X'
        pgtomd(ipg)

ipg = ['N','N','N','N','N','N','N','N','N']
pgtomd(ipg)

rst1, rst2, rst3 = st.columns([1, 1, 5])
with rst1:
    st.markdown("重新开始：")
with rst2:
    if st.button('X', disabled=False):
        ipg = ['N','N','N','N','N','N','N','N','N']
        pgtomd(ipg)
with rst3:
    if st.button('O', disabled=False):
        ipg = ['N','N','N','N','N','N','N','N','N']
        pgtomd(ipg)

st.markdown("---")

with st.form("go"):
    nextstepplayer = st.slider("位置：", 0, 8, 0, 1)
    if st.form_submit_button("下棋"):
        afterplayer(nextstepplayer)
        st.markdown(pg)
        st.markdown('---')
