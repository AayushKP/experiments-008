import requests


def get_profile(username: str) -> dict:

    try:
        response = requests.get(f"https://api.github.com/users/{username}")

        if response.status_code == 404:
            print("User not found")
            return {}

        data = response.json()

        return {
            "name": data.get("name"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "public_repos": data.get("public_repos"),
            "created_at": data.get("created_at"),
        }

    except requests.exceptions.RequestException as e:
        print(e)
        return {}
