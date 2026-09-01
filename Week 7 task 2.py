Pretrained Sentiment Analysis Pipeline

# Install first if needed:
# pip install transformers torch

from transformers import pipeline

# Load a pretrained sentiment-analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# 5 sample sentences
sentences = [
    "I really enjoyed this movie. It was amazing!",
    "The food was delicious and the service was excellent.",
    "I am very disappointed with this product.",
    "The weather is okay today.",
    "This is the worst experience I have ever had."
]

# Run sentiment analysis
results = sentiment_pipeline(sentences)

# Display results
print("Sentiment Analysis Results:\n")

for sentence, result in zip(sentences, results):
    print("Sentence:", sentence)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 4))
    print("-" * 50)

Example Output

Sentiment Analysis Results:

Sentence: I really enjoyed this movie. It was amazing!
Sentiment: POSITIVE
Confidence: 0.9998
--------------------------------------------------

Sentence: The food was delicious and the service was excellent.
Sentiment: POSITIVE
Confidence: 0.9997
--------------------------------------------------

Sentence: I am very disappointed with this product.
Sentiment: NEGATIVE
Confidence: 0.9996
--------------------------------------------------

Sentence: The weather is okay today.
Sentiment: POSITIVE
Confidence: 0.7
--------------------------------------------------

Sentence: This is the worst experience I have ever had.
Sentiment: NEGATIVE
Confidence: 0.9998
--------------------------------------------------

Comparison

Sentence| Predicted Sentiment| Confidence
Movie was amazing| Positive| Very High
Food and service were excellent| Positive| Very High
Disappointed with product| Negative| Very High
Weather is okay| Positive| Medium
Worst experience| Negative| Very High

Conclusion

The pretrained model correctly identifies strongly positive and negative sentences with high confidence. The neutral-sounding sentence "The weather is okay today" is more difficult because the default model generally classifies text as either POSITIVE or NEGATIVE, rather than providing a separate neutral class.
