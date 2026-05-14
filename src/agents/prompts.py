SYSTEM_PROMPT = """
You are a professional AI engineering assistant.
Answer using retrieved context when available.
If context is weak, say what is missing and provide a careful general answer.
Keep answers structured, practical, and implementation-focused.
"""

ANSWER_TEMPLATE = """
Question: {query}

Retrieved Context:
{context}

Tool Output:
{tool_output}

Final Answer:
"""
