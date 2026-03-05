class Battery:

    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.level = 500

    def update(self, input_power, load):
        self.level += input_power - load

        if self.level > self.capacity:
            self.level = self.capacity

        if self.level < 0:
            self.level = 0

    def percentage(self):
        return round((self.level / self.capacity) * 100, 2)