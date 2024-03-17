import requests

def log_click(url, user_id):
    webhook_url = 'https://discord.com/api/webhooks/1218947479999877151/nloZbM1-6HP8SZkD1illqnEl_vvPUOA2FHXH0hPy9YzJJ-Qec0SSO9MYXeBye7InhQW3'
    payload = {'content': f'User {user_id} clicked the link: {url}'}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print('Successfully logged click.')
    else:
        print(f'Failed to log click. Status code: {response.status_code}')

if __name__ == "__main__":
    url = input("https://example.com ")
    user_id = input("Enter user ID: ")
    log_click(url, user_id)

