with open("AoC_10_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]
points_worth = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
errors_found = {')' : 0, ']' : 0, '}' : 0, '>' : 0}
closers_openers = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}
openers_closers ={'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
def search_string_for_err(string):
    evaluated = []
    for ch in string:
        if ch in openers_closers.keys():
            evaluated.append(ch)
        elif ch in closers_openers.keys():
            if evaluated[-1] == closers_openers[ch]:
                evaluated.pop()
            else:
                errors_found[ch] += 1
                break

for string in lines:
    search_string_for_err(string)

score = 0
for key in errors_found:
    score += errors_found[key] * points_worth[key]
print(errors_found)
print(score)

