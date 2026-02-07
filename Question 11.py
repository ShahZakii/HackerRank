# HackerRank Python Question.

# Question 11:
# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for i in range(N):
        user_input = input().split()
        
        if user_input[0] == "insert":
            lst.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0] == "print":
            print(lst)
        elif user_input[0] == "remove":
            lst.remove(int(user_input[1]))
        elif user_input[0] == "append":
            lst.append(int(user_input[1]))
        elif user_input[0] == "sort":
            lst.sort()
        elif user_input[0] == "pop":
            lst.pop()
        elif user_input[0] == "reverse":
            lst.reverse()