import os
import uuid
from os.path import join
from gen_scheme_file import gen_scheme_file
from normalize_lab_for_merlin import normalize_lab_for_merlin
import subprocess

base_dir = '/opt/merlin'
make_labels_exe = base_dir + '/misc/scripts/frontend/festival_utt_to_lab/make_labels'
festival_utt_to_label = base_dir + '/misc/scripts/frontend/festival_utt_to_lab'
festival_exe = base_dir + '/tools/festival/bin/festival'
festival_dumpfeats = base_dir + '/tools/festival/examples/dumpfeats'
temp_dir = '/tmp'


# create labels step 1 from the generate speech synthesis process
def create_labels(text, out_dir, utt_dir='utt', label_dir='label', scheme_file='001.scm',
                  file_id_scp='001_id_list.scp', labels='state_align'):

    gen_scheme_file(text, join(out_dir, utt_dir), join(out_dir, scheme_file), join(out_dir, file_id_scp))

    # generate utt from scheme file
    subprocess.call([festival_exe, '-b', join(out_dir, scheme_file)])

    # convert festival utt to lab
    subprocess.call([make_labels_exe, join(out_dir, label_dir), join(out_dir, utt_dir),
                     festival_dumpfeats, festival_utt_to_label])

    # normalize lab for merlin with options: state_align or phone_align
    normalize_lab_for_merlin(join(join(out_dir, label_dir), 'full'),
                             join(out_dir, label_dir), labels, join(out_dir, file_id_scp))

    # remove any un-necessary files
    print("Labels are ready in: " + join(out_dir, label_dir))


if __name__ == "__main__":
    # test
    job_id = uuid.uuid4().__str__()
    out_dir = join(temp_dir, job_id)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    create_labels('hello there my name is peter', out_dir)
