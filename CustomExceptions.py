class DuplicateTweetError(Exception):
    pass

class Set_duplicate_detector(set):
    count = 0

    def add(self, value):
        if value in self:
            self.count += 1
            raise DuplicateTweetError()
        super().add(value)