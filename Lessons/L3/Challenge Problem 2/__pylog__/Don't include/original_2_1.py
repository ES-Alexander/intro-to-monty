
coded_message = "V'z n fhcre frperg pbqr. Pna lbh svaq bhg jung V fnl?"
correct_message = "I'm a super secret code. Can you find out what I say?"

# ----- Example Solution ----- #

for shift_amount in range(26):
    decoded_message = ''
    for char in coded_message:
        if char in lower_case_alphabet:
            decoded_message += lower_case_alphabet[
                (lower_case_alphabet.index(char) + shift_amount) % 26]
        elif char in upper_case_alphabet:
            decoded_message += upper_case_alphabet[
                (upper_case_alphabet.index(char) + shift_amount) % 26]
        else:
            decoded_message += char
    print(decoded_message)
