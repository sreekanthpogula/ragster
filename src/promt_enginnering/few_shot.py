import openai

# Replace with your OpenAI API key
openai.api_key = "YOUR_API_KEY"


def few_shot_prompting(prompt, examples, model="gpt-3.5-turbo", max_tokens=150):
    """
    Implements few-shot prompting using OpenAI's Chat API.

    :param prompt: The user query or prompt string.
    :param examples: A list of (input, output) tuples as few-shot examples.
    :param model: The OpenAI model to use.
    :param max_tokens: Max tokens for the response.
    :return: The model's response string.
    """
    messages = []
    # Add examples as system and assistant messages
    for inp, out in examples:
        messages.append({"role": "user", "content": inp})
        messages.append({"role": "assistant", "content": out})
    # Add the actual prompt
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=0.7,
    )
    return response.choices[0].message["content"].strip()


if __name__ == "__main__":
    # Example few-shot examples
    examples = [
        ("Translate 'Hello' to French.", "Bonjour"),
        ("Translate 'Goodbye' to French.", "Au revoir"),
    ]
    prompt = "Translate 'Thank you' to French."
    result = few_shot_prompting(prompt, examples)
    print("Response:", result)
