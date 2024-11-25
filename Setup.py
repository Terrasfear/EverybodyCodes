import os

year = "2024"
challenge = input("Generate folders for challenge number:")
challenge = int(challenge)

challenge_str = f"Challenge_{challenge}"

files = os.listdir('.')
if not any([i == year for i in files]):
    print(f"Start of the year {year}, good luck")
    os.makedirs(f"./{year}")

files = os.listdir(f'./{year}')
if any([i == challenge_str for i in files]):
    print(f"Folder {challenge_str} already exists")
else:
    print(f"Making folder {challenge_str}")
    os.makedirs(f"./{year}/{challenge_str}")

files = os.listdir(f'./{year}/{challenge_str}')
planned_files = [f'{challenge_str}.py', 'Input_1', 'Input_2', 'Input_3']

for plan in planned_files:
    if not any(i == plan for i in files):
        print(f"\tmaking file: {plan}")
        open(f"./{year}/{challenge_str}/{plan}", 'x')
