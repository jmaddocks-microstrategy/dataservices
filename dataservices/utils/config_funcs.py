
def read_config_value(section, key):
    from dataservices.utils.file_funcs import get_config
    config = get_config()
    return config[section][key]