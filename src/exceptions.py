class InternalServerError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        return f"{self.message}"