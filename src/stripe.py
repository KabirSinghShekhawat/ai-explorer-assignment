from enum import Enum
from src.executor.run import CodeRunner
import ollama


class StripeAPIs(Enum):
    SUBSCRIPTIONS = "subscriptions"
    INVOICES = "invoices"
    CUSTOMERS = "customers"
    REFUNDS = "refunds"


class StripeIntegration:
    def __init__(self, stripe_secret: str, model: str = "llama3") -> None:
        if not stripe_secret:
            raise Exception("Stripe secret is required!")
        self.stripe_secret = stripe_secret
        self.model = model

    def fetch_data(self, data_type: str, filter_by: str, sort_by: str, limit: str):
        prompt = f"""
        Write a python script to fetch {data_type} from Stripe
        {'AND apply these filters if possible: ' + filter_by if filter_by else ' '}
        {'AND sort by these if possible: ' + sort_by if sort_by else ' '}
        {'AND limit records to ' + limit if limit else ' '}.
        The API key is in `os.environ.get('STRIPE_API_KEY')`.
        Only write code. Do not explain anything.
        Add error handling code, return the response from stripe API directly.
        Wrap all code in <code></code> blocks.
        """
        return prompt

    def call(self, api_name: StripeAPIs, filters: str, sort_by: str, limit: int):
        """Call Stripe APIs (read-only) for Customers, Invoices, Subscriptions, Refunds.

        Args:
            api_name (StripeAPIs): Valid API enum type.
            filters (str): List of filters or required API params. eg: 'customer:{customer_id};'
            sort_by (str): Key to sort by.
            limit (int): Number of records to return.

        https://docs.stripe.com/api/subscriptions/list
        https://docs.stripe.com/api/invoices/list
        https://docs.stripe.com/api/customers/list
        https://docs.stripe.com/api/refunds/list
        """
        prompt = self.fetch_data(api_name.value, filters, sort_by, str(limit))
        output = ollama.generate(
            model=self.model,
            prompt=prompt,
        )
        response_json = CodeRunner({"STRIPE_API_KEY": self.stripe_secret}).run(
            output["response"]
        )
        data = response_json.get("data", [])
        return data
