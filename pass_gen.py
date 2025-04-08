import streamlit as st

st.image("1592485.png", width=100)
st.title("Password Generator 🔒🔑")

un = st.text_input("Enter your new user_id: ")
sp1 = st.text_input("Enter your new password: ", type="password")
sp2 = st.text_input("Re-enter your password: ", type="password")

if (sp1 == sp2) and (sp1 != ""):
    st.success("Yor password is saved 📁")

    un2 = st.text_input("Enter your_id: ")
    sp3 = st.text_input("Enter your password: ", type="password")
    
    if st.button("Login"):
        if(sp2 == sp3) and (un == un2):
          st.success("Congratulations! you succesfuly logged in")

          st.markdown("[Click on it 👉 www.linkedin.com/in/aman-sharma-5050a3229]")
        else:
          st.error("Error! please check your user_id or password 🚫.")
else:
    if (sp1 != "") and (sp2 != ""):
        st.error("Please check your new and re-enter password ❎")
