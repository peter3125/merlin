## Build your own Voice - Setup Ubuntu 16.04

```
mkdir -p database/wav
mkdir -p database/txt
mkdir -p database/labels
mkdir -p database/labels/label_state_align
mkdir -p database/feats

# proceed by extracting x wav files into the above wav directory, all 16KHz, mono 16 bit
# and an equivalent same named number of txt files into the txt directory
# my example here assumes 115 files total, 5 test, 5 validate (defaults) and 105 training files

export voice=jc

./01_setup.sh $voice
./02_prepare_labels.sh database/wav database/txt database/labels

# step 3 doesn't work well - do it manually
/opt/merlin/misc/scripts/vocoder/world/extract_features_for_merlin.sh /opt/merlin /opt/merlin/egs/build_your_own_voice/s1/database/wav /opt/merlin/egs/build_your_own_voice/s1/database/feats 16000
cp -r /opt/merlin/egs/build_your_own_voice/s1/database/feats/* ./experiments/$voice/acoustic_model/data

# check all the required files match before running the setup files
python consistency_check.py

./04_prepare_conf_files.sh conf/global_settings.cfg
sed -i 's/^Train=.*/Train=305/g' conf/*.cfg
sed -i 's/^train_file_number.*/train_file_number: 305/g' conf/*.conf

./05_train_duration_model.sh conf/duration_${voice}.conf
./06_train_acoustic_model.sh conf/acoustic_${voice}.conf
```
