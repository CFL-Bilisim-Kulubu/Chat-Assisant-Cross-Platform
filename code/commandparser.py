commandList = [
    "email",
    "text",
    "reminder",
    "summary",
    "meeting",
    "book",
    "website",

]
class Commands:
    def __init__(self):
        pass
    def email(self, to, content):
        pass
    def text(self, to, content):
        pass
    def reminder(self, time):
        pass
    def website(self, content):
        pass
    def meeting(self, time):
        self.reminder(time)
    def book(self, book):
        pass
    def summary(self, book):
        pass


class CommandParser:
    def __init__(self):
        pass
    def parse(self, command):
        self.command = None

        words = command.split(" ").lower()

        for word in words:
            if word in commandList:
                self.command = word
                self.commandFound = True
                break
        if self.commandFound:
            if self.command == "email":
                return Commands.email()
            elif self.command == "text":
                return Commands.text()
            elif self.command == "reminder":
                return Commands.reminder()
            elif self.command == "website":
                return Commands.website()
            elif self.command == "meeting":
                return Commands.meeting()
            elif self.command == "book":
                return Commands.book()
        else:
            return None

        

    def apply(self):
        pass