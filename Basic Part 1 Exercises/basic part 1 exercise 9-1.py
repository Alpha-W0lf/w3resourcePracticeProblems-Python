# Write a program to display the exam schedule. (Do  this assuming exam_st_date is a tuple. Then assume it's a
# string.) DONE

exam_st_date = ('11, 12, 2014')
# Sample output: The exam will start: 11/12/2014

# exam_st_date_list = list(exam_st_date)
# print(exam_st_date_list)
# month = exam_st_date_list[0]
# day = exam_st_date_list[1]
# year = exam_st_date_list[2]
#
# print('The exam will start: ', month, '/', day, '/', year, sep = '')

exam_st_date_list = list(exam_st_date.split(', '))
print(exam_st_date_list)
month = exam_st_date_list[0]
day = exam_st_date_list[1]
year = exam_st_date_list[2]

print ('The exam will start: ', month, '/', day, '/', year, sep = '')