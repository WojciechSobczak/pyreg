import os
import subprocess
import shutil

SCRIPT_DIR = os.path.normpath(os.path.dirname(os.path.realpath(__file__))).replace('\\', '/')
BUILD_DIR = f'{SCRIPT_DIR}/.build'

def main():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)        
    os.makedirs(BUILD_DIR)

    proc = subprocess.run(args=' && '.join([
        "python3 -m build --sdist --wheel --no-isolation --outdir . .."
    ]), shell=True, cwd=BUILD_DIR)
    
    if proc.returncode != 0:
        print(f"[ERROR] Building package failed. Process code: {proc.returncode}")
        return 1
    
    shutil.move(f'{SCRIPT_DIR}/pyreg.egg-info', f'{BUILD_DIR}/pyreg.egg-info')
    shutil.move(f'{SCRIPT_DIR}/build', f'{BUILD_DIR}/build')


if __name__ == "__main__":
    exit(main())