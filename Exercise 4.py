import random
import string

ask = int(input("Enter 1 for Decoding and 0 for Encoding: "))

if ask==0:
    msg = input("Enter the message you want to code: ")
    if len(msg) <=2:
        codeM = msg[::-1]
        print(codeM)
    else:
        h = msg[0]
        new = msg[1:]
        # random_start = ''.join(random.choices(string.digits, k=3))
        # random_end = ''.join(random.choices(string.digits, k=3))
        random_start = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        random_end = ''.join(random.choices(string.ascii_letters + string.digits, k=3))

        code_m = random_start  + new + h+ random_end
        print(code_m)

else:
    msg = input("Enter the message you want to decode: ")
    if len(msg) <=2:
        codeM = msg[::-1]
        print(codeM)
    else:
        trimmed_string = msg[3:-3]
        end = trimmed_string[-1]
        new = trimmed_string[:-1]
        decoded_m = end + new
        print(decoded_m)

