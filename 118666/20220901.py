def solution(surveys, choices):
    # print(surveys)
    # print(choices)

    score_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    iter_cnt = 0

    for survey in surveys:
        tmp_score = choices[iter_cnt] - 4

        if tmp_score < 0:
            score_dict[survey[0]] = score_dict[survey[0]] + abs(tmp_score)
        else:
            score_dict[survey[1]] = score_dict[survey[1]] + tmp_score

        iter_cnt += 1

        # print(score_dict)

    answer = "RCJA"
    if score_dict['R'] < score_dict['T']:
        answer = answer.replace('R', 'T')
    if score_dict['C'] < score_dict['F']:
        answer = answer.replace('C', 'F')
    if score_dict['J'] < score_dict['M']:
        answer = answer.replace('J', 'M')
    if score_dict['A'] < score_dict['N']:
        answer = answer.replace('A', 'N')

    return answer