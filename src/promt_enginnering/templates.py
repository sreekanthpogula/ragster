# templates.py

# Example prompt templates using prompt and context engineering best practices

# 1. Clear instruction, context, and expected output
SUMMARIZE_PROMPT = """
You are an expert summarizer.
Context:
{text}

Task:
Summarize the above context in 3 concise sentences.
"""

# 2. Role specification, input, and output format
QA_PROMPT = """
You are a helpful assistant.
Given the following context, answer the user's question.

Context:
{context}

Question:
{question}

Answer (in 2-3 sentences):
"""

# 3. Step-by-step reasoning
REASONING_PROMPT = """
You are a logical reasoning assistant.
Task: Analyze the following problem step by step and provide a clear solution.

Problem:
{problem}

Step-by-step solution:
"""

# 4. Extraction template
EXTRACTION_PROMPT = """
Extract the following information from the text below:
- Names of people
- Dates mentioned
- Locations

Text:
{text}

Extracted Information (in JSON format):
"""

# 5. Rewriting template
REWRITE_PROMPT = """
You are a professional editor.
Task: Rewrite the following text to be more formal and concise.

Original Text:
{text}

Rewritten Text:
"""