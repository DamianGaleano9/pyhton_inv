class Invoice: 

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes {self.total}'
    
google = Invoice('Google', 100)
instagram = Invoice('Instragam', 200)
facebook = Invoice('Facebook', 200)


# print(google.formatter())
# print(instagram.formatter())

print(google.client)
print(google.total)
