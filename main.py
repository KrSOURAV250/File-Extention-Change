import os
folder = r'D:\Other Videos'
for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.MOV', '.mp4')
    os.rename(infilename, newname)
