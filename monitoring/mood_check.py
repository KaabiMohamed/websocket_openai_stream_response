from textblob import TextBlob


def estimate_mood(message: str) -> float:
    """
    Estimates the mood of a given message by analyzing its sentiment polarity.

    Args:
        message (str): The message text to analyze.

    Returns:
        float: The sentiment polarity of the message, indicating its mood. A higher value
               indicates a more positive mood, while a lower value indicates a more negative
               mood.

    Examples:
        >>> estimate_mood("I feel good today!")
        0.5  # Example of a positive sentiment

        >>> estimate_mood("I feel depressed.")
        -0.8  # Example of a negative sentiment
    """
    blob = TextBlob(message)
    return blob.sentiment.polarity
