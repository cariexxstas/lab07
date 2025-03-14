class Duration:
    def __init__(self, hours: int, minutes: int):
        self.__hours = hours
        self.__minutes = minutes
    
    def get_total_minutes(self):
        return self.__hours * 60 + self.__minutes
    
    def __add__(self, minutes):
        total_minutes = self.get_total_minutes() + minutes
        return Duration(total_minutes // 60, total_minutes % 60)
    
    def __str__(self):
        return f"{self.__hours:02}:{self.__minutes:02}"

class PreciseDuration(Duration):
    def __init__(self, hours: int, minutes: int, seconds: int):
        super().__init__(hours, minutes)
        self.__seconds = seconds
    
    def get_total_hours(self):
        return self.get_total_minutes() / 60 + self.__seconds / 3600
    
    def __lt__(self, other):
        return self.get_total_hours() < other.get_total_hours()
    
    def __str__(self):
        return f"{super().__str__()}:{self.__seconds:02}"

def read_durations_from_file(filename):
    durations = []
    names = []
    with open(filename, 'r') as file:
        for line in file:
            name, h, m, s = line.strip().split(', ')
            durations.append(PreciseDuration(int(h), int(m), int(s)))
            names.append(name)
    return names, durations

def analyze_durations(durations):
    total_duration = sum(d.get_total_minutes() for d in durations)
    shortest = min(durations, key=lambda d: d.get_total_minutes())
    longest = max(durations, key=lambda d: d.get_total_minutes())
    return total_duration, shortest, longest

if __name__ == "__main__":
    names, durations = read_durations_from_file("events.txt")
    total, shortest, longest = analyze_durations(durations)
    
    print("Перелік подій:")
    for name, duration in zip(names, durations):
        print(f"{name} - {duration}")
    
    print(f"\nЗагальна тривалість: {total} хвилин")
    print(f"Найкоротша подія: {shortest}")
    print(f"Найтриваліша подія: {longest}")
