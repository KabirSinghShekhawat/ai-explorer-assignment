from src.executor.parse import extract_code_block

block = """
<code>
import os
import requests

stripe_api_key = os.environ.get('STRIPE_API_KEY')

url = 'https://api.stripe.com/v1/subscriptionss'
params = {
    'customer': 'john',
    'price': 12000,
    'status': 'done',
    'limit': 3
}

headers = {
    'Authorization': f'Bearer {stripe_api_key}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.get(url, params=params, headers=headers)

data = response.json()

print(data)
</code>
"""


if __name__ == "__main__":
    exec(extract_code_block(block))
