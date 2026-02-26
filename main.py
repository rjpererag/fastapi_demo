from datetime import datetime


def print_name_with_date(name: str, time_format: str = "%Y-%m-%d") -> None:
    now_str = datetime.now().strftime(time_format)
    print(f"Hello {name}, today is : {now_str}")


def main() -> None:
    print_name_with_date(name="Jon Doe")


if __name__ == "__main__":
    main()
