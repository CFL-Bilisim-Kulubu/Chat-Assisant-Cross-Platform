

class Command:
    def __init__(self, command=None, time=None, to=None, content=None, named=None):
        self.command = command
        self.time = time
        self.to = to
        self.content = content
        self.named = named
        self.apply_command()

    def apply_command(self):
        if self.command is not None:
            if self.command == "email":
                return self.email(self.to, self.content)
            elif self.command == "text":
                return self.text(self.to, self.content)
            elif self.command == "reminder":
                return self.reminder(self.time)
            elif self.command == "website":
                return self.website(self.named)
            elif self.command == "meeting":
                return self.meeting(self.time)
            elif self.command == "book":
                return self.book(self.named)
        else:
            return None
        
    def email(self, to, content):
        if to is None:
            print("no email")
            return None
        elif content is None:
            print("no content")
            return None
        
        print("email sent to " + to + " with content " + content)
        return None
    
    def text(self, to, content):
        print("text sent to " + to + " with content " + content)
        return None
    
    def reminder(self, time):
        print("reminder set for " + time)
        return None
    
    def website(self, website):
        print("opening website " + website)
        return None
    
    def meeting(self, time):
        self.reminder(time)

    def book(self, book):
        print("summarizing book " + book)
        return None


class CommandParser:
    commandList = [
    "email",
    "text",
    "reminder",
    "summary",
    "meeting",
    "book",
    "website",
    ]
    def __init__(self):
        self.command = None
        self.time = None
        self.to = None
        self.content = None
        self.named = None
        self.commandFound = False
    def parse(self, command):
        self.command = None

        words = command.lower().split(" ")

        for index, word in enumerate(words):
            if word in self.commandList:
                self.command = word
                self.commandFound = True
            
            if word in "at":
                try:
                    self.time = words[index + 1]
                except:
                    print("no time")
                    self.time = None

            elif word in "to":
                try:
                    self.to = words[index + 1]
                except:
                    print("no to")
                    self.to = None

            elif word in "content":
                try:
                    self.content = words[index + 1]
                except:
                    print("no content")
                    self.content = None

            elif word in "named":
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