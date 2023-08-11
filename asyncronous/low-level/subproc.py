

import asyncio


async def run_sub_process(cmd: str):

    proc = await asyncio.create_subprocess_shell(
        cmd, 
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    if proc:
        print(f"child process {cmd} with pid: {proc.pid} created.")

    (stdout, stderr) = await proc.communicate()

    print(f"[{cmd} exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout: \n {stdout.decode()}]")
    if stderr:
        print(f"[stderr: ]\n {stderr.decode()}")

# asyncio.run(run_sub_process("ls --recursive"))


async def main():
    await asyncio.gather(
        run_sub_process("ls"),
        run_sub_process('sleep 1; echo "hello"'),
        # run_sub_process(" echo ?")
    )

asyncio.run(main())