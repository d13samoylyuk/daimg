from functools import wraps
import os
import traceback

from modules.basic import define_id
from modules.files import read_json_file, update_json_file, write_file
from modules.program import get_path
from modules.times import time_now

# Needed to inform user
ERROR_REPORT = {
    'report path': None,
    'message': None
}


class DaimngError(Exception):
    def __init__(self, error_name: str,
                 service_name: str = None,
                 error_info: str = None
        ) -> None:

        self.error_name = error_name
        self.service_name = service_name
        self.error_description = error_info
    
    def __str__(self) -> str:
        return (f'Error {self.error_name} in {self.service_name}'
                f'\nDetails: {self.error_description}')


def error_report():
    def __error_report(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            try:
                result = old_function(*args, **kwargs)
                return result
            except Exception as error:
                save_error_report(error)
                raise
        return new_function
    return __error_report


def save_error_report(exception: Exception) -> None:
    report_text = create_error_report(exception)
    errors_store_path = get_path('errors_hangout')
    file_name = make_error_file_name(time_now(nice_format=True))
    file_path = errors_store_path + '/' + file_name
    write_file(file_path, report_text)

    abs_file_path = os.path.abspath(file_path)
    ERROR_REPORT['report path'] = f'{abs_file_path}'

    if isinstance(exception, DaimngError):
        errors_uncode = read_json_file(get_path('errors_uncode'))
        ERROR_REPORT['message'] = (errors_uncode
            [exception.service_name][exception.error_name])


def create_error_report(exception: Exception) -> str:
    time_ = time_now(nice_format=True)
    report_text = f'''\
Error occured at {time_}

Error message:
{exception}

ERROR TRACEBACK:
{traceback.format_exc()}
'''
    return report_text


def make_error_file_name(error_time: str) -> str:
    errors_info_path = get_path('errors_info')

    errors_info = read_json_file(errors_info_path)
    err_num = errors_info['last_error_id'] + 1

    err_id = define_id(
        errors_info['last_error_id'] + 1,
        prefix='err-',
        max_id_lenth=0
    )

    update_json_file(errors_info_path, 'last_error_id', err_num)

    return f'{err_id}_{error_time}.txt'