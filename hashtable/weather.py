"""
create a data structure that contains new york city weather for first few --
days in the month of January. Write a program that can answer following,

1. Filters the data to include only the first week of January (first 7 days).
2. Calculates the average temperature for the first week.
3. Filters the data to include the first 10 days of January.
4. Finds the maximum temperature in the first 10 days.
5. What was the temperature on Jan 9?
6. What was the temperature on Jan 4?

"""


class Weather:
    def __init__(self, size):
        self.size = size
        self.weather = [[] for _ in range(self.size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, sublist in enumerate(self.weather[h]):
            if sublist[0] == key:
                self.weather[h][idx] = (key, val)
                found = True
        if not found:
            self.weather[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for sublist in self.weather[h]:
            if sublist[0] == key:
                return sublist[1]
        raise KeyError(f"Key '{key}' not found")

    def search(self, val):
        for sublist in self.weather:
            for element in sublist:
                if element[1] == val:
                    return True
        return False

    def keys(self):
        keys = []
        for sublist in self.weather:
            for element in sublist:
                keys.append(element[0])
        return keys

    def values(self):
        values = []
        for sublist in self.weather:
            for element in sublist:
                values.append(element[1])
        return values


weather = Weather(15)
weather["Jan 1"] = 27
weather["Jan 2"] = 31
weather["Jan 3"] = 23
weather["Jan 4"] = 34
weather["Jan 5"] = 37
weather["Jan 6"] = 38
weather["Jan 7"] = 29
weather["Jan 8"] = 30
weather["Jan 9"] = 35
weather["Jan 10"] = 35
print(f"1. {weather.values()[:7]}")
print(f"2. {sum(weather.values()[:7])}")
print(f"3. {weather.values()[:10]}")
print(f"4. {max(weather.values()[:7])}")
print(f"5. {weather['Jan 9']}")
print(f"6. {weather['Jan 4']}")
