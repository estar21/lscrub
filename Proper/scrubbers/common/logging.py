import os, string, datetime
import pygogo as gogo

##DF Helper takes care of this
##def start_log(telco, scrubber_start_time): # function to create log file if it does not exist
##    """Creates Log File Object"""
##    log_file_path = "%s_%s.log" % (telco, scrubber_start_time)
##    if not os.path.exists(log_file_path):
##        log_file_path_fo = open(log_file_path, 'wb') # change 'wb' to 'w' for non-windows system
##    return log_file_path_fo
        
def log_all(log_fo, log_object, errormsg):
    # define filepath
    log_file_path = "%s_%s.log" % (log_object["telco"], log_object["scrubber_start_time"])
    logger = gogo.Gogo(low_hdlr=gogo.handlers.file_hdlr(log_file_path)).logger
    # define output string
    formatted = "[%s] - %s - %s - %s - %s - %s" % (datetime.datetime.utcnow().isoformat(), log_object["telco"], log_object["file_name"], log_object["line_number"], log_object["line_content"], errormsg)
    # append output string to logfile each time log_all is called.
    log_fo.write(formatted + "\r\n")

# --- from a later file ---- check LOG ALL
##def log_content(content_object):
##    formatted = "[%d] - [%s] - %s" % (content_object.line_number, content_object.message, content_object.line)
##    print formatted
##
##def log_all(lineno, message, line):
##    message = "line removed because y"
##    log_object = {
##        "file_name": "x",
##        "message": message
##    }
##    content_object = {
##        "line_number": lineno,
##        "message": message,
##        "line": line
##    }
##    log_this(log_object)
##    log_content(content_object)
##    lines.remove(line)
