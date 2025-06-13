def get_average_grade(self, ortacha_baho):
        self.ortacha_baho = sum(self.grades) // self.courses
        return self.ortacha_baho
    def __str__(self):
       