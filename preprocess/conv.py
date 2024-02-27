import pykakasi
import csv
from typing import NamedTuple

kks = pykakasi.kakasi()


class ConvertedWard(NamedTuple):
    orig: str
    hira: str
    kana: str
    hepburn: str
    kunrei: str
    passport: str


def read_csv(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader]


def to_csv(words: list[ConvertedWard]) -> str:
    csv = "orig,hira,kana,hepburn,kunrei,passport\n"
    return csv + "\n".join(
        [f"{word.orig},{word.hira},{word.kana},{word.hepburn},{word.kunrei},{word.passport}" for word in words]
    )


def save_csv(words: list[ConvertedWard], file_name: str) -> None:
    with open(file_name, "w") as f:
        f.write(to_csv(words))


def convert_wards(file_path: str, file_name: str) -> ConvertedWard:
    wards = read_csv(file_path)
    converted_wards: list[ConvertedWard] = []
    for ward in wards:
        res = kks.convert(ward[0])
        if not len(res) == 1:
            continue
        res = ConvertedWard(
            orig=ward[0],
            hira=res[0]["hira"],
            kana=res[0]["kana"],
            hepburn=res[0]["hepburn"],
            kunrei=res[0]["kunrei"],
            passport=res[0]["passport"],
        )
        converted_wards.append(res)

    save_csv(converted_wards, file_name)


if __name__ == "__main__":
    convert_wards("data/scraped/sahen.csv", "data/preprocessed/sahen_kakasi.csv")
    convert_wards("data/scraped/meishi.csv", "data/preprocessed/meishi_kakasi.csv")
