import csv
from typing import NamedTuple
import re


class WordVowel(NamedTuple):
    orig: str
    hira: str
    vowel: str


def read_csv(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader][1:]


def to_csv(words: list[WordVowel]) -> str:
    csv = "orig,hira,vowel\n"
    return csv + "\n".join([f"{word.orig},{word.hira},{word.vowel}" for word in words])


def save_csv(words: list[WordVowel], file_name: str) -> None:
    with open(file_name, "w") as f:
        f.write(to_csv(words))


vowels = ["a", "i", "u", "e", "o", "n"]
pattern = r"[^aiueon]"
repatter = re.compile(pattern)


def convert_wards(file_path: str, file_name: str) -> WordVowel:
    words = read_csv(file_path)
    vowel_words: list[WordVowel] = []

    for word in words:
        # 母音だけを抽出
        hepburn = repatter.sub("", word[3])
        vowel_words.append(WordVowel(orig=word[0], hira=word[1], vowel=hepburn))

    save_csv(vowel_words, file_name)


if __name__ == "__main__":
    convert_wards("data/preprocessed/sahen_kakasi.csv", "data/preprocessed/sahen_vowel.csv")
    convert_wards("data/preprocessed/meishi_kakasi.csv", "data/preprocessed/meishi_vowel.csv")
