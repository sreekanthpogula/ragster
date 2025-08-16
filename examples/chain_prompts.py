# chain_prompts.py


def chain_prompts(prompts, initial_input):
    """
    Chains a list of prompt functions together.
    Each prompt function takes the output of the previous as input.
    :param prompts: List of functions.
    :param initial_input: Initial input to the first prompt.
    :return: Final output after all prompts.
    """
    output = initial_input
    for prompt in prompts:
        output = prompt(output)
    return output


# Example prompt functions
def prompt1(text):
    return f"Step 1 processed: {text}"


def prompt2(text):
    return f"Step 2 processed: {text}"


def prompt3(text):
    return f"Step 3 processed: {text}"


if __name__ == "__main__":
    prompts = [prompt1, prompt2, prompt3]
    initial_input = "Hello, world!"
    result = chain_prompts(prompts, initial_input)
    print(result)
