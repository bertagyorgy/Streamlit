import streamlit as st

st.title("Kalkulátor app Streamlitben")

st.write("---")

szam1 = st.number_input(label="Első szám")
szam2 = st.number_input(label="Második szám")

st.write("Művelet kiválasztása")
operation = st.radio("Add meg, milyen műveletet akarsz elvégezni:",
                     ("Összeadás", "Kivonás", "Szorzás", "Osztás"))
ans = 0

def kalkulálás():
  if operation == "Összeadás":
  	ans = szam1 + szam2
  elif operation == "Kivonás":
    ans = szam1 - szam2
  elif operation == "Szorzás":
    ans = szam1 * szam2
  elif operation == "Osztás":
    ans = szam1 / szam2

  st.success(f"Eredmény: {ans}")
 	else:
		st.warning("0val való osztás nem lehetséges")
		ans = "Nincs értelmezve"
if st.button("Eredmény kiszámolása"):
		kalkulálás()
   
   
    
