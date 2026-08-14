t = ('a', 'b', 'c', 'd', 'e')
print(t[1:])

t1 = 'A',
print(t1)

t2 = t1 + t[1:]
print(t2)

# ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10

a, b = b, a
print(a, b)

email = "fulano@gmail.com"
username, domain = email.split("@")
print(username)
print(domain)