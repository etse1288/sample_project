from typing import List
from pathlib import Path
import shutil

def task_hello():
    return {
        "actions": ['echo hello'],
    }
    
def remove_directory(dirnames: List[str]):
    for dirname in dirname:
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
            # clean_targets,
            'echo ok',
            (remove_directory, ['build', 'src/test2.egg-info']),
        ],
        'targets': [
            'dist', 'build', 'src\\*.egg-info',
        ]
    }        