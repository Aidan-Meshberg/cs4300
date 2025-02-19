import subprocess

def testHelloWorld():
    assert subprocess.run(["python3", "task1.py"], capture_output=True, text=True).stdout.strip() == "hello world"