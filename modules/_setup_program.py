from modules.files import (check_file_exists, create_path, 
                           list_dir_files, read_any_file, read_json_file,
                           update_csv_columns, write_any_file)
from modules.program import get_path


def setup_program() -> None:
    '''
    Create program files and paths from Setup template
    files and check already existing files for needed updates
    comparing them with Setup files.
    
    The files and paths:
    - file "history.csv"
    - file "config.json"
    - path "data/errors_hangout"
    - file ".errors_info.json"
    - path "images_store"
    '''
    
    rule_paths = get_path(get_all_paths=True)
    setup_files_path = rule_paths['setup_files']

    # First create needed paths
    paths_setup = read_json_file(get_path('paths_setup'))
    for path in paths_setup:
        if not check_file_exists(path):
            create_path(path)
    
    # Then go thru files
    setup_files = list_dir_files(setup_files_path)
    for filename in setup_files:
        if filename.startswith('SETUP'):
            file, extention = filename.split('.')[1:]
            file_path = rule_paths[file]
            setup_file_content = read_any_file(
                f'{setup_files_path}/{filename}'
            )
            # If file exists, check if it needs an update
            if check_file_exists(file_path):
                existing_file_content = read_any_file(file_path)
                existing_file_content_UPD = existing_file_content.copy()

                if extention == 'json':
                    for key in setup_file_content:
                        if key not in existing_file_content:
                            existing_file_content_UPD[key] = \
                                                    setup_file_content[key]
                # If the setup CSV file has new columns,
                # update the existing file with the new ones
                if extention == 'csv':
                    if len(setup_file_content[0]) > \
                                            len(existing_file_content[0]):
                        new_columns = [colm for colm
                                       in setup_file_content[0]
                                       if colm not in
                                       existing_file_content[0]]
                        update_csv_columns(
                            file_path=file_path,
                            new_columns=new_columns
                        )

                if existing_file_content != existing_file_content_UPD:
                    write_any_file(
                        file_path=file_path,
                        content=existing_file_content_UPD
                    )
            else:
                write_any_file(
                    file_path=file_path,
                    content=setup_file_content
                )

    return 'done'


def integrity_check():
    pass