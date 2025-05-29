import pandas as pd
import streamlit as st

df = pd.read_csv('ranked_scratch_offs.csv')

st.title('🎯 Florida Scratch-Off Analyzer')
st.write('Top Scratch-Off Games Ranked by Value Score')

st.dataframe(df[['Game', 'Top Prize', 'Top Prizes Remaining', 'Ticket Price', 'Value Score']].head(20))

min_price = st.slider('Minimum Ticket Price', min_value=1, max_value=50, value=1)
filtered_df = df[df['Ticket Price'] >= min_price]

st.write(f'Games with Ticket Price >= ${min_price}')
st.dataframe(filtered_df.head(20))