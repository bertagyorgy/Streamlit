import streamlit as st
 
# st.title("A 2 hatványai")
# st.write("Görgesd a csúszkát")
# level = st.slider("2 hányadik hatványa legyen?", 1, 10)
# st.text('Kiválasztva: {}'.format(2**level))

st.header("Űrlap")
nev = st.text_input("Írd be a neved")
email = st.text_input("Írd be az e-mail címed")
eletkor = st.slider("Add meg az életkorod", 1, 100)
nem = st.radio("Nem: ", ('Fiú', 'Lány'))
if (nem == 'Fiú'):
	st.success("Sikeresen rögzítve: Fiú")
else:
	st.success("Sikeresen rögzítve: Lány")


st.button(".button: Click me for no reason")
if(st.button(".button: About")):
	st.text(".text: Welcome To GeeksForGeeks!!!")
   
    
