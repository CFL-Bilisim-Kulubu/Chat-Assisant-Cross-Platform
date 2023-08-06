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
        pass
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

        if self.commandFound:
            if self.command == "email":
                return Commands.email(self.to, self.content)
            elif self.command == "text":
                return Commands.text(self.to, self.content)
            elif self.command == "reminder":
                return Commands.reminder(self.time)
            elif self.command == "website":
                return Commands.website(self.named)
            elif self.command == "meeting":
                return Commands.meeting(self.time)
            elif self.command == "book":
                return Commands.book(self.named)
        else:
            return None

        

    def apply(self):
        pass