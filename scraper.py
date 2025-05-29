import requests
import pandas as pd

api_url = 'https://apim-website-prod-eastus.azure-api.net/scratchgamesapp/getTopPrizesRemaining'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    games = []
    ticket_prices = []
    top_prizes = []
    top_remaining = []

    for item in data:
        game_name = item.get('GameName', 'N/A')
        ticket_price = item.get('TicketPrice', 0)
        
        if item.get('TopPrizes') and isinstance(item['TopPrizes'], list) and len(item['TopPrizes']) > 0:
            top_prize_info = item['TopPrizes'][0]  # Assuming first prize is the top one
            top_prize = top_prize_info.get('TopPrize', 'N/A').strip()
            top_remaining_str = top_prize_info.get('TopPrizesRemaining', '0 of 0').strip()
            top_remaining_count = top_remaining_str.split('of')[0].strip()
        else:
            top_prize = 'N/A'
            top_remaining_count = '0'
        
        games.append(game_name)
        ticket_prices.append(ticket_price)
        top_prizes.append(top_prize)
        top_remaining.append(top_remaining_count)

    df = pd.DataFrame({
        'Game': games,
        'Ticket Price': ticket_prices,
        'Top Prize': top_prizes,
        'Top Prizes Remaining': top_remaining
    })

    df.to_csv('florida_lottery_top_prizes.csv', index=False)
    print('✅ Data saved to florida_lottery_top_prizes.csv')
else:
    print(f'❌ Failed to fetch data. Status code: {response.status_code}')