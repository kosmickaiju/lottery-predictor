import pandas as pd
import re

#load csv from scraper
df = pd.read_csv('florida_lottery_top_prizes.csv')

#helper function to extract numeric values
def extract_numeric(value):
    clean_value = re.sub(r'[$,]', '', str(value))
    try:
        return float(clean_value)
    except ValueError:
        return None

#cleaning
df['Top Prize Numeric'] = df['Top Prize'].apply(extract_numeric)
df = df.dropna(subset=['Top Prize Numeric'])  # drop rows without numeric top prizes
df['Top Prize Numeric'] = df['Top Prize Numeric'].astype(int)

df['Top Prizes Remaining'] = df['Top Prizes Remaining'].replace('[,]', '', regex=True).astype(int)
df['Ticket Price'] = df['Ticket Price'].astype(int)

#calculate value score
df['Value Score'] = df['Top Prizes Remaining'] / df['Ticket Price']
df_sorted = df.sort_values(by='Value Score', ascending=False)

print('Top 10 Best Value Scratch-Off Games:')
print(df_sorted[['Game', 'Top Prize', 'Top Prize Numeric', 'Top Prizes Remaining', 'Ticket Price', 'Value Score']].head(10))

#save ranked list
df_sorted.to_csv('ranked_scratch_offs.csv', index=False)
print('✅ Ranked scratch-off games saved to ranked_scratch_offs.csv')