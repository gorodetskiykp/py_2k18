# from re import findalls
some_string = "ssme2streng12"
# print(findall(r'\d+', some_string))
digits = [sign for sign in some_string if sign.isdigit()]
# for sign in some_string:
#     try:
#         int(sign)
#         digits.append(sign)
#     except:
#         pass
print(len(some_string) == int(''.join(digits)) and str(len(some_string)) in some_string)
