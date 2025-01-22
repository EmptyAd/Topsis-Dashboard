# Topsis Dashboard

## Overview
The Topsis Dashboard is a web application built using Streamlit that provides a user-friendly interface for visualizing leaderboard data and applying the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method. This dashboard enables users to analyze and rank teams based on their scores and submission counts.

## Link: https://dashboardpy-l3qscmv8jtnkjku5swhb9b.streamlit.app

## Features
- **Leaderboard Visualization**: Displays a leaderboard with various team metrics.
- **TOPSIS Implementation**: Applies the TOPSIS method to rank teams based on specified weights and impacts for different criteria.
- **Dynamic Filtering**: Users can search for specific players or teams and filter results dynamically.
- **Submission Count Analysis**: Visualizes submission counts of selected teams using line graphs.
- **Interactive Controls**: Allows users to choose the number of top players to display or view all records.

## Technologies Used
- **Python**: The primary programming language.
- **Streamlit**: For building the web application.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib**: For data visualization.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EmptyAd/Topsis-Dashboard.git
   cd Topsis-Dashboard
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Use the search bar to filter for specific teams or players.
- Select the number of top players to display from the dropdown menu or view all records.
- The dashboard will automatically apply the TOPSIS method and display the results.
