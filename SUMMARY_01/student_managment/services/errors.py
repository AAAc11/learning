class InvalidAgeError(Exception):
    def __init__(self, age, message = "Incorrect age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return (f"{self.message}: {self.age}")
