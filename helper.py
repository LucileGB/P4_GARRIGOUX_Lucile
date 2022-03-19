from datetime import date

import views
import texts


class CheckForm:
    def check_date(input):
        """Checks if the date is set to the one accepted format."""
        try:
            split_input = input.split("/")
            date_string = f"{split_input[2]}-{split_input[1]}-{split_input[0]}"
            date.fromisoformat(date_string)
        except Exception:
            return False
        return date_string

    def correct_date(input):
        """Only returns the date once it's correctly inputted."""
        while CheckForm.check_date(input) is False:
            new_date = views.Menu.input_new(texts.Texts.wrong_date)
            new_date = CheckForm.check_date(new_date)
            if new_date is not False:
                return new_date

    def check_gender(gender):
        genders = ("homme", "femme")
        while gender.lower() not in genders:
            new_gender = views.Menu.input_new(texts.Texts.new_gender)
            if new_gender.lower() in genders:
                return new_gender

    def check_number(number):
        while str(number).isnumeric() is False:
            new_number = views.Menu.input_new(texts.Texts.new_number)
            if str(new_number).isnumeric() is True:
                return new_number

    def control_time(number):
        """Once it receives the proper input, returns chosen time control."""
        right_answers = ["1", "2", "3"]
        while number.isnumeric() is False or number not in right_answers:
            print("wrong!")
            number = views.Menu.input_new(texts.Texts.wrong_time_control)
        if str(number).isnumeric() is True and str(number) in right_answers:
            if number == "1":
                result = "Bullet"
            if number == "2":
                result = "Blitz"
            else:
                result = "Coup rapide"
            return result
