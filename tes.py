import streamlit as st

st.title("Contoh Website Python")
with st.form(key="my_form"):
    nama = st.text_input("nama lengkap")
    jenis_kelamin= st.radio("jenis kelamin", ("Laki-laki", "Perempuan"))
    submit = st.form_submit_button(label="Kirim")