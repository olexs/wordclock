class SentenceGenerator:
    minutes = {
        0:  ["uhr"],
        5:  ["fünf", "nach"],
        10: ["zehn", "nach"],
        15: ["viertel", "nach"],
        20: ["zwanzig", "nach"],
        25: ["fünf", "vor", "halb"],
        30: ["halb"],
        35: ["fünf", "nach", "halb"],
        40: ["zwangig", "vor"],
        45: ["viertel", "vor"],
        50: ["zehn", "vor"],
        55: ["fünf", "vor"],
        60: ["uhr"]
    }

    hours = {
        0: "zwölf",
        1: "eins",
        2: "zwei",
        3: "drei",
        4: "vier",
        5: "fünf2",
        6: "sechs",
        7: "sieben",
        8: "acht",
        9: "neun",
        10: "zehn2",
        11: "elf"
    }

    prefix = ["es", "ist"]

    def get_sentence(self, time):
        minutesRounded = round(time.minute / 5) * 5
        minutes = self.minutes[minutesRounded]

        hoursRounded = time.hour % 12
        if minutesRounded >= 25:
            hoursRounded = (hoursRounded + 1) % 12
        hours = [self.hours[hoursRounded]]

        return self.prefix + minutes + hours
        