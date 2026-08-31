# Install first if needed:
# pip install transformers

from transformers import AutoTokenizer

# Sample paragraph
paragraph = """
Artificial Intelligence is changing the world. Machine learning helps
computers learn from data and make predictions.
"""

# --------------------------------------------------
# 1. Manual Tokenization
# --------------------------------------------------

# Convert text to lowercase
text = paragraph.lower()

# Remove punctuation
punctuation = ".,!?;:\"'()-"
for symbol in punctuation:
    text = text.replace(symbol, "")

# Split text into words
manual_tokens = text.split()

print("Manual Tokens:")
print(manual_tokens)
print("Number of Manual Tokens:", len(manual_tokens))


# --------------------------------------------------
# 2. Hugging Face Tokenization
# --------------------------------------------------

# Load a pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the same paragraph
hf_tokens = tokenizer.tokenize(paragraph)

print("\nHugging Face Tokens:")
print(hf_tokens)
print("Number of Hugging Face Tokens:", len(hf_tokens))


# --------------------------------------------------
# 3. Compare Results
# --------------------------------------------------

print("\nComparison:")
print("Manual token count:", len(manual_tokens))
print("Hugging Face token count:", len(hf_tokens))

print("\nManual tokenization treats each word as a token.")
print("Hugging Face uses subword tokenization, so some words")
print("may be divided into smaller pieces.")
