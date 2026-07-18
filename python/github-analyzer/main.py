from github_api import get_profile


def main() -> None:
    username = input("Enter username: ")
    get_profile(username)


if __name__ == "__main__":
    main()
