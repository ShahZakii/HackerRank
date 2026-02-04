# HackerRank Python Question.

# Question 8:
# Given the participants' score sheet for your University Sports Day, you are required to find the 
# runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    rem_dup = set(arr)
    new_arr = list(rem_dup)
    new_arr.sort(reverse=True)
    print(new_arr[1])