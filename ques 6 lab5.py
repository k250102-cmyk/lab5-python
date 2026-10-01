
import requests
import json

# Mock REST API for demonstrating CRUD operations
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

try:
    # 1. GET: Retrieve an existing prediction record
    print("\n--- GET Operation ---")

    response = requests.get(BASE_URL + "/1", timeout=10)

    print("Status Code:", response.status_code)
    response.raise_for_status()

    data = response.json()
    print("JSON Response:", json.dumps(data, indent=4))

except requests.exceptions.Timeout:
    print("GET Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("GET Error: Unable to connect to server.")

except requests.exceptions.HTTPError as e:
    print("GET HTTP Error:", e)

except (requests.exceptions.RequestException, ValueError) as e:
    print("GET Error:", e)


try:
    # 2. POST: Send new image prediction data
    print("\n--- POST Operation ---")

    prediction = {
        "title": "Image Prediction",
        "body": json.dumps({
            "image": "cat.jpg",
            "prediction": "cat",
            "confidence": 0.97
        }),
        "userId": 1
    }

    response = requests.post(
        BASE_URL,
        json=prediction,
        timeout=10
    )

    print("Status Code:", response.status_code)
    response.raise_for_status()

    data = response.json()
    print("JSON Response:", json.dumps(data, indent=4))

except requests.exceptions.Timeout:
    print("POST Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("POST Error: Unable to connect to server.")

except requests.exceptions.HTTPError as e:
    print("POST HTTP Error:", e)

except (requests.exceptions.RequestException, ValueError) as e:
    print("POST Error:", e)


try:
    # 3. PUT: Replace/update an existing record
    print("\n--- PUT Operation ---")

    updated_prediction = {
        "id": 1,
        "title": "Updated Image Prediction",
        "body": json.dumps({
            "image": "cat.jpg",
            "prediction": "tiger",
            "confidence": 0.89
        }),
        "userId": 1
    }

    response = requests.put(
        BASE_URL + "/1",
        json=updated_prediction,
        timeout=10
    )

    print("Status Code:", response.status_code)
    response.raise_for_status()

    data = response.json()
    print("JSON Response:", json.dumps(data, indent=4))

except requests.exceptions.Timeout:
    print("PUT Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("PUT Error: Unable to connect to server.")

except requests.exceptions.HTTPError as e:
    print("PUT HTTP Error:", e)

except (requests.exceptions.RequestException, ValueError) as e:
    print("PUT Error:", e)


try:
    # 4. PATCH: Modify selected fields only
    print("\n--- PATCH Operation ---")

    partial_update = {
        "body": json.dumps({
            "image": "cat.jpg",
            "prediction": "cat",
            "confidence": 0.99
        })
    }

    response = requests.patch(
        BASE_URL + "/1",
        json=partial_update,
        timeout=10
    )

    print("Status Code:", response.status_code)
    response.raise_for_status()

    data = response.json()
    print("JSON Response:", json.dumps(data, indent=4))

except requests.exceptions.Timeout:
    print("PATCH Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("PATCH Error: Unable to connect to server.")

except requests.exceptions.HTTPError as e:
    print("PATCH HTTP Error:", e)

except (requests.exceptions.RequestException, ValueError) as e:
    print("PATCH Error:", e)


try:
    # 5. DELETE: Remove an existing record
    print("\n--- DELETE Operation ---")

    response = requests.delete(
        BASE_URL + "/1",
        timeout=10
    )

    print("Status Code:", response.status_code)
    response.raise_for_status()

    if response.text.strip():
        try:
            data = response.json()
            print("JSON Response:", json.dumps(data, indent=4))
        except ValueError:
            print("Response:", response.text)
    else:
        print("Record deleted successfully. No JSON body returned.")

except requests.exceptions.Timeout:
    print("DELETE Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("DELETE Error: Unable to connect to server.")

except requests.exceptions.HTTPError as e:
    print("DELETE HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("DELETE Error:", e)