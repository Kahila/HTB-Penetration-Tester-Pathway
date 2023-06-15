import os

class clrs:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

print(clrs.OKBLUE + clrs.BOLD + 'Creating project directories' + clrs.ENDC)
print(clrs.OKBLUE + f'path: {clrs.ENDC} {clrs.OKGREEN + clrs.BOLD}' + os.getcwd() + clrs.ENDC)
project_name = input(f"{clrs.OKBLUE}input project name:{clrs.ENDC}")

directories = ["","/EPT", "/EPT/evidence", "/EPT/evidence/credentials", "/EPT/evidence/data", "/EPT/evidence/screenshots", "/EPT/log", "/EPT/scans", "/EPT/scope", "/EPT/tools",
               "/IPT", "/IPT/evidence", "/IPT/evidence/credentials", "/IPT/evidence/data", "/IPT/evidence/screenshots", "/IPT/log", "/IPT/scans", "/IPT/scope", "/IPT/tools"]

for directory in directories:
    os.mkdir(project_name + directory)
    print(clrs.OKGREEN  + f"Created directory:{clrs.ENDC} {project_name}{directory}")