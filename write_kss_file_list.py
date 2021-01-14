from glob import glob
import random
import os

ROOT_DATA = 'KSS'

DATA_PATH = f'{ROOT_DATA}/wavs'

TRAINING_FILE_NAME = f'{ROOT_DATA}/training.txt'
VALIDATION_FILE_NAME = f'{ROOT_DATA}/validation.txt'

NUM_VALID = 150

files = [os.path.basename(f).replace('.wav', '') for f in sorted(glob(os.path.join(DATA_PATH, '*.wav')))]

print(f'* Found {len(files):05d} wav files inside {DATA_PATH}')

random.shuffle(files)

validation_files = sorted(files[:NUM_VALID])
training_files = sorted(files[NUM_VALID:])

with open(TRAINING_FILE_NAME, 'w') as f:
    for i, file_name in enumerate(training_files):
         f.write(file_name + '|' + '\n')     

print(f'* Wrote {i+1:05d} files in {TRAINING_FILE_NAME}')

with open(VALIDATION_FILE_NAME, 'w') as f:
    for i, file_name in enumerate(validation_files):
         f.write(file_name + '|' + '\n')     

print(f'* Wrote {i+1:05d} files in {VALIDATION_FILE_NAME}')


