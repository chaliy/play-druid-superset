# %%
import subprocess

def run_superset_command(cmd: list[str]):
    subprocess.call(["docker", "compose", "exec", "-it", "superset", "superset"] + cmd)


# Setups from https://hub.docker.com/r/apache/superset#!

run_superset_command(["fab", "create-admin", 
    "--username", "admin", 
    "--firstname", "Superset", 
    "--lastname", "Admin",
    "--email", "admin@superset.com",
    "--password", "password1"
])

run_superset_command(["db", "upgrade"])

# run_superset_command(["load_examples"])

run_superset_command(["init"])

print("Done!")

# %%
