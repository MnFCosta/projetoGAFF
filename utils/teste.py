
nome="Manoel"

if ' ' in nome:
    first_name, last_name = nome.split(' ', 1)
else:
    first_name = nome


print(first_name)