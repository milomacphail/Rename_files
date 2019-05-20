import os
from datetime import datetime

folder = "/Users/milo/Documents/renamer"
location = input("Photo location: ")
files = os.listdir(folder)
counter = 0;

for filename in files:
    counter += 1
    string_counter = str(counter)
    if not filename.startswith('.'):
        file = os.path.join(folder, filename)

        m_time = os.path.getmtime(file)
        real_time = datetime.fromtimestamp(m_time)
        f_time = datetime.strftime(real_time, "%Y-%B-%d %H:%M:%S")

        new_filename = string_counter + "_" + f_time + "_" + location + ".jpeg"
        new_file = os.path.join(folder, new_filename)
        os.rename(file, new_file)
