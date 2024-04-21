import json
import os

import ollama
from dotenv import load_dotenv

from src.executor.run import CodeRunner
from src.stripe import StripeIntegration

load_dotenv()  # take environment variables from .env.

modelfile = """
FROM llama3
SYSTEM You are a 3rd party SaaS integration code generator. You only generate code and nothing else.
You generate the functions and required data models and nothing else.
Always return json response and never call print() in the code.
"""

ollama.create(model="stripe", modelfile=modelfile)

stripe_client = StripeIntegration("", "stripe")
prompt = stripe_client.fetch_data("Customers", "", "", "3")

output = ollama.generate(
    model="stripe",
    prompt=prompt,
)
response = CodeRunner({"STRIPE_API_KEY": os.environ.get("STRIPE_API_KEY", "")}).run(
    output["response"]
)

response_json = json.loads(response)
response_json = response_json.get("data", [])
for res in response_json:
    customer_id = res['id']
    email = res['email']
    print(f"Customer ID: {customer_id}\nEmail: {email}")
