def send_message(msg):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': msg}
    
    # Make the GET request and capture the response
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
    
    return response.json()  # Return JSON response for further processing or debugging