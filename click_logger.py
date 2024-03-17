import requests

def log_click(user_id):
    webhook_url = 'https://discord.com/api/webhooks/your_webhook_url_here'
    payload = {'content': f'User {user_id} clicked the link.'}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print('Successfully logged click.')
    else:
        print(f'Failed to log click. Status code: {response.status_code}')

if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    log_click(user_id)  # For Windows
