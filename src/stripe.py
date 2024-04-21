class StripeIntegration:
    def __init__(self, stripe_secret: str, model) -> None:
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
