commandList = [
    "email",
    "text",
    "reminder",
    "summary",
    "meeting",
    "book",
    "website",

]
class Command:
    def __init__(self, command=None, time=None, to=None, content=None, named=None):
        if command is not None:
            if self.command == "email":
                return self.email(to, content)
            elif self.command == "text":
                return self.text(to, content)
            elif self.command == "reminder":
                return self.reminder(time)
            elif self.command == "website":
                return self.website(named)
            elif self.command == "meeting":
                return self.meeting(time)
            elif self.command == "book":
                return self.book(named)
        else:
            return None
        
    def email(self, to, content):
        pass
    def text(self, to, content):
        pass
    def reminder(self, time):
        pass
    def website(self, website):
        pass
    def meeting(self, time):
        self.reminder(time)
    def book(self, book):
        pass
    def summary(self, book):
        pass


class CommandParser:
    def __init__(self):
        self.command = None
        self.time = None
        self.to = None
        self.content = None
        self.named = None
        self.commandFound = False
    def parse(self, command):
        self.command = None

        words = command.split(" ").lower()

        for index, word in words:
            if word in commandList:
                self.command = word
                self.commandFound = True
            elif word is "at":
                try:
                    self.time = words[index + 1]
                except:
                    print("no time")
                    self.time = None

            elif word is "to":
                try:
                    self.to = words[index + 1]
                except:
                    print("no to")
                    self.to = None

            elif word is "content":
                try:
                    self.content = words[index + 1]
                except:
                    print("no content")
                    self.content = None

            elif word is "named":
                try:
                    self.named = words[index + 1]
                except:
                    print("no named")
                    self.named = None
        return {
            "command": self.command,
            "time": self.time,
            "to": self.to,
            "content": self.content,
            "named": self.named
        }