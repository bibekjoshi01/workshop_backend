class EmailNotSetError(ValueError):
    def __init__(self):
        super().__init__("The given email must be set")
