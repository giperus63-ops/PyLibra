from .analytics import TextAnalyzer
from .tracker import ReadingTracker


class ReportGenerator:

    @staticmethod
    def book_report(analyzer: TextAnalyzer) -> str:
        s = analyzer.summary()
        lines = [
            f"📖 Отчёт по книге: «{s['title']}»",
            "─" * 40,
            f"Слов:              {s['words']:,}",
            f"Страниц (оценка):  {s['pages']}",
            f"Ср. длина слова:   {s['avg_word_length']} симв.",
            f"Ср. длина предл.:  {s['avg_sentence_length']} слов",
            f"Читаемость:        {s['readability']}/100",
            "",
            "Топ-5 слов:",
        ]
        for word, count in s["top_words"]:
            lines.append(f"  • {word}: {count}")
        return "\n".join(lines)

    @staticmethod
    def tracker_report(tracker: ReadingTracker) -> str:
        lines = [
            "📊 Отчёт о чтении",
            "─" * 40,
            f"Сессий:      {len(tracker.sessions)}",
            f"Страниц:     {tracker.total_pages}",
            f"Минут:       {tracker.total_minutes:.0f}",
            f"Скорость:    {tracker.avg_speed:.2f} стр/мин",
        ]
        if tracker.goal_pages:
            lines.append(f"Цель:        {tracker.progress():.1f}% ({tracker.total_pages}/{tracker.goal_pages})")
        lines.append("")
        lines.append("По книгам:")
        for title, pages in tracker.by_book().items():
            lines.append(f"  • {title}: {pages} стр.")
        return "\n".join(lines)