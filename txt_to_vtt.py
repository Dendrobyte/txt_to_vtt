import webvtt

txt_path = "-1"
while txt_path == "-1":
    txt_path = input("Please enter path to text file: ")

    try:
        txt_file = open(txt_path, "r+")
    except:
        print("Didn't work! Please try again")
        txt_path = "-1"

print("Got it! VTT file will be put in same folder.")

filename = txt_path.split("/")[-1].split(".")[0]


final_vtt = open(filename + '-converted.vtt', "w+")
final_vtt.write("WEBVTT\n\n")
lineCounter = 0

vtt_incr = 1
for line in txt_file:
    if lineCounter % 4 == 0:
        final_vtt.write(str(vtt_incr) + "\n")
        vtt_incr += 1

        startTimeArr = line.split(" ")[0].split(":")
        endTimeArr = line.split(" ")[2].split(":")
        newStartTime = startTimeArr[0] + ":" + startTimeArr[1] + ":" + startTimeArr[2] + "." + startTimeArr[3] + "0"
        newEndTime = endTimeArr[0] + ":" + endTimeArr[1] + ":" + endTimeArr[2] + "." + endTimeArr[3][0:2] + "0" + "\n"
        vttTime = newStartTime + " --> " + newEndTime
        final_vtt.write(vttTime)
    elif lineCounter % 4 == 2:
        final_vtt.write(line)
        final_vtt.write("\n")
    lineCounter += 1

final_vtt.close()
print("All done!")