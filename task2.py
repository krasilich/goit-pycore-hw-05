from typing import Iterable, Optional


def create_word_finder(text: str) -> callable:
    """
    Create a function that finds the next word in the text.
    Word is considered a sequence of characters between spaces.
    :param text:
    :return:
    """
    text_position = 0
    text_len = len(text)

    def get_next_word() -> Optional[str]:
        """
        Get the next word from the text.
        Returns None if no more words are found.
        :return: str
        """
        nonlocal text_position

        if text_position >= text_len:
            return None

        word = ''
        while text_position < text_len and text[text_position] != ' ':
            word += text[text_position]
            text_position += 1
        text_position += 1
        return word

    return get_next_word


def generator_numbers(text: str) -> Iterable[float]:
    """
     Go over the text and yield a number once found.
     Uses a closure to seek over the text for next word.
     This allows to use only one copy of the text unlike text.split() or similar
     which duplicates the text in memory.
    :param text: str
    :return: generator
    """
    get_next_word = create_word_finder(text)
    while True:
        word = get_next_word()

        if word is None:
            break

        try:
            number = float(word)
            yield number
        except ValueError:
            pass


def sum_profit(text: str, generator: callable) -> float:
    """
    Calculate the sum of all numbers in the text.
    :param text: str
    :param generator: callable
    :return: float
    """
    profit = 0
    for number in generator(text):
        profit += number
    return profit
