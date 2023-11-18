import pandas as pd
import pytest

from hockey_scraper.nhl import game_scraper, playing_roster
from hockey_scraper.nhl.pbp import json_pbp

pbp, shifts = game_scraper.scrape_game("2023020251", "2023-11-17", False)

print(pbp)