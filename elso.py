import streamlit as st
 
st.title("A 2 hatványai")
st.write("Görgesd a csúszkát")
level = st.slider("2 hányadik hatványa legyen?", 1, 10)
st.text('Selected: {}'.format(2**level))
   
    
