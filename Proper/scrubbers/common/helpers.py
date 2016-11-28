"""Helper methods for datafusion ingest."""

# For printing current date and time
import datetime
# For checksum generation and validation
import hashlib
# For output of valid data in original folder structure
import os

if __name__ == "__main__":
    print "This module cannot be run as a script."
    print "Import this module into your code."
    exit()


class DFHelper:
    """Helper Class to be used in Datafusion scrubbers."""

    def __init__(self, telco=None, log_dir_path=None):
        """Constructor for DFHelper.
           log_dir_path is the destination directory log files are written to"""
        if telco is None or log_dir_path is None:
            raise ValueError("telco and log_dir_path must be defined!")

        # save values in object
        self.telco = telco
        self.log_dir_path = log_dir_path

        # generate log file path
        now = datetime.datetime.utcnow().isoformat().replace(":", "")
        self.log_file_path = self.log_dir_path + now + ".log"

        # create log file
        # change 'wb' to 'w' for non-windows system
        self.log_file = open(self.log_file_path, 'wb')

    def __del__(self):
        """Destructor for DFHelper."""
        self.log_file.close()

    def log(self, log_object, error_message):
        """Log method for DFHelper."""
        # define output string
        formatted = "[%s] - %s - %s - %s - %s - %s" % (
            datetime.datetime.utcnow().isoformat(),
            self.telco,
            log_object["file_name"],
            log_object["line_number"],
            log_object["line_content"],
            error_message
        )
        # append output string to logfile each time log_all is called.
        self.log_file.write(formatted + "\r\n")


    def writeout(self,filepath,folderpath,good_data_file_path,valid_lines):
        """Writes valid rows to a new file, replicating original folder structure"""

        # create relative path in output destination folder
        relative_file_path = filepath.replace(folderpath,"")
        output_path = good_data_file_path + relative_file_path
        output_path_parts = output_path.split("\\")
        output_dir = output_path.replace("\\" + output_path_parts[-1],"")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # create output file object
        # change 'wb' to 'w' for non-windows system
        fo = open(output_path,"wb") 
        for line in valid_lines:
            fo.write(line)
        fo.close()   


    def md5(self, file_path):
        """Compute and returns md5 hash of file."""
        computed_hash = None
        with open(file_path, 'rb') as file:
            file_buffer = file.read()
            md5_hash = hashlib.md5()
            md5_hash.update(file_buffer)
            computed_hash = md5_hash.hexdigest()
        return computed_hash
