import streamlit as st
 
# st.title("A 2 hatványai")
# st.write("Görgesd a csúszkát")
# level = st.slider("2 hányadik hatványa legyen?", 1, 10)
# st.text('Kiválasztva: {}'.format(2**level))

st.header("Űrlap")

nev = st.text_input("Név")
email = st.text_input("E-mail cím")
eletkor = st.slider("Életkor", 1, 100)
nem = st.radio("Nem: ", ('Fiú', 'Lány'))
if (nem == 'Fiú'):
	st.info("Sikeresen rögzítve: Fiú")
else:
	st.info("Sikeresen rögzítve: Lány")

if(st.button("Beküldés")):
	st.success("Válaszodat rögzítettük.")
   
    
