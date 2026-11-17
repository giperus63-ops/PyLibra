from dataclasses import dataclass, field
from datetime import date


@dataclass
class ReadingSession:
    book_title: str
    pages_read: int
    minutes: float
    date: date = field(default_factory=date.today)

    @property
    def pages_per_minute(self) -> float:
        return self.pages_read / self.minutes if self.minutes else 0.0


class ReadingTracker:

    def __init__(self):
        self.sessions: list[ReadingSession] = []
        self.goal_pages: int | None = None

    def log(self, book_title: str, pages: int, minutes: float):
        self.sessions.append(ReadingSession(book_title, pages, minutes))

    def set_goal(self, pages: int):
        self.goal_pages = pages

    @property
    def total_pages(self) -> int:
        return sum(s.pages_read for s in self.sessions)

    @property
    def total_minutes(self) -> float:
        return sum(s.minutes for s in self.sessions)

    @property
    def avg_speed(self) -> float:
        return self.total_pages / self.total_minutes if self.total_minutes else 0.0

    def progress(self) -> float:
        if not self.goal_pages:
            return 0.0
        return min(100.0, self.total_pages / self.goal_pages * 100)

    def by_book(self) -> dict[str, int]:
        result: dict[str, int] = {}
        for s in self.sessions:
            result[s.book_title] = result.get(s.book_title, 0) + s.pages_read
        return result