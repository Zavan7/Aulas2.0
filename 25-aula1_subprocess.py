import subprocess


cmd = ['ping', '10.10.10.36']

proc = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding='cp850'
    )

print()

# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)