import pandas as pd
import matplotlib.pyplot as plt

file_path = 'updated_dataset.csv'
data = pd.read_csv(file_path)
data.head()

party_counts = data['Leading Party'].value_counts()

top_parties = party_counts.head(10)

plt.figure(figsize=(12, 8))
top_parties.plot(kind='bar', color='skyblue')
plt.title('Top Parties by Number of Seats Won')
plt.xlabel('Party')
plt.ylabel('Number of Seats')
plt.xticks(rotation=45, ha='right')
plt.show()

filtered_df = data[(data['Leading Party'] != 'Bharatiya Janata Party') & (data['Leading Party'] != 'Indian National Congress')]

party_seat_counts = filtered_df['Leading Party'].value_counts().reset_index()
party_seat_counts.columns = ['Leading Party', 'Seats']
party_seat_counts = party_seat_counts.sort_values(by='Seats', ascending=False)

plt.figure(figsize=(12, 8))
plt.barh(party_seat_counts['Leading Party'], party_seat_counts['Seats'], color='skyblue')
plt.xlabel('Number of Seats')
plt.ylabel('Party')
plt.title('Number of Seats Won by Each Party (Excluding BJP and INC)')
plt.gca().invert_yaxis()
plt.show()

data['Margin'] = pd.to_numeric(data['Margin'], errors='coerce')
data = data.dropna(subset=['Margin'])

top_candidates = data.nlargest(10, 'Margin')

plt.figure(figsize=(12, 8))
plt.barh(top_candidates['Leading Candidate'], top_candidates['Margin'], color='skyblue')
plt.xlabel('Margin of Victory')
plt.ylabel('Candidate')
plt.title('Top 10 Best-Performing Candidates by Margin of Victory')
plt.gca().invert_yaxis()
plt.show()

data = data.dropna(subset=['Margin'])

bottom_candidates = data.nsmallest(10, 'Margin')

plt.figure(figsize=(12, 8))
plt.barh(bottom_candidates['Leading Candidate'], bottom_candidates['Margin'], color='skyblue')
plt.xlabel('Margin of Victory')
plt.ylabel('Candidate')
plt.title('Top 10 Candidates with the Lowest Margin of Victory')
plt.gca().invert_yaxis()
plt.show()

data = data.dropna(subset=['Margin'])
median_margin = data['Margin'].median()

above_median_df = data[data['Margin'] > median_margin]
below_median_df = data[data['Margin'] <= median_margin]

above_median_seat_counts = above_median_df['Leading Party'].value_counts().reset_index()
below_median_seat_counts = below_median_df['Leading Party'].value_counts().reset_index()

above_median_seat_counts.columns = ['Leading Party', 'Seats']
below_median_seat_counts.columns = ['Leading Party', 'Seats']

above_median_seat_counts = above_median_seat_counts.sort_values(by='Seats', ascending=False)
below_median_seat_counts = below_median_seat_counts.sort_values(by='Seats', ascending=False)

plt.figure(figsize=(12, 8))
plt.barh(above_median_seat_counts['Leading Party'], above_median_seat_counts['Seats'], color='skyblue')
plt.xlabel('Number of Seats')
plt.ylabel('Party')
plt.title('Number of Seats Won by Each Party with Margins Above the Median')
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(12, 8))
plt.barh(below_median_seat_counts['Leading Party'], below_median_seat_counts['Seats'], color='salmon')
plt.xlabel('Number of Seats')
plt.ylabel('Party')
plt.title('Number of Seats Won by Each Party with Margins Below the Median')
plt.gca().invert_yaxis()
plt.show()

trailing_party_counts = data['Trailing Party'].value_counts().reset_index()
trailing_party_counts.columns = ['Trailing Party', 'Count']

top_7_trailing_parties = trailing_party_counts.head(7)

plt.figure(figsize=(12, 8))
plt.barh(top_7_trailing_parties['Trailing Party'], top_7_trailing_parties['Count'], color='lightcoral')
plt.xlabel('Number of Trailing Candidates')
plt.ylabel('Party')
plt.title('Top 7 Parties with the Most Trailing Candidates')
plt.gca().invert_yaxis()
plt.show()

filtered_data = data[(data['Leading Party'] != 'Bharatiya Janata Party') & (data['Trailing Party'] != 'Bharatiya Janata Party')]

leading_party_counts = filtered_data['Leading Party'].value_counts().reset_index()
trailing_party_counts = filtered_data['Trailing Party'].value_counts().reset_index()

leading_party_counts.columns = ['Party', 'Leading Count']
trailing_party_counts.columns = ['Party', 'Trailing Count']

combined_counts = pd.merge(leading_party_counts, trailing_party_counts, on='Party', how='outer').fillna(0)
combined_counts['Total Seats'] = combined_counts['Leading Count'] + combined_counts['Trailing Count']
combined_counts = combined_counts.sort_values(by='Total Seats', ascending=False)

top_parties = combined_counts.head(10)

plt.figure(figsize=(12, 8))
plt.barh(top_parties['Party'], top_parties['Total Seats'], color='lightblue')
plt.xlabel('Number of Seats')
plt.ylabel('Party')
plt.title('Top Parties with Most Seats (Leading and Trailing Combined, Excluding BJP)')
plt.gca().invert_yaxis()
plt.show()

south_indian_states = ['Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Kerala']

filtered_data = data[data['State'].isin(south_indian_states)]

seat_distribution = filtered_data['Leading Party'].value_counts().reset_index()
seat_distribution.columns = ['Party', 'Seats']

plt.figure(figsize=(12, 8))
plt.pie(seat_distribution['Seats'], labels=seat_distribution['Party'], autopct='%1.1f%%', startangle=140)
plt.title('Seat Distribution in South Indian States (Tamil Nadu, Karnataka, Andhra Pradesh, Telangana, Kerala)')
plt.axis('equal')
plt.show()

middle_indian_states = ['Uttar Pradesh', 'Madhya Pradesh', 'Rajasthan', 'Bihar', 'Jharkhand', 'Haryana', 'Delhi', 'Chhattisgarh']

filtered_data = data[data['State'].isin(middle_indian_states)]

seat_distribution = filtered_data['Leading Party'].value_counts().reset_index()
seat_distribution.columns = ['Party', 'Seats']

plt.figure(figsize=(12, 8))
plt.pie(seat_distribution['Seats'], labels=seat_distribution['Party'], autopct='%1.1f%%', startangle=140)
plt.title('Seat Distribution in Middle Indian States (Uttar Pradesh, Madhya Pradesh, Rajasthan, Bihar, Jharkhand, Haryana, Delhi, Chhattisgarh)')
plt.axis('equal')
plt.show()

state_seat_counts = data['State'].value_counts().reset_index()
state_seat_counts.columns = ['State', 'Seats']

top_5_states = state_seat_counts.head(5)['State'].tolist()

filtered_data = data[data['State'].isin(top_5_states)]

seat_distribution = filtered_data['Leading Party'].value_counts().reset_index()
seat_distribution.columns = ['Party', 'Seats']

plt.figure(figsize=(12, 8))
plt.pie(seat_distribution['Seats'], labels=seat_distribution['Party'], autopct='%1.1f%%', startangle=140)
plt.title('Seat Distribution in Top 5 States with Most Seats')
plt.axis('equal')
plt.show()
