from collections import OrderedDict
from typing import Dict, List, Set, Tuple


def main() -> None:

    with open("sample.txt", mode="r") as file:

        file_data: List[str] = [line for line in file]

        print("Number of lines in file: {}".format(sum(1 for i in file_data)))
        print("Number of words in file: {}".format(sum(len(row.split()) for row in file_data)))
        print("Number of characters in file: {}".format(sum(1 for row in file_data for character in row)))

        list_of_words: List[str] = [i.lower() for row in file_data for i in row.split()]  # get list of all words
        list_of_unique_words: Set[str] = set(list_of_words)  # list of unique words
        word_count_tuple: List[Tuple[str, int]] = [
            (word, list_of_words.count(word)) for word in list_of_unique_words
        ]  # tuple of words with word count

        word_count_ordered: Dict[str, int] = {
            word: count for word, count in sorted(word_count_tuple, key=lambda item: item[1], reverse=True)
        }
        word_count_dict: OrderedDict[str, int] = OrderedDict(word_count_ordered)

        print("Number of unique words in file: {}".format(len(list_of_unique_words)))
        print("Occurrence of the top 5 most common word: {}".format(list(word_count_dict.items())[:5]))


if __name__ == "__main__":
    main()
