import datetime
import random


def exam_st_date (user_dict):
    print ("\n")
    for i in user_dict:
        print (i, "exam starts from: ", user_dict[i])

courses= ['DS','CE','DB','SE','CD','FDB']  
my_dict= { }


#         my_dict[i]=date

for i in courses:
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    my_dict[i]=random_date

    print( random_date)
    print(i)