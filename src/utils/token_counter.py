class TokenCounter:
    def __init__(self, input_token_limit: int, output_token_limit: int):
        self.input_token_limit = input_token_limit
        self.output_token_limit = output_token_limit

    def count_tokens(self, text: str) -> int:
        # Simple whitespace tokenizer; replace with LLM-specific tokenizer if needed
        return len(text.split())

    def validate_input(self, text: str) -> bool:
        return self.count_tokens(text) <= self.input_token_limit

    def validate_output(self, text: str) -> bool:
        return self.count_tokens(text) <= self.output_token_limit

    def truncate_input(self, text: str) -> str:
        tokens = text.split()
        if len(tokens) > self.input_token_limit:
            tokens = tokens[: self.input_token_limit]
        return " ".join(tokens)

    def truncate_output(self, text: str) -> str:
        tokens = text.split()
        if len(tokens) > self.output_token_limit:
            tokens = tokens[: self.output_token_limit]
        return " ".join(tokens)


# Example usage:
# counter = TokenCounter(input_token_limit=512, output_token_limit=128)
# valid = counter.validate_input("some input text")
# truncated = counter.truncate_input("some input text")
