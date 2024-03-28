from pathlib import Path
from functools import partial
import shutil

def task_hello():
    return {
        "actions": ['echo hello'],
    }
    
def remove_directory(dirname: str):
    if Path(dirname).exists():
        shutil.rmtree(dirname)

def eric(xx: str = 'eric'):
    print('hello', xx)
    
def task_build_clean():
    return {
        "actions": [
            'echo clean',
            eric,
        ]
    }    
    
from doit.task import clean_targets
def task_build():
    return {
        "actions": [
            'echo build',
            'pip wheel -w dist . --no-deps',
        ],
        "clean": [
            clean_targets,
            'echo ok',
            # partial(remove_directory, 'dist'),
            # partial(remove_directory, 'build'),
            # partial(remove_directory, 'src/test2.egg-info'),
        ],
        'targets': [
            'dist', 'build', 'src\\*.egg-info',
        ]
    }        