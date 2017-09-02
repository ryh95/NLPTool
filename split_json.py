import json

import numpy as np

#  change as you like
file_to_split = '/home/ryh/dataset/wiki-reading/validation-00001-of-00015.json'
file_sample = 500
file_num = 10
early_stop_num = 100000

with open(file_to_split,'r') as js_file:
    # raise json decode error
    # because it's not a standard json file
    # dataset = json.load(js_file)

    # remove json decode error
    correct_sample = []
    for i, line in enumerate(js_file):
        try:
            d = json.loads(line)

            correct_sample.append(line)
            # early stop to save memory
            if i > early_stop_num:
                break
        except json.decoder.JSONDecodeError:
            print('Error on line', i + 1, ':\n', repr(line))

    # write into output file
    N = len(correct_sample)

    for i in range(file_num):
        f = open('validation-'+str(i)+'.json','w')
        sample_indices = np.random.choice(N,file_sample,replace=False)

        for indice in sample_indices:
            f.write(correct_sample[indice])

