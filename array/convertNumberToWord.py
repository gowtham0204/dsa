def convert_to_text(number):
    if number < 0 or number > 9999:
        return "Input out of range"
    if number == 0:
        return "Zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    thousand_part = number // 1000
    hundred_part = (number % 1000) // 100
    tens_part = (number % 100 ) //10
    ones_part = number % 10
    lastTwoDigit = number % 100

    result = ""
    if thousand_part > 0:
        result += ones[thousand_part] + " " + "thousand "
    if hundred_part > 0:
        result += ones[hundred_part] + " " + "hundred and "
    if lastTwoDigit >= 11 and lastTwoDigit <20:
        result += (teens[lastTwoDigit % 10])
    else:
        result += (tens[tens_part] +  " " + ones[ones_part])
    
    return result.strip()
 

# Example usage:
number = 1001
print(convert_to_text(number))
