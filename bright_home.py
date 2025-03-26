import streamlit as st
import cash_data_import 
import invoice_data_import

# 初期状態では何も表示しないようにセッション状態を設定
if 'current_app' not in st.session_state:
    st.session_state['current_app'] = None

st.title('freee_import')

# ボタンが押されたときに実行する関数
def show_app1():
    st.session_state['current_app'] = 'app1'

def show_app2():
    st.session_state['current_app'] = 'app2'


# サイドバーでアプリ選択用のボタンを表示
with st.sidebar:
    if st.button('窓口売上', key='app1'):
        show_app1()

    if st.button('請求売上', key='app2'):
        show_app2()

# 選択されたアプリを表示
if st.session_state['current_app'] == 'app1':
    cash_data_import.app1()
elif st.session_state['current_app'] == 'app2':
    invoice_data_import.app2()