def open_brackets(parsed_msg, msg_point):
    mult = ''
    while parsed_msg[msg_point].isdigit():
        mult += parsed_msg[msg_point]
        msg_point += 1
    msg_point += 1
    temp_msg = ''
    closed = False
    while closed is not True:
        if parsed_msg[msg_point].isdigit():
            in_temp_msg, msg_point = open_brackets(parsed_msg, msg_point)
            temp_msg += in_temp_msg
        elif parsed_msg[msg_point] == ']':
            msg_point += 1
            closed = True
        else:
            temp_msg += parsed_msg[msg_point]
            msg_point += 1
    temp_msg *= int(mult)
    return temp_msg, msg_point


def decrypt_msg(msg):
    parsed_msg = list(str(msg))
    msg_point = 0
    answer = ''
    msg_end = len(parsed_msg)

    while msg_point < msg_end:
        if parsed_msg[msg_point].isdigit():
            temp_msg, msg_point = open_brackets(parsed_msg, msg_point)
            answer += temp_msg

        else:
            answer += parsed_msg[msg_point]
            msg_point += 1
    print(answer)


if __name__ == "__main__":
    msg = input()
    decrypt_msg(msg)

    # decrypt_msg('30[a]2[bc]')
    # decrypt_msg('3[a2[c]]')
    # decrypt_msg('2[abc]3[cd]ef')

