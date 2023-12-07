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
hobbik = st.multiselect("Hobbiaid:",
	['Sportolás', 'Olvasás', 'Írás', 'Játék'])
st.write("Hobbik száma", len(hobbik), 'db')

if(st.button("Submit")):
	st.write(nev, email, eletkor, nem, hobbik)
	st.success("Válaszát rögzítettük.")
   
    
