import streamlit as st

check = st.checkbox("Show/Hide")

st.title("Hello")
if check:
    st.button("Click Me")
    st.selectbox("メニューリスト",("選択肢1","選択肢3","選択肢2",))
    st.multiselect("メニューリスト",("選択肢1","選択肢3","選択肢2",))
    st.radio("ラジオボタン",("選択肢1","選択肢3","選択肢2",))
    st.text_input("文字入力欄")
    st.text_area("テキストエリア")

