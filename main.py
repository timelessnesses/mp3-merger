import pydub,os,sys

try:
  path = sys.argv[1]
except IndexError:
  path = "."
try:
  exportname = sys.argv[2]
except IndexError:
  export = "audio.mp3"

merge = pydub.AudioSegment.empty()

for file in os.listdir(path):
  try:
    print("trying to merge",file)
    merge += AudioSegment.from_file(path+"/"+file)
  except:
    print("failed",file)
    continue
 merge.export(path+"/"+exportname,format="mp3")
