import os
def getsonglist(internal, external):
    my_dict = {}
    print('getting songs')
    if internal is not None:
        for subdir, dirs, files in os.walk(internal):
            for filename in files:
                filepath = subdir + os.sep + filename
                if filepath.endswith(".mp3") or filepath.endswith(".wav"):
                    split = filepath.split('/')
                    my_dict[split[-1]] = filepath
    if external is not None:
        for subdir, dirs, files in os.walk(external):
            for filename in files:
                filepath = subdir + os.sep + filename
                if filepath.endswith(".mp3") or filepath.endswith(".wav"):
                    split = filepath.split('/')
                    my_dict[split[-1]] = filepath
    print('got songs')
    return my_dict
