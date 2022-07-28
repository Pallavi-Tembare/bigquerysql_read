from exec_bigquery import Exec_Bigquery


class Bigsqlfile_Read:
    def __init__(self, filepath):
        self.filepath = filepath
        filename = (filepath.split("\\")[-1]).strip('"')
        dir_path = (filepath.split(filename)[0]).strip('"')

    def bigsqlfile_read(self):
        try:
            # trying to open a file in read mode
            with open(self.filepath, "r") as f:
                data = f.read()
                ex_bq = Exec_Bigquery(data)
        except FileNotFoundError:
            print("File does not exist")


user_input = input("Enter the path of your file: ")
bq_read = Bigsqlfile_Read(user_input)
bq_read.bigsqlfile_read()
