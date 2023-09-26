from datetime import datetime

time_list = []
number_of_coughs = 0
out_file = open(f"coughs_{datetime.now()}.txt", "a")
start = datetime.now()
out_file.write(f"[")
while True:
    coughs = input(f"coughs? ({number_of_coughs} total)")
    moment = datetime.now() - start
    if coughs == "yeet":
        out_file.write(f"]")
        break
    else:
        out_file.write(f"[{number_of_coughs+1}, {moment.total_seconds()}]")
    out_file.write(f"\n")
    number_of_coughs += 1

out_file.close()

# json.dump({"number of coughs": time_list}, out_file)

# start_time = time(15, 30, 0)
# time_objects_list = [time(15, 45, 45),
#                      time(15, 45, 56),
#                      time(15, 46, 6),
#                      time(15, 46, 16),
#                      time(15, 46, 19),
#                      time(15, 46, 22),
#                      time(15, 47, 0),
#                      time(15, 47, 0),
#                      time(15, 47, 30),
#                      time(15, 47, 35),
#                      time(15, 47, 40),
#                      time(15, 47, 44),
#                      time(15, 47, 45),
#                      time(15, 48, 29),
#                      time(15, 48, 42),
#                      time(15, 50, 0),
#                      time(15, 50, 31),
#                      time(15, 51, 2),
#                      time(15, 52, 33),
#                      time(15, 53, 1),
#                      time(15, 53, 20),
#                      time(15, 53, 29),
#                      time(15, 53, 29),
#                      time(15, 53, 41),
#                      time(15, 54, 1),
#                      time(15, 54, 15),
#                      time(15, 54, 32),
#                      time(15, 54, 44),
#                      time(15, 54, 44),
#                      time(15, 55, 5),
#                      time(15, 56, 0),
#                      time(15, 56, 14),
#                      time(15, 56, 22),
#                      time(15, 56, 49),
#                      time(15, 57, 11),
#                      time(15, 57, 11),
#                      time(15, 57, 40),
#                      time(15, 57, 40),
#                      time(15, 57, 41),
#                      time(15, 57, 56),
#                      time(15, 58, 52),
#                      time(15, 58, 52),
#                      time(15, 59, 25),
#                      time(15, 59, 38),
#                      time(15, 59, 49),
#                      time(16, 00, 0),
#                      time(16, 00, 38),
#                      time(16, 00, 49),
#                      time(16, 1, 11),
#                      time(16, 1, 19),
#                      time(16, 1, 24),
#                      time(16, 1, 29),
#                      time(16, 2, 17),
#                      time(16, 2, 17),
#                      time(16, 2, 31),
#                      time(16, 2, 57),
#                      time(16, 2, 57),
#                      time(16, 3, 37),
#                      time(16, 3, 37),
#                      time(16, 4, 15),
#                      time(16, 4, 18),
#                      time(16, 5, 00),
#                      time(16, 5, 7),
#                      time(16, 5, 7),
#                      time(16, 5, 24),
#                      time(16, 5, 24),
#                      time(16, 5, 44),
#                      time(16, 5, 44),
#                      time(16, 6, 00),
#                      time(16, 6,1),
#                      time(16, 6, 1),
#                      time(16, 6, 3),
#                      time(16, 6, 48),
#                      time(16, 6, 48),
#                      time(16, 6, 54),
#                      time(16, 6, 56),
#                      time(16, 7, 10),
#                      time(16, 7, 10),
#                      time(16, 7, 11),
#                      time(16, 7, 30),
#                      time(16, 7, 32),
#                      time(16, 7, 37),
#                      time(16, 7, 47),
#                      time(16, 8, 0),
#                      time(16, 8, 1),
#                      time(16, 8, 2),
#                      time(16, 8, 3),
#                      time(16, 8, 3),
#                      time(16, 8, 3),
#                      time(16, 8, 5),
#                      time(16, 8, 5),
#                      time(16, 9, 0),
#                      time(16, 9, 0),
#                      time(16, 9, 0),
#                      time(16, 9, 2),
#                      time(16, 9, 2),
#                      time(16, 9, 2),
#                      time(16, 9, 2),
#                      time(16, 9, 4),
#                      time(16, 9, 5),
#                      time(16, 10, 4),
#                      time(16, 10, 13),
#                      time(16, 10, 32),
#                      time(16, 10, 40),
#                      time(16, 10, 41),
#                      time(16, 10, 45),
#                      time(16, 11, 19),
#                      time(16, 11, 24),
#                      time(16, 11, 29),
#                      time(16, 11, 33),
#                      time(16, 11, 46),
#                      time(16, 12, 3),
#                      time(16, 12, 21),
#                      time(16, 12, 45),
#                      time(16, 12, 45),
#                      time(16, 12, 59),
#                      time(16, 13, 13),
#                      time(16, 13, 22),
#                      time(16, 13, 44),
#                      time(16, 13, 46),
#                      time(16, 14, 00),
#                      time(16, 14, 26),
#                      time(16, 14, 28),
#                      time(16, 14, 38),
#                      time(16, 14, 52),
#                      time(16, 14, 58),
#                      time(16, 15, 17),
#                      time(16, 15, 34),
#                      time(16, 15, 34),
#                      time(16, 15, 41),
#                      time(16, 15, 59),
#                      time(16, 16, 2),
#                      time(16, 16, 10),
#                      time(16, 16, 28),
#                      time(16, 16, 45),
#                      time(16, 16, 50),
#                      time(16, 17, 1),
#                      time(16, 17, 17),
#                      time(16, 17, 23),
#                      time(16, 17, 27),
#                      time(16, 18, 11),
#                      time(16, 18, 14),
#                      time(16, 18, 19)]
#
# seconds_list = []
#
# for time in time_objects_list:
#     seconds_list.append(time.hour*3600 + time.minute*60 + time.second)
# position_list = [i for i in range(len(seconds_list))]
# seconds_array = np.array(seconds_list)
# plt.plot(seconds_list, position_list)
# plt.plot([seconds_list[0], seconds_list[-1]], [position_list[0], position_list[-1]])
# # plt.hist(seconds_list, bins=25)
# plt.show()
