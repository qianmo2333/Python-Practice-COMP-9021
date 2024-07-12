def condition_judge(all_sir, saying_d, condition):
    mentioned_name = []
    for word in saying_d:
        if type(word) == int:
            mentioned_name.append(word)
        if word == 'us':
            mentioned_name = [i for i in range(len(all_sir))]
    temp = []