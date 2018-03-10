from os.path import  join, isfile
from os import listdir

#
# check all the files in database match after step 3 of the process
#

wav_files = [join('database/wav', f) for f in listdir('database/wav') if isfile(join('database/wav', f)) and f.endswith('.wav')]
txt_files = [join('database/txt', f) for f in listdir('database/txt') if isfile(join('database/txt', f)) and f.endswith('.txt')]

print("wav size = " + str(len(wav_files)))
print("txt size = " + str(len(txt_files)))

if len(wav_files) != len(txt_files):
    print("major error - txt files do not match wav files")
    exit(1)

mgc_files = [join('database/feats/mgc', f) for f in listdir('database/feats/mgc') if isfile(join('database/feats/mgc', f)) and f.endswith('.mgc')]
print("mgc size = " + str(len(mgc_files)))
if len(mgc_files) != len(txt_files):
    print("mgc file count not matching - adjustment needed see: database/feats/mgc")
    exit(1)

lab_files = [join('database/labels/label_state_align', f) for f in listdir('database/labels/label_state_align') if isfile(join('database/labels/label_state_align', f)) and f.endswith('.lab')]
print("lab size = " + str(len(lab_files)))
if len(mgc_files) != len(lab_files):
    print("lab file count not matching - adjustment needed see: database/labels/label_state_align")
    exit(1)

print("all sizes good to go!")
