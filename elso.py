import streamlit as st
 
st.title("Kalkulátor App Streamlitben")
 
# creates a horizontal line
st.write("---")
 
# input 1
num1 = st.number_input(label="Első szám")
 
# input 2
num2 = st.number_input(label="Második szám")
 
st.write("Művelet")
 
operation = st.radio("Válasszon egy műveletet:",
                    ("Összeadás", "Kivonás", "Szorzás", "Osztás"))
 
ans = 0
 
def calculate():
    if operation == "Összeadás":
        ans = num1 + num2
    elif operation == "Kivonás":
        ans = num1 - num2
    elif operation == "Szorzás":
        ans = num1 * num2
    elif operation=="Osztás" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Osztás 0-val hibát jelez. Írjon egy másik számot")
        ans = "Nincs definiálva"
 
    st.success(f"Eredmény: {ans}")
 
if st.button("Eredmény kikalkulásása"):
    calculate()
   
    
