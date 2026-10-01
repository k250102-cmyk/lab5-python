
import requests

# Public sentiment-analysis API
url = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# Input information
text = "I love learning Python programming!"

# Query parameters
params = {
    "text": text
}

try:
    # Send GET request
    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    # Check HTTP status code
    response.raise_for_status()

    # Convert JSON response into Python objects
    data = response.json()

    # Validate and extract prediction information
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Invalid or empty API response.")

    prediction = data[0]

    if not isinstance(prediction, dict):
        raise ValueError("Unexpected response format.")

    label = prediction.get("label")
    confidence = prediction.get("score")

    if label is None or confidence is None:
        raise ValueError("Prediction or confidence score is missing.")

    # Display results
    print("Input Text:", text)
    print("Prediction:", label)
    print("Confidence Score:", round(confidence, 4))

except requests.exceptions.Timeout:
    print("Error: The API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API.")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    print("The API could not provide the requested result.")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except (ValueError, TypeError) as e:
    print("Invalid API response:", e)

except Exception as e:
    print("Unexpected error:", e)