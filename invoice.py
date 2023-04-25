# class Invoice:

#     def __init__(self, client, total):
#         self._client = client
#         self._total = total

#     def formatter(self):
#         return f'{self._client} owes {self._total}'

#     @property
#     def client(self):
#         return self._client

#     @client.setter
#     def client(self, client):
#         self._client = client


#     @property
#     def total(self):
#         return self._total

#     @total.setter
#     def total(self, total):
#         self._total = total


# google = Invoice('Google', 100)

# print(google.total)


# google.total = 1000

# print(google.total)

# google.client = 'Instagram'
# print(google.client)


class Invoice:

    def __init__(self, total, client):
        self.total = total
        self.client = client

    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'


inv = Invoice('Damian', 100000)
print(str(inv))
