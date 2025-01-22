import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load leaderboard data
@st.cache
def load_data():
    data = pd.read_csv('leaderboard.csv')
    return data

data = load_data()

# Remove entries without roll numbers
data = data[data['TeamMemberUserNames'].notnull()]

# Title and Description
st.title("Leaderboard Dashboard with TOPSIS")
st.write("This dashboard displays the leaderboard data with TOPSIS results.")

# TOPSIS Implementation
def topsis(data_pd, weights, impacts):
    if len(weights) != len(impacts) or len(weights) != data_pd.shape[1]:
        raise ValueError("Length of weights and impacts must match the number of criteria columns.")
    
    # Extract numeric data for criteria
    data = data_pd.values.astype(float)
    
    # Normalize the data
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))
    
    # Apply weights
    weights_array = np.array(weights)
    weighted_data = norm_data * weights_array
    
    # Determine ideal best and worst solutions
    pos_ideal = np.array([
        np.max(weighted_data[:, i]) if impacts[i] == '+' else np.min(weighted_data[:, i]) 
        for i in range(weighted_data.shape[1])
    ])
    neg_ideal = np.array([
        np.min(weighted_data[:, i]) if impacts[i] == '+' else np.max(weighted_data[:, i]) 
        for i in range(weighted_data.shape[1])
    ])
    
    # Calculate distances to ideal solutions
    pos_distance = np.sqrt(((weighted_data - pos_ideal) ** 2).sum(axis=1))
    neg_distance = np.sqrt(((weighted_data - neg_ideal) ** 2).sum(axis=1))
    
    # Calculate TOPSIS scores
    scores = neg_distance / (neg_distance + pos_distance)
    
    # Add scores and ranks to the DataFrame
    data_pd['Topsis Score'] = scores
    data_pd['Stand'] = scores.argsort()[::-1] + 1  # Rank in descending order of scores
    
    return data_pd

# Select relevant columns for TOPSIS
topsis_data = data[["Rank", "Score", "SubmissionCount"]].copy()

# Weights and impacts for the criteria
weights = [1, 2, 3]  # Adjust weights as needed
impacts = ['-', '+', '+']  # Adjust impacts as needed

# Apply TOPSIS
topsis_result = topsis(topsis_data, weights, impacts)

# Add results back to the original dataset
data['Topsis Score'] = topsis_result['Topsis Score']
data['Stand'] = topsis_result['Stand']

data = data[["Stand", "TeamId", "TeamName", "LastSubmissionDate", "Score", "SubmissionCount", "TeamMemberUserNames", "Rank"]]
data = data.rename(columns={'Rank': 'Original_Rank'})

# Player Name Filter
player_name = st.text_input("Search for a player:", key="player_search")
filtered_data = data[data['TeamName'].str.contains(player_name, case=False)] if player_name else data

# Dropdown Menu for Displaying Records
st.subheader("Select Number of Records to Display:")
options = [10, 20, 30, 50, 'All']  # Added 'All' option
selected_top_n = st.selectbox("Choose the number of records:", options)

# Displaying Records
if selected_top_n == 'All':
    displayed_data = filtered_data.sort_values('Stand')  
else:
    displayed_data = filtered_data.nsmallest(selected_top_n, 'Stand') 

# Display the filtered data
st.dataframe(displayed_data)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Line Graph for Submission Count of Selected Players
st.subheader("Submission Count Distribution of Selected Players")
submission_counts = displayed_data['SubmissionCount'].value_counts().sort_index()

# Create a line graph
plt.figure(figsize=(16, 9))
plt.plot(submission_counts.index, submission_counts.values, marker='o', linestyle='-', color='b', markersize=8, linewidth=2)

plt.title('Distribution of Submission Counts Among Selected Players', fontsize=16)
plt.xlabel('Submission Count', fontsize=14)
plt.ylabel('Number of Teams', fontsize=14)

plt.ylim(0, submission_counts.values.max() + 1)  
y_ticks = np.arange(0, submission_counts.values.max() + 2, 1)  
plt.yticks(y_ticks)
plt.grid(True, linestyle='--', alpha=0.7)  

st.pyplot(plt)
plt.clf()


