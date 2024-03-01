from datetime import date, timedelta

class Books:
    def __init__(self, title, author, is_available, condition):
        self.title = title
        self.author = author
        self.is_available = is_available
        self.condition = condition

    def condition_status(self):
    """ finds condition status """
        if self.condition == 5:
            return ('This books is in great condition')
        elif self.condition >= 3:
            return ('This book  is in ok condition')
        elif self.condition >= 1:
            return ('This book is almost destroyed')
        elif self.condition < 1:
            return ('This book needs to be recycled')

    def check_out(self):
        self.condition -= 1
        self.is_available = False
        today_date = date.today()
        due_date = today_date + timedelta(days = 14)
        print(f'You have checked out {self.title} by {self.author} on {today_date} it is due back on {due_date}')

    def book_return(self):
        self.is_available = True
        print(f'You have returned out {self.title} by {self.author}')
