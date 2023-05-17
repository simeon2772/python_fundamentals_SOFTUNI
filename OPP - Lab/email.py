class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []
command = input()
while command != "Stop":
    element = command.split()
    sender = element[0]
    receiver = element[1]
    content = element[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())
