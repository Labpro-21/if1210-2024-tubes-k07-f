def is_integer(input):
    is_integer = True
    for char in input:
        # Mengecek input menggunakan ascii number (0-9 : 48-57)
        if not (48 <= ord(char) <= 57):
            is_integer = False
    return is_integer