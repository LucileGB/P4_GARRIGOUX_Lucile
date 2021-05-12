class CheckForms:
    def check_text(text):
        if len(text) > 0:
            return True
        else:
            return False

    def check_names(name):
        if len(str(name)) > 0:
            for letter in str(name):
                if letter.isnumeric():
                    return False
            return str(name)
        else:
            return False

    def check_date(input):
        try:
            split_input = str(input).split("/")
            date_string = f"{split_input[2]}-{split_input[1]}-{split_input[0]}"
            date.fromisoformat(date_string)
        except Exception:
            return False
        return date_string

    def check_rank(rank):
        if str(rank).isnumeric() and int(rank) > 0:
            return int(rank)
        else:
            return False

    def check_gender(gender):
        if str(gender).lower() in ("homme", "femme"):
            return str(gender)
        else:
            return False

    def check_string(string):
        if len(str(string)) > 0:
            return str(string)
        else:
            return False

    def check_player(self, data):
        first_name = self.check_names(data[0])
        last_name = self.check_names(data[1])
        birth_date = self.check_date(data[2])
        gender = self.check_gender(data[3])
        rank = self.check_rank(data[4])
        result = (first_name, last_name, birth_date, gender, rank)
        for bit in result:
            if bit == False:
                return False
        return result
