# Claude Camp Week 3 Practices

Three data-processing projects covering file I/O, JSON handling, and unit testing.

## Project 1: CSV Student Data Analyzer
Reads student data from a CSV file, computes statistics (total count, count by country, completion rate), and saves the result to `report.json`.

Run: `python3 csv_analyzer.py`

## Project 2: JSON Config Reader/Writer
Reads settings from `config.json`, lets the user update any setting via command line with validation (font size must be 8-32), and saves changes back.

Run: `python3 config_manager.py`

## Project 3: String Utilities Library
A string utility module with three functions (`reverse_words`, `count_vowels`, `is_palindrome`) and a pytest test suite.

Run tests: `pytest`
