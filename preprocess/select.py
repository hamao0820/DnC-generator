import csv
from typing import NamedTuple
import re


class ConvertedWard(NamedTuple):
    orig: str
    hira: str
    vowel: str


def read_csv(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader][1:]


def to_csv(words: list[ConvertedWard]) -> str:
    csv = "orig,hira,vowel\n"
    return csv + "\n".join([f"{word.orig},{word.hira},{word.vowel}" for word in words])


def save_csv(words: list[ConvertedWard], file_name: str) -> None:
    with open(file_name, "w") as f:
        f.write(to_csv(words))


def select_words(file_path: str, file_name: str, pattern: re.Pattern):
    wards = read_csv(file_path)
    selected_wards: list[ConvertedWard] = []
    for ward in wards:
        if pattern.match(ward[2]):
            selected_wards.append(ConvertedWard(orig=ward[0], hira=ward[1], vowel=ward[2]))

    save_csv(selected_wards, file_name)


if __name__ == "__main__":
    konnan_pattern = r"^o[aiueon]n?a[nu]$"
    konnan_words = select_words(
        "data/preprocessed/meishi_vowel.csv", "data/preprocessed/konnan.csv", re.compile(konnan_pattern)
    )
    bunkatsu_pattern = r"^u[aiueon]?au$"
    bunkatsu_words = select_words(
        "data/preprocessed/meishi_vowel.csv", "data/preprocessed/bunkatsu.csv", re.compile(bunkatsu_pattern)
    )
