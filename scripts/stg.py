import click
import subprocess

@click.group()
def cli():
    pass



@cli.command()
@click.option("--local-ip", default="127.0.0.1", help="local ip that docker can reach to deploy log4j exploit")
def do_log4j(local_ip):
    subprocess.call(("bash do_log4j_nohands.sh " + local_ip).split(" "))

def main(do_it: str):
    if do_it == "log4j":
        do_log4j()
    elif do_it == "atomicred":
        pass

if __name__ == "__main__":
    cli()
# @click.option("--module", help="Choose from log4j or Atomic Red Team")