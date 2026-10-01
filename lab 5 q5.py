
import requests
import json
import csv

try:
    # Get search query from user
    query = input("Enter a keyword to search: ")
    limit = int(input("Enter number of results: "))

    if limit <= 0:
        raise ValueError("Number of results must be positive.")

    # Send GET request with query parameters
    url = "https://hn.algolia.com/api/v1/search"
    params = {
        "query": query,
        "tags": "story",
        "hitsPerPage": limit
    }

    response = requests.get(url, params=params, timeout=10)

    # Check HTTP status
    response.raise_for_status()

    # Parse JSON into Python dictionary
    data = response.json()

    if not isinstance(data, dict) or not isinstance(data.get("hits"), list):
        raise ValueError("Invalid JSON response from API.")

    results = []

    # Extract relevant fields
    for item in data["hits"]:
        text = item.get("title") or item.get("story_text")

        if not text:
            continue

        record = {
            "text": text,
            "author": item.get("author", "Unknown"),
            "source": "Hacker News",
            "url": item.get("url", ""),
            "created_at": item.get("created_at", ""),
            "points": item.get("points", 0)
        }

        results.append(record)

    if not results:
        print("No text results found for this query.")
    else:
        # Display retrieved results
        for i, item in enumerate(results, start=1):
            print("\nResult", i)
            print("Text:", item["text"])
            print("Author:", item["author"])
            print("Source:", item["source"])
            print("URL:", item["url"])
            print("Date:", item["created_at"])
            print("Points:", item["points"])

        # Save data to JSON file
        with open("nlp_data.json", "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4, ensure_ascii=False)

        # Save data to CSV file
        with open("nlp_data.csv", "w", newline="", encoding="utf-8") as file:
            fields = [
                "text", "author", "source",
                "url", "created_at", "points"
            ]

            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(results)

        print("\nData saved to nlp_data.json and nlp_data.csv")

except requests.exceptions.Timeout:
    print("Error: The request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

except (ValueError, TypeError) as e:
    print("Invalid input or API response:", e)

except (OSError, csv.Error) as e:
    print("File error:", e)