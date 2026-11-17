from pathlib import Path


class Book:

    def __init__(self, title: str, text: str, words_per_page: int = 250):
        self.title = title
        self.text = text
        self.words_per_page = words_per_page

    @classmethod
    def from_file(cls, path: str | Path, title: str | None = None):
        path = Path(path)
        text = path.read_text(encoding="utf-8")
        return cls(title or path.stem, text)

    @property
    def words(self) -> list[str]:
        return self.text.split()

    @property
    def word_count(self) -> int:
        return len(self.words)

    @property
    def pages(self) -> int:
        return max(1, self.word_count // self.words_per_page + 1)

    @property
    def sentences(self) -> list[str]:
        import re
        return [s.strip() for s in re.split(r"[.!?]+", self.text) if s.strip()]

    def search(self, query: str) -> list[int]:
        q = query.lower()
        words = [w.lower().strip(".,!?;:«»\"'") for w in self.words]
        return [i for i, w in enumerate(words) if q in w]

    def __repr__(self):
        return f"<Book '{self.title}': {self.word_count} слов, ~{self.pages} стр.>"