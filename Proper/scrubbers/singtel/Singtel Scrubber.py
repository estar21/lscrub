import sys, os, string, datetime
sys.path.insert(0, "F:\ingest\Proper\scrubbers\common")
import helpers
from helpers import DFHelper


# Define Acceptable Ranges for Values in each Telco's Schema Here:
Telco_3 = {"0": {"allowed": set(string.ascii_uppercase + string.digits), "length": 64},
           "1": {"allowed": "%Y-%m-%d %H:%M", "length": 16},
           "2": {"allowed": range(0,150), "length": range(1,4)},
           "3": {"allowed": range(0,200), "length": range(1,4)},
	   "num_col" : 5
           }

# Define Input and Output Filepaths Here:
Telco_3_file_paths = {"nas1" : "F:\\ingest\\Proper\\nas1\\singtel",
                      "good_data": "F:\ingest\Proper\output\scrubbed\singtel",
                      "data_error_logs": "F:\ingest\Proper\output\data error logs\singtel\\",
                      "checksum_error_logs": "F:\ingest\Proper\output\checksum error logs\singtel"}


def validate_telco3(Telco_3):
    """Returns only lines that are valid.
       Calls log_all() to log lines that are invalid"""

    # Start DFHelper instance once per scrubber run
    telco = "ST"
    df_helper = DFHelper(telco, Telco_3_file_paths["data_error_logs"])
    
    # process raw files (one pass per daily batch)
    folderpath = Telco_3_file_paths["nas1"]
    for dirpath, subdirs, files in os.walk(folderpath):
        for filename in files:
            filepath = os.path.join(dirpath, filename)

            ### INSERT CHECKSUM PROCESS HERE ###
            # call df_helper.md5("path_to_file_you_want_to_hash")
            # proceed only if checksum matches. else, generate checksum log to Telco_3_file_paths["checksum_error_logs"]

            fo = open(filepath, "rb")
            lines = fo.readlines()
            for line in lines:
                line_index = str(lines.index(line) + 1)           
                line_clean = line.replace("\n","")
                line_clean = line.replace("\r\n","")
                
                # create dictionary for each line's properties so they can be included in log via df_helper.log() if line is problematic
                log_obj = {"file_name": filename, "line_number": line_index, "line_content": line_clean}

                # check expected no. of cols
                cols = line_clean.split(",")
                if len(cols) != Telco_3["num_col"]:
                    df_helper.log(log_obj, "unexpected no. of cols")
                    lines.remove(line)
                else:
                    # check char type
                    try:
                        # col 1 type test
                        set(cols[0]).issubset(Telco_3["0"]["allowed"])
                        # col 2 type test
                        datetime.datetime.strptime(cols[1],Telco_3["1"]["allowed"]) 
                        # col 3 type test
                        int(cols[2])
                        # col 4 type test
                        int(cols[3]) 
                    except ValueError:
                        df_helper.log(log_obj, "unexpected char or data type")
                        lines.remove(line)
                    else:
                        # check length and allowed characters/ ranges for values
                        # 1st col
                        if ((set(cols[0]).issubset(Telco_3["0"]["allowed"])) and (len(cols[0]) == Telco_3["0"]["length"])) == False:
                            df_helper.log(log_obj, "col 1 unexpected charset or char length")
                            lines.remove(line)
                        # 2nd col
                        elif ((datetime.datetime.strptime(cols[1],Telco_3["1"]["allowed"])) and (len(cols[1]) == Telco_3["1"]["length"])) == False:
                            df_helper.log(log_obj, "col 2 unexpected format or char length")
                            lines.remove(line)
                        # 3rd col
                        elif ((set(cols[2]).issubset(string.digits)) and (int(cols[2]) in Telco_3["2"]["allowed"]) and (len(cols[2]) in Telco_3["2"]["length"])) == False:
                            df_helper.log(log_obj, "col 3 unexpected char length or value out of range")
                            lines.remove(line)
                        # 4th col
                        elif ((set(cols[3]).issubset(string.digits)) and (int(cols[3]) in Telco_3["3"]["allowed"]) and (len(cols[2]) in Telco_3["3"]["length"])) == False:
                            df_helper.log(log_obj, "col 3 unexpected char length or value out of range")
                            lines.remove(line)
            df_helper.writeout(filepath,folderpath,Telco_3_file_paths["good_data"],lines)
    #return lines



validate_telco3(Telco_3)
print "done"
