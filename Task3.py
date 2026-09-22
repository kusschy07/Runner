text = input("Enter a string: ")

if len(text) < 8:
    print("Please enter a string with at least 8 characters.")
else:
    result = ""

    for i in range(len(text)):
        ch = text[i]

        # Odd positions: 1st, 3rd, 5th, ...
        if i % 2 == 0:
            ascii_value = ord(ch)

            # Convert lowercase to uppercase
            if ascii_value >= 97 and ascii_value <= 122:
                ascii_value = ascii_value - 32

            ch = chr(ascii_value)

        result = result + ch

    print("Modified String:", result)
