from typing import Optional


def test(text: Optional[str]):
    if text:
        print(text)


if __name__ == "__main__":
    test(None)
    test("Hello!")
