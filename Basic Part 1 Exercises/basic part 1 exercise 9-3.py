# Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)

print('The exam will start: ', exam_st_date[0], '/', exam_st_date[1], '/', exam_st_date[2], sep='')
print('The exam will start: %i/%i/%i' % exam_st_date)

# DONE