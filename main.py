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
"""

ollama.create(model="saas_man", modelfile=modelfile)

stripe_client = StripeIntegration("", "llama3")
prompt = stripe_client.fetch_data(
    "Subscriptions", "customer:john;price:1200;status:done;", "", "3"
)

output = ollama.generate(
    model="saas_man",
    prompt=prompt,
)
CodeRunner({"STRIPE_API_KEY": os.environ.get("STRIPE_API_KEY", "")}).run(
    output["response"]
)
