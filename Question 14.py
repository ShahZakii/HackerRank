# HackerRank Python Question.

# Question 14:
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    split_line = line.split(" ")
    join_line = "-".join(split_line)
    return join_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)