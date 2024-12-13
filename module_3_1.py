calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_registr = string.upper()
    lower_registr = string.lower()
    return (length, upper_registr, lower_registr)

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string in list_to_search:
        print(True)
    else:
        print(False)


print(string_info("Capybara"))
print(string_info("Armageddon"))
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)