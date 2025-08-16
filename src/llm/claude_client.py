import os
import requests


class ClaudeClient:
    def __init__(self, config_path=None):
        self.api_key = self._load_api_key(config_path)
        self.api_url = "https://api.anthropic.com/v1/complete"

    def _load_api_key(self, config_path):
        # Default config path for Claude Desktop
        if config_path is None:
            config_path = os.path.expanduser("~/.claude/desktop_config")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Claude config not found at {config_path}")
        with open(config_path, "r") as f:
            for line in f:
                if line.startswith("api_key="):
                    return line.strip().split("=", 1)[1]
        raise ValueError("API key not found in Claude config.")

    def complete(self, prompt, model="claude-2", max_tokens=256, temperature=0.7):
        headers = {"x-api-key": self.api_key, "content-type": "application/json"}
        payload = {
            "prompt": prompt,
            "model": model,
            "max_tokens_to_sample": max_tokens,
            "temperature": temperature,
            "stop_sequences": ["\n\nHuman:"],
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["completion"]


# Example usage:
# client = ClaudeClient()
# result = client.complete("Hello, Claude!")
# print(result)
