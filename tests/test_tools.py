from src.tools.basic_tools import safe_calculator


def test_safe_calculator():
    assert safe_calculator("2+3") == "5"


def test_safe_calculator_blocks_bad_input():
    assert "Invalid" in safe_calculator("import os")
