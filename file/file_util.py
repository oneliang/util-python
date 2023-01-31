import os


def list_file_recursion(root_dir: str, suffix_array: [str]) -> []:
    """
    list file recursion
    :param root_dir:
    :param suffix_array:
    :return: []
    """
    file_list = []
    for filename in os.listdir(root_dir):
        pathname = os.path.join(root_dir, filename)
        if os.path.isfile(pathname):
            for suffix in suffix_array:
                if filename.endswith(suffix):
                    file_list.append(pathname)
                else:
                    pass
        else:  # is directory
            file_list.extend(list_file_recursion(pathname, suffix_array))
    return file_list


def delete_file(full_filename: str):
    if os.path.exists(full_filename):
        os.remove(full_filename)  # remove the file
