from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from typing import NamedTuple
from time import sleep


class Word(NamedTuple):
    word: str
    url: str


def to_csv(words: list[Word]) -> str:
    csv = "word,url\n"
    return csv + "\n".join([f"{w.word},{w.url}" for w in words])


def save_csv(words: list[Word], file_name: str) -> None:
    with open(file_name, "w") as f:
        f.write(to_csv(words))


def collect_words(url: str, file_name: str):
    words: list[Word] = []

    driver.get(url)
    page_num = 1
    while True:
        print(f"page {page_num}")
        lis = driver.find_elements(By.CSS_SELECTOR, "#mw-pages .mw-category ul li")
        for li in lis:
            word = li.text
            href = li.find_element(By.TAG_NAME, "a").get_attribute("href")
            words.append(Word(word, href))

        sleep(3)
        try:
            next_page = driver.find_element(By.LINK_TEXT, "次のページ")
            if next_page:
                next_page.click()
            else:
                break
        except NoSuchElementException:
            break
        page_num += 1

    save_csv(words, file_name)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    sahenUrl = "https://ja.wiktionary.org/w/index.php?title=カテゴリ:日本語_名詞_サ変動詞&from=あ"
    collect_words(sahenUrl, "data/scraped/sahen.csv")

    meishiUrl = "https://ja.wiktionary.org/w/index.php?title=カテゴリ:日本語_名詞&from=あ"
    collect_words(meishiUrl, "data/scraped/meishi.csv")

    driver.quit()
