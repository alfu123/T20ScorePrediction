
# import tkinter as tk
# from tkinter import ttk, messagebox
# import pickle
# import pandas as pd


# pipe = pickle.load(open('pipe.pkl', 'rb'))


# teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England',
#          'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka']

# cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London',
#           'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington',
#           'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai',
#           'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore',
#           'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff',
#           'Christchurch', 'Trinidad']


# root = tk.Tk()
# root.title("Cricket Score Predictor")
# root.geometry("500x650")
# root.resizable(False, False)

# title_label = tk.Label(root, text="T20 Cricket Score Predictor", font=("Arial", 18, "bold"))
# title_label.pack(pady=15)



# frame = tk.Frame(root)
# frame.pack(pady=10)

# # Batting Team
# tk.Label(frame, text="Batting Team:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=8, sticky='w')
# batting_team_cb = ttk.Combobox(frame, values=teams, state="readonly", width=20)
# batting_team_cb.grid(row=0, column=1)
# batting_team_cb.current(0)

# # Bowling Team
# tk.Label(frame, text="Bowling Team:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=8, sticky='w')
# bowling_team_cb = ttk.Combobox(frame, values=teams, state="readonly", width=20)
# bowling_team_cb.grid(row=1, column=1)
# bowling_team_cb.current(1)

# # City
# tk.Label(frame, text="City:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=8, sticky='w')
# city_cb = ttk.Combobox(frame, values=cities, state="readonly", width=20)
# city_cb.grid(row=2, column=1)
# city_cb.current(0)

# # Current Score
# tk.Label(frame, text="Current Score:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=8, sticky='w')
# current_score_entry = tk.Entry(frame, width=22)
# current_score_entry.grid(row=3, column=1)

# # Overs Done
# tk.Label(frame, text="Overs Completed:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=8, sticky='w')
# overs_entry = tk.Entry(frame, width=22)
# overs_entry.grid(row=4, column=1)

# # Wickets Out
# tk.Label(frame, text="Wickets Fallen:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=8, sticky='w')
# wickets_entry = tk.Entry(frame, width=22)
# wickets_entry.grid(row=5, column=1)

# # Runs in Last 5 Overs
# tk.Label(frame, text="Runs in Last 5 Overs:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=8, sticky='w')
# last_five_entry = tk.Entry(frame, width=22)
# last_five_entry.grid(row=6, column=1)



# def predict_score():
#     try:
#         batting_team = batting_team_cb.get()
#         bowling_team = bowling_team_cb.get()
#         city = city_cb.get()

#         current_score = int(current_score_entry.get())
#         overs = float(overs_entry.get())
#         wickets = int(wickets_entry.get())
#         last_five = int(last_five_entry.get())

#         if overs <= 0:
#             messagebox.showerror("Error", "Overs must be greater than 0")
#             return

#         balls_left = 120 - int(overs * 6)
#         crr = current_score / overs
#         wickets_left = 10 - wickets

#         # Create DataFrame
#         input_df = pd.DataFrame({
#             'batting_team': [batting_team],
#             'bowling_team': [bowling_team],
#             'city': [city],
#             'current_score': [current_score],
#             'balls_left': [balls_left],
#             'wickets_left': [wickets_left],
#             'crr': [crr],
#             'last_five': [last_five]
#         })

#         result = pipe.predict(input_df)[0]

#         result_label.config(text=f"Predicted Final Score: {int(result)}")

#     except Exception as e:
#         messagebox.showerror("Error", f"Invalid Input!\n{e}")



# predict_button = tk.Button(root, text="Predict Score", command=predict_score,
#                            font=("Arial", 14), bg="green", fg="white")
# predict_button.pack(pady=20)

# # Result Label
# result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
# result_label.pack(pady=10)

# # Run the app
# root.mainloop()




import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Innings Insight')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))







