import os
import argparse


path=os.getcwd()

def main():
    parser = argparse.ArgumentParser(description="Python Command Line Interface")
    parser.add_argument("command", choices=["ls", "cd", "mkdir", "rmdir", "rm","rm-r", "cp", "mv", "find", "cat"])
    parser.add_argument("args", nargs="*")
    parser.add_argument("cp",action="store_true",help="cp[source] [destination]: Copy a file or directory from `source` to `destination`.")
    return parser





def files(path):
    files_path=[]
    for paths,dirs,file in os.walk(path):
        for f in file:
            f_path=os.path.join(paths,f)
            files_path.append(f_path)

    return files_path


def find_file_exts(files):
  exts = set()
  for f in files:
    ext = f.split(".")[-1]
    exts.add(ext)
  return exts


def create_dirs(path, exts):
  for x in exts:
    name = f"folder_{x}"
    new_path = os.path.join(path, name)
    os.mkdir(new_path)


def cut_files(files,path="."):
    for f in files:
        with open(f,"r")  as f_read:
            data=f_read.read()
        name=os.path.basename(f)
        ext=name.split(".")[-1]
        name_dir=f"folder_{ext}"
        new_path=os.path.join(path,name_dir,name)
        with open(new_path,"w") as f_write:
            f_write.write(data)
    

#...........Main..........
parser=main()
args=parser.parse_args()


if args.command=="cp":

  ff=files(path)
  exts = find_file_exts(ff)
  create_dirs(path, exts)
  cut_files(ff,*args.args)
