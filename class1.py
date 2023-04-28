class Hello:
    def __init__(self, str):
        self.str = str

class annyong(Hello):
    def __init__(self, str):
        super().__init__(str)
