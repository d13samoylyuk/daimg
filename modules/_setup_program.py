from modules.files import check_file_exists, create_folder, write_file
from modules.program import get_path

sys_files_contents = {
    "history": "id,file_name,date,description\n",

    "config": ('{'
    '"imgs_path": null'
    '}'),

    "errors_info": ('{'
    '"last_error_id": 0'
    '}')
}


def setup_program():
    '''
    Check if exists and create files:
    - file "history.csv"
    - file "config.json"
    - path "data/errors_hangout"
    - file ".errors_info.json"
    - path "images"
    '''

    files_required = [
        'history',
        'config',
        'errors_hangout',
        'errors_info'
        ]
    
    for item in files_required:
        path = get_path(item)
        if item in sys_files_contents:
            if not check_file_exists(path):
                write_file(path, sys_files_contents[item])
        else:
            if not check_file_exists(path):
                create_folder(path)


def integrity_check():
    pass