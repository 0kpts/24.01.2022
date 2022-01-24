def replace_o(word: str) -> None:
    try:
        return word.lower().replace("o", "%")
    except Exception as _ex:
        return None

if __name__ == "__main__":
    print(replace_o("123ooo123"))
