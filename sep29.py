#pylint disable=c
#
# word = 'Hello World'
# # position = 0
# # n = len(word)
# # while position < n:
# #     print word[position]
# #     position += 1
#
# n = len(word)
# for position in range(0, n):
#     print word[position]
#
# #**To ignore the case use while Q and q
# #use keyword "break" to get out of while loops
# # #i.e:
# #similar to return for functions
# # while True:
# #     question = raw_input('What is your question (or press Q to quit)')
# #     if question.lower() = 'q'
# #       break <---!
# #      answer = random.randint(1,4)
#
# s = 'APPLE'
# s = s.lower()
# print s

while True:
    password = raw_input('What is the password?')
    if len(password) == 4:
        break
