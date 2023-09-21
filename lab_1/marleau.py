from datetime import datetime
import json

time_list = []
number_of_coughs = 0
out_file = open(f"coughs_{datetime.now()}.txt", "a")

while True:
    coughs = input(f"coughs? ({number_of_coughs} to date)")
    moment = datetime.now()
    out_file.write(f"{coughs} coughs at time {moment} \n")
    if coughs == "yeet":
        break
    number_of_coughs += 1

out_file.close()

# json.dump({"number of coughs": time_list}, out_file)
