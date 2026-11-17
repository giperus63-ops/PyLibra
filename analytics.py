from collections import Counter
from .reader import Book


class TextAnalyzer:

    STOPWORDS = {
        "и", "в", "во", "не", "что", "он", "на", "я", "с", "со", "как",
        "а", "то", "все", "она", "так", "его", "но", "да", "ты", "к",
        "у", "же", "вы", "за", "бы", "по", "только", "ее", "мне",
    }

    def __init__(self, book: Book):
        self.book = book

    def top_words(self, n: int = 10, skip_stopwords: bool = True) -> list[tuple[str, int]]:
        words = [w.lower().strip(".,!?;:«»\"'()") for w in self.book.words]
        words = [w for w in words if len(w) > 2]
        if skip_stopwords:
            words = [w for w in words if w not in self.STOPWORDS]
        return Counter(words).most_common(n)

    @property
    def avg_word_length(self) -> float:
        words = self.book.words
        return sum(len(w) for w in words) / len(words) if words else 0.0

    @property
    def avg_sentence_length(self) -> float:
        sentences = self.book.sentences
        if not sentences:
            return 0.0
        return sum(len(s.split()) for s in sentences) / len(sentences)

    @property
    def readability_score(self) -> float:
        if self.avg_sentence_length == 0:
            return 0.0
        score = 206.835 - 1.015 * self.avg_sentence_length - 60.0 * (
            self.avg_word_length / 4
        )
        return max(0.0, min(100.0, score))

    def summary(self) -> dict:
        return {
            "title": self.book.title,
            "words": self.book.word_count,
            "pages": self.book.pages,
            "avg_word_length": round(self.avg_word_length, 2),
            "avg_sentence_length": round(self.avg_sentence_length, 1),
            "readability": round(self.readability_score, 1),
            "top_words": self.top_words(5),
        }