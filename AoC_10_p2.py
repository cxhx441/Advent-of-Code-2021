with open("AoC_10_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]
points_worth = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
# errors_found = {')' : 0, ']' : 0, '}' : 0, '>' : 0}
closers_openers = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}
openers_closers ={'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

def get_completion_string(string):
    evaluated = []
    needed_closers = []
    for ch in string:
        if ch in openers_closers.keys():
            evaluated.append(ch)
        else:
            if evaluated[-1] == closers_openers[ch]:
                evaluated.pop()
    for ch in evaluated[::-1]:
        needed_closers.append(openers_closers[ch])
    return needed_closers

def errors_found(string):
    evaluated = []
    for ch in string:
        if ch in openers_closers.keys():
            evaluated.append(ch)
        elif ch in closers_openers.keys():
            if evaluated[-1] == closers_openers[ch]:
                evaluated.pop()
            else:
                # errors_found[ch] += 1
                # break
                return True

string_completions = []
for string in lines:
    if not errors_found(string):
        string_completions.append(get_completion_string(string))

scores = []
for string_completion in string_completions:
    score = 0
    for ch in string_completion:
        score *= 5
        score += points_worth[ch]
    scores.append(score)
    print(score)

scores.sort()
print(scores[len(scores)//2])

