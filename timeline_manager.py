from datetime import datetime

class Event:
    def __init__(self, name, date):
        self.name = name.lower()
        self.date = datetime.strptime(date, "%Y-%m-%d")

class Timeline:
    def __init__(self, name):
        self.name = name.lower()
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        self.events.sort(key=lambda x: x.date)

class TimelineManager:
    def __init__(self):
        self.timelines = {}

    def create_timeline(self, name):
        name = name.lower()
        if name not in self.timelines:
            self.timelines[name] = Timeline(name)
            return True
        return False

    def add_event_to_timeline(self, timeline_name, event_name, event_date):
        timeline = self.timelines.get(timeline_name.lower())
        if timeline:
            event = Event(event_name, event_date)
            timeline.add_event(event)
            return True
        return False