"""Scoring rules for a user's progress."""

from src.domain.models.progress import ComputeStats
from src.domain.rules.score import add_scores, calculate_score


class TestCalculateScore:
    def test_unattempted_area_scores_zero(self):
        assert calculate_score(ComputeStats()) == 0

    def test_score_is_a_percentage(self):
        assert calculate_score(ComputeStats(total_attempts=4, correct_attempts=3)) == 75


class TestAddScores:
    def test_totals_accumulate_in_place(self):
        running = ComputeStats(total_attempts=2, correct_attempts=1)

        add_scores(running, ComputeStats(total_attempts=3, correct_attempts=3))

        assert running == ComputeStats(total_attempts=5, correct_attempts=4)
