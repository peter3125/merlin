import os, sys, glob
import collections


def readtext(fname):
    f = open(fname, 'r')
    data = f.read()
    data = data.strip(' \n')
    f.close()
    return data


def create_dictionary_from_txt_file(filename, text):
    utt_text = {}
    for newline in text.split('\n'):
        newline = newline.strip()
        newline = newline.replace('(', '')
        newline = newline.replace(')', '')

        if text[0] == '"' and text[-1] == '"':
            text = text[1:-1]  # remove beginning and end double quotes

        utt_text[filename] = text

    return utt_text


# Usage: python genScmFile.py <in_text> <out_utt_dir> <out_scm_file> <out_file_id_list>
def gen_scheme_file(in_text, out_utt_dir, out_scm_file, out_id_file, text_filename='001'):

    if not os.path.exists(out_utt_dir):
        os.makedirs(out_utt_dir)

    utt_text = create_dictionary_from_txt_file(text_filename, in_text)
    sorted_utt_text = collections.OrderedDict(sorted(utt_text.items()))

    out_f1 = open(out_scm_file, 'w')
    out_f2 = open(out_id_file, 'w')

    for utt_name, sentence in sorted_utt_text.items():
        out_file_name = os.path.join(out_utt_dir, utt_name+'.utt')
        sentence = sentence.replace('"', '\\"')
        out_f1.write("(utt.save (utt.synth (Utterance Text \""+sentence+"\" )) \""+out_file_name+"\")\n")
        out_f2.write(utt_name+"\n")

    out_f1.close()
    out_f2.close()
