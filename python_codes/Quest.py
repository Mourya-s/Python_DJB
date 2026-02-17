# #leap year
# year=int(input("enter the year "))
# if year%4 ==0:
#     print("is a leap year")
# else :
#     print(f"Not a laep year")


# #Pattern program
# alp=97
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(chr(alp),end=" ")
#             alp+=1
#         else :
#             print(alp, end=" ")
   
#     print()


# #NOTE: THE THE TAB DISTANCE IS NOT IMPORTANT , ALL ATATEMENT OF THE CONDITION SHALL BE IN SAME LINE
# sen = 0

# if sen == 0:
#   print('sensor is OFF')
#   print('Switch Motor OFF')
# else:
#         print('sensor is ON')
#         print('Switch Motor ON')
    
# print('Done')

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()