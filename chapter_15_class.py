class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        return Point(self.x, -self.y)

    def __str__(self):
        return str((self.x, self.y))

    def slope_from_line(self, other):
        s = (other.y - self.y) / (other.x - self.x)
        return s

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def add(self, other):
        return self + other

    def get_line_to(self, point2):
        a = self.slope_from_line(point2)
        b = self.y - a * self.x
        return (a, b)


p4 = Point(4, 11)
p5 = Point(6, 15)

p6 = p4.slope_from_line(p5)
# print(p6)
p7 = p4.get_line_to(p5)
print(p7)


class SmsStore:
    def __init__(self):
        self.smses = []

    def add_new_arrival(self, from_number, time_arrived, tex_of_SMS):
        self.smses.append([False, from_number, time_arrived, tex_of_SMS])

    def message_count(self):
        return len(self.smses)

    def get_unread_indexes(self):
        result = []
        for i, sms in enumerate(self.smses):
            if not sms[0]:
                result.append(i)
        return result

    def get_message(self, i):
        if i < 0 or i >= len(self.smses):
            return None
        sms = self.smses[i]
        sms[0] = True
        return sms[1:]

    def delete(self, i):
        self.smses = self.smses[:i] + self.smses[i + 1:]

    def clear(self):
        self.smses = []


p = SmsStore(False, 36919, 9, "I love U")
print(p.m)
