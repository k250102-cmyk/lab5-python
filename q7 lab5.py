
import requests
import json
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

try:
    # 1. Send GET request with query parameters
    params = {
        "userId": 1,
        "_limit": 5
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=10
    )

    # 2. Check HTTP response
    response.raise_for_status()

    # 3. Parse JSON into Python objects
    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Invalid API response format")

    # 4. Extract required fields
    processed_data = []

    for item in data:
        record = {
            "id": item["id"],
            "userId": item["userId"],
            "title": item["title"],
            "body_length": len(item["body"])
        }

        processed_data.append(record)

    # 5. Perform simple analysis
    total_records = len(processed_data)

    if total_records > 0:
        average_body_length = (
            sum(item["body_length"] for item in processed_data)
            / total_records
        )

        highest_record = max(
            processed_data,
            key=lambda item: item["body_length"]
        )

        print("Total records:", total_records)
        print("Average body length:", average_body_length)
        print("Longest record ID:", highest_record["id"])
        print("Longest body length:", highest_record["body_length"])

    else:
        print("No records received from API.")

    # 6. Save processed data into JSON file
    with open("processed_data.json", "w", encoding="utf-8") as file:
        json.dump(processed_data, file, indent=4)

    print("Data saved to JSON file.")

    # 7. Save processed data into CSV file
    with open("processed_data.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "userId", "title", "body_length"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)

    print("Data saved to CSV file.")

except requests.exceptions.Timeout:
    print("Error: API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except requests.exceptions.RequestException as e:
    print("API request error:", e)

except (ValueError, KeyError, TypeError) as e:
    print("Invalid API data:", e)

except (OSError, csv.Error) as e:
    print("File operation error:", e)

except json.JSONDecodeError as e:
    print("Invalid JSON data:", e)

else:
    # 8. Read JSON file and verify results
    print("\n--- Verify JSON file ---")

    with open("processed_data.json", "r", encoding="utf-8") as file:
        saved_json = json.load(file)

    print("JSON records:", len(saved_json))
    print("First JSON record:", saved_json[0] if saved_json else "No records")

    # 9. Read CSV file and verify results
    print("\n--- Verify CSV file ---")

    with open("processed_data.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        saved_csv = list(reader)

    print("CSV records:", len(saved_csv))
    print("First CSV record:", saved_csv[0] if saved_csv else "No records")

    # Verify that both files contain the same number of records
    if len(saved_json) == len(saved_csv):
        print("Verification successful: Both files contain the same number of records.")
    else:
        print("Verification failed: Record counts do not match.")

finally:
    print("\nExperiment pipeline finished.")