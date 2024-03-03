import csv
from typing import NamedTuple
import random


class ConvertedWard(NamedTuple):
    orig: str
    hira: str
    vowel: str


def read_csv(file_path: str) -> list[ConvertedWard]:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [ConvertedWard(orig=row[0], hira=row[1], vowel=row[2]) for row in reader][1:]


if __name__ == "__main__":
    konnan_words = read_csv("data/preprocessed/konnan.csv")
    bunkatsu_words = read_csv("data/preprocessed/bunkatsu.csv")
    for _ in range(5):
        konnan = random.choice(konnan_words)
        bunkatsu = random.choice(bunkatsu_words)
        print("--------------------")
        print(f"{konnan.orig} は {bunkatsu.orig}せよ")
        print(f"{konnan.hira} は {bunkatsu.hira}せよ")
