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

class Event:
    def __init__(self, name: str, duration: PreciseDuration):
        self.__name = name
        self.__duration = duration
    
    def get_duration(self):
        return self.__duration
    
    def __str__(self):
        return f"{self.__name} - {self.__duration}"

def read_events_from_file(filename):
    events = []
    with open(filename, 'r') as file:
        for line in file:
            name, h, m, s = line.strip().split(', ')
            duration = PreciseDuration(int(h), int(m), int(s))
            events.append(Event(name, duration))
    return events

def analyze_events(events):
    total_duration = sum(event.get_duration().get_total_minutes() for event in events)
    shortest = min(events, key=lambda e: e.get_duration())
    longest = max(events, key=lambda e: e.get_duration())
    return total_duration, shortest, longest

if __name__ == "__main__":
    events = read_events_from_file("events.txt")
    total, shortest, longest = analyze_events(events)
    
    print("Перелік подій:")
    for event in events:
        print(event)
    
    print(f"\nЗагальна тривалість: {total} хвилин")
    print(f"Найкоротша подія: {shortest}")
    print(f"Найтриваліша подія: {longest}")
