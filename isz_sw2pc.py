import os, shutil, sys
from time import sleep

current_dir = os.path.dirname(__file__)
in_folder = current_dir + '\\in'
out_folder = current_dir + '\\out'
os.makedirs(out_folder, exist_ok=True)
os.makedirs(in_folder, exist_ok=True)

file2copy = os.listdir(in_folder)

for file_name in file2copy:
    source_file = os.path.join(in_folder, file_name)

    if '.vdf' not in file_name:
        file_name = file_name + '.sav'
    else:
        pass

    destination_file = os.path.join(out_folder, file_name)
    shutil.copy2(source_file, destination_file)

file2copy = os.listdir(out_folder)

for file_name in file2copy:
    file_name = out_folder + f"\\{file_name}"

    with open(file_name,'rb+') as f:
        if '.vdf' not in file_name:
            f.seek(0x00)
            f.write(b'\x00')
            f.close()
        else:
            pass

file2copy = os.listdir(in_folder)

for in_folderf in file2copy:
    in_folderf = in_folder + f"\\{in_folderf}"
    os.remove(in_folderf)

sleep(1)
print(f"\nConversion has been Completed.")