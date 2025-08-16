import openai


class GPTClient:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def generate_response(
        self, prompt: str, max_tokens: int = 150, temperature: float = 0.7
    ) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message["content"].strip()


# Example usage:
# client = GPTClient(api_key="your-openai-api-key")
# reply = client.generate_response("Hello, how are you?")
# print(reply)
