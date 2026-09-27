class Student:
    def __init__(self, name: str, show_gradelevel: int):
        self.name = name
        self.show_gradelevel = show_gradelevel

    def promotion(self):
        self.show_gradelevel += 1
        return self.show_gradelevel

    def has_passed(self, score:int):
        if score >= 70:
            return True
        else:
            return False

    def update_name(self, name:str):
        self.name = name
        return self.name

    def is_graduating(self) :
        if self.show_gradelevel == 12:
            return True
        else:
            return False

