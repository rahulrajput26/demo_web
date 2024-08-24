import streamlit as st
st.title("welome")
st.header("Enjoy calculator...")
a=st.selectbox("select operation :",("select","Addition","Subtraction","Multiplication","Division"))
b=st.number_input("Enter 1st number : ")
c=st.number_input("Enter 2st number : ")
if a=="Addition" :
      d=st.button("print sum")
      if d :
            st.write("**sum is** ",b+c)
if a=="Subtraction" :
      d=st.button("print minus")
      if d :
            st.write("**minus is **",b-c)
if a=="Multiplication" :
      d=st.button("print multiply")
      if d :
            st.write("**product is** ",b*c)
if a=="Division" :
      d=st.button("print division")
      if d :
            st.write("**division is** ",b/c) 
if d :
      st.write("Thank uhh..")
      
      