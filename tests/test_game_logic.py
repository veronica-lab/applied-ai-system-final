import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess


def test_win():
    outcome, msg = check_guess(5, 5)
    assert outcome == "Win"


def test_too_high():
    outcome, msg = check_guess(10, 5)
    assert outcome == "Too High"


def test_too_low():
    outcome, msg = check_guess(2, 5)
    assert outcome == "Too Low"