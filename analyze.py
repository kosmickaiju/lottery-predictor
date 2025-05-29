import pandas as pd

df = pd.read_csv('florida_lottery_top_prizes.csv')

df['Top Prize'] = df['Top Prize'].replace('[\$,]', '', regex=True).astype(int)
df['Top Prizes Remaining'] = df['Top Prizes Remaining'].replace('[,]', '', regex=True).astype(int)
df['Ticket Price'] = df['Ticket Price'].replace('[\$,]', '', regex=True).astype(int)

df['Value Score'] = df['Top Prizes Remaining'] / df['Ticket Price']
df_sorted = df.sort_values(by='Value Score', ascending=False)

print('Top 10 Best Value Scratch-Off Games:')
print(df_sorted[['Game', 'Top Prize', 'Top Prizes Remaining', 'Ticket Price', 'Value Score']].head(10))

df_sorted.to_csv('ranked_scratch_offs.csv', index=False)
print('✅ Ranked scratch-off games saved to ranked_scratch_offs.csv')