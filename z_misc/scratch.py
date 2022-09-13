# import datetime
# from datetime import timedelta

# today = datetime.date.today()
# days_45 = timedelta(days = 90)
# result = today - days_45
# print(today)
# print(result)

# for i in range(10, 0, -1):
#     print(i)

# num = "7.25"
# print(type(num))
# num = int(num)
# print(type(num))
# print(num)

period_queue = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(period_queue)
period_queue.pop(-1)
period_queue.insert(0, 1)
print(period_queue)