import os

import ollama
from dotenv import load_dotenv

from src.stripe import StripeAPIs, StripeIntegration

load_dotenv()  # take environment variables from .env.

modelfile = """
FROM llama3
SYSTEM You are a 3rd party SaaS integration code generator. You only generate code and nothing else.
You generate the functions and required data models and nothing else.
Always return json response and never call print() in the code.
"""

ollama.create(model="stripe", modelfile=modelfile)

stripe_client = StripeIntegration(os.environ.get("STRIPE_API_KEY", ""), "stripe")
response_data = stripe_client.call(StripeAPIs.CUSTOMERS, "", "", "3")

if not response_data:
    print("No response returned.")
    exit(1)

first_customer = response_data.pop()
customer_id = first_customer.get("id", None)
if customer_id is None:
    raise Exception("customer ID missing.")

print(first_customer)
