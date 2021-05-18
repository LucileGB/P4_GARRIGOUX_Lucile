from datetime import date
from tinydb import TinyDB, Query

class CheckForm:
    def check_date(input):
        try:
            split_input = input.split("/")
            date_string = f"{split_input[2]}-{split_input[1]}-{split_input[0]}"
            date.fromisoformat(date_string)
        except Exception:
            return False
        return date_string

    def check_gender(gender):
        if gender.lower() in ("homme", "femme"):
            return gender
        else:
            return False

    def check_rank(rank):
        if str(rank).isnumeric():
            return int(rank)
        else:
            return False
