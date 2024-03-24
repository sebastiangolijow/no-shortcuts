import re
from math import ceil


class ArticleReadTimeEngine:
    @staticmethod
    def word_count(text):
        words = re.findall(r"\w+", text)
        return len(words)

    @staticmethod
    def estimate_reading_time(
        article, words_per_minute=250, second_per_image=10, secondes_per_tag=2
    ):
        word_count_body = ArticleReadTimeEngine.word_count(article.body)
        word_count_title = ArticleReadTimeEngine.word_count(article.title)
        word_count_description = ArticleReadTimeEngine.word_count(article.description)

        total_word_count = word_count_body + word_count_description + word_count_title

        reading_time = total_word_count / words_per_minute

        if article.banner_image:
            reading += second_per_image / 60

        tag_count = article.tags.count()
        reading_time += tag_count * secondes_per_tag / 60

        reading_time = ceil(reading_time)

        return reading_time
