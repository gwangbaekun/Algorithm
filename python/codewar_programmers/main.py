#letters: abcdefghijklmnopqrstuvwxyz
def find_the_number_plate(customer_id):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    divide = customer_id // 999
    letter = letters[divide % 26] + letters[divide // 26 % 26] + letters[divide // (26 * 26) % 26]
    number = customer_id % 999 + 1
    if number < 10:
        return(letter + '00' + str(number))
    elif number < 100:
        return(letter + '0' + str(number))
    else: 
        return(letter + str(number))