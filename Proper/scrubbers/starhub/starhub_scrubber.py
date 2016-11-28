import os, string, datetime

def validate_telco1(telco):
    """Returns only lines that are valid"""
    scrubber_start_time = datetime.datetime.utcnow().isoformat().replace(":","")
    telco_name = "SH"
    log_fo = start_log(telco_name, scrubber_start_time)
    # process raw files
    folderpath = telco["folderpath"]
    for filename in os.listdir(folderpath):
        fo = open(folderpath + "\\" + filename,"rb")
        lines = fo.readlines()

        for line in lines:
            line_index = str(lines.index(line) + 1)
            line_clean = line.replace("\n","")
            log_obj = {"scrubber_start_time": scrubber_start_time, "telco": telco_name, "file_name": filename,
                       "line_number": line_index, "line_content": line_clean}
            cols = line_clean.split(",")
            # check expected no. of cols
            if len(cols) != telco["num_col"]:
                log_all(log_fo, log_obj, "unexpected no. of cols")
                lines.remove(line)
            else:
                # check char type
                try:
                    int(cols[0])
                    int(cols[1])
                    int(cols[2])
                    set(cols[3]).issubset(telco["3"]["allowed"])
                    int(cols[4])
                    int(cols[5])
                except ValueError:
                    log_all(log_fo, log_obj, "unexpect char or data type")
                    lines.remove(line)
                else:
                    # 1st col accuracy
                    if ((set(cols[0]).issubset(string.digits)) and (int(cols[0]) in telco["0"]["allowed"]) and (
                                len(cols[0]) in telco["0"]["length"])) == False:
                        log_all(log_fo, log_obj, "col 1 unexpected charset or char length")
                        lines.remove(line)
                    # 2nd col lat
                    if ((set(cols[1]).issubset(string.digits)) and (int(cols[1]) in telco["1"]["allowed"]) and (
                                len(cols[1]) in telco["1"]["length"])) == False:
                        log_all(log_fo, log_obj, "col 2 unexpected charset or char length")
                        lines.remove(line)
                    # 3rd col long
                    if ((set(cols[2]).issubset(string.digits)) and (int(cols[2]) in telco["2"]["allowed"]) and (
                                len(cols[2]) in telco["2"]["length"])) == False:
                        log_all(log_fo, log_obj, "col 3 unexpected charset or char length")
                        lines.remove(line)
                    # 4th col token
                    if ((set(cols[3]).issubset(telco["3"]["allowed"])) and (len(cols[3]) == telco["3"]["length"])) == False:
                        log_all(log_fo, log_obj, "col 4 unexpected charset or char length")
                        lines.remove(line)
                    # 5th col mcc
                    if ((set(cols[4]).issubset(string.digits)) and (int(cols[4]) in telco["4"]["allowed"]) and (
                                len(cols[4]) in telco["4"]["length"])) == False:
                        log_all(log_fo, log_obj, "col 5 unexpected charset or char length")
                        lines.remove(line)
                    # 6th col timestamp
                    if ((set(cols[5]).issubset(string.digits)) and (int(cols[5]) in telco["5"]["allowed"]) and (
                                len(cols[5]) in telco["5"]["length"])) == False:
                        log_all(log_fo, log_obj, "col 6 unexpected charset or char length")
                        lines.remove(line)
    log_fo.close()
    return lines


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

# Define Acceptable Ranges for Values in each Telco's Schema Here:
Telco_1 = { "0": {"allowed": range(0, 1), "length": 4},
            "1": {"allowed": frange(1.229499, 1.469821, 0.000001), "length": 8 },
            "2": {"allowed": frange(103.609342, 104.05034, 0.000001), "length": 10},
            "3": {"allowed": set(string.ascii_uppercase + string.digits), "length": 32},
            "4": {"allowed": range(0, 999), "length": 3},
            "5": {"allowed": range(1475251200, 1538323200), "length": 10},
            "folderpath" : "C:\etc",
	        "num_col" : 6
            }

valid_lines = validate_telco1(Telco_1)
#for line in valid_lines:
#    # write the line somewhere