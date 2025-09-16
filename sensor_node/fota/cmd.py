import subprocess

def push_fota():
    cmd = ['test_ota_win_x86.exe com']
    cwd = 'C:/Users/Administrator/Desktop/Kone_SensorNode-SensorNode.hw_v1-0.0.2-user-65670dc10/fota/tools'

    result = subprocess.run(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    print("Return code:", result.returncode)

push_fota()