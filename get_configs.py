import os


def get_configs(file="config", local_file=True, return_length=None):
    if local_file:
        file = os.path.join(os.path.dirname(__file__), file)
    
    configs = []
    
    with open(file, 'r') as f:
        for line in f:
            conf = line[:line.find("#")].strip()
            if conf != '':
                configs.append(conf)
    
    if return_length is not None:
        configs += [None for _ in range(return_length - len(configs))]
    
    if len(configs) == 1:
        return configs[0]
    else:
        return configs
