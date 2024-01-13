import os, shutil, sys
from time import sleep

current_dir = os.path.dirname(__file__)
main_path = os.getenv('LOCALAPPDATA')
mode_f = current_dir + '\\mode.bin'
chk0 = os.path.exists(mode_f)
in_folder = current_dir + '\\in'
out_folder = current_dir + '\\out'

os.makedirs(out_folder, exist_ok=True)
os.makedirs(in_folder, exist_ok=True)

if chk0 == True:
    isz_path = current_dir + '\\in'
    print(f"Conversion Mode: in-2-out")
else:
    isz_path = main_path + '\\ISZ\\Saved\\SaveGames'
    print(f"Conversion Mode: save-2-out")

chk = os.path.exists(isz_path)

print(f"Does Folder Exist: {chk}")
sleep(0.5)

if chk == False:
    print("Closing Application.")
    sys.exit(1)
else:
    print(f"Continuing to Process Files.")
    pass

file2copy = os.listdir(isz_path)

for file_name in file2copy:
    source_file = os.path.join(isz_path, file_name)
    destination_file = os.path.join(in_folder, file_name)
    shutil.copy2(source_file, destination_file)

for file_name in file2copy:
    source_file = os.path.join(in_folder, file_name)
    destination_file = os.path.join(out_folder, file_name)

    if ".sav" in destination_file:
        destination_file = destination_file.replace('.sav','')
        with open(source_file,'rb+') as f:
            f.seek(0x00)
            f.write(b'\x01')
            f.close()

    shutil.copy2(source_file, destination_file)

for in_folderf in file2copy:
    in_folderf = in_folder + f"\\{in_folderf}"
    os.remove(in_folderf)

sleep(1)
print(f"\nConversion has been Completed.")
sys.exit(1)