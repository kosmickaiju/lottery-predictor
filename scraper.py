### Updated scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://floridalottery.com/games/scratch-offs/top-remaining-prizes'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

games, top_prizes, top_remaining, ticket_prices = [], [], [], []

topprizes_div = soup.find('div', class_='topprizes')
if topprizes_div:
    table = topprizes_div.select_one('table')
    if table:
        rows = table.find_all('tr')[1:]  # skip header row
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                games.append(cols[0].get_text(strip=True))
                top_prizes.append(cols[1].get_text(strip=True))
                top_remaining.append(cols[2].get_text(strip=True).split(' of ')[0])  # extract remaining count
                ticket_prices.append(cols[3].get_text(strip=True))

        df = pd.DataFrame({
            'Game': games,
            'Top Prize': top_prizes,
            'Top Prizes Remaining': top_remaining,
            'Ticket Price': ticket_prices
        })

        df.to_csv('florida_lottery_top_prizes.csv', index=False)
        print('✅ Data saved to florida_lottery_top_prizes.csv')
    else:
        print('❌ Table not found inside topprizes div.')
else:
    print('❌ Topprizes div not found.')