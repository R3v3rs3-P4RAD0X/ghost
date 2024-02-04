# This is a simple script used to run any terminal command easily

import subprocess

# Usage:
# term = Term()
# term.set_command("ls").add_argument("-l").run()
# print(term.get_result())
# term.reset()

class Term:
    command: str
    args: list[str]
    result: dict[str, any]

    def __init__(self):
        self.command = ""
        self.args = []
        self.result = {
            "output": "",
            "success": False
        }

    def reset(self):
        self.command = ""
        self.args = []
        self.result = {
            "output": "",
            "success": False
        }

    def set_command(self, command: str):
        self.command = command
        return self
    
    def add_argument(self, arg: str):
        self.args.append(arg)
        return self

    def add_arguments(self, *args: str):
        self.args.extend(args)
        return self

    def run(self):
        try:
            # Run the command using subprocess
            result = subprocess.run([self.command, *self.args], capture_output=True, text=True, check=True)
            self.result["output"] = result.stdout
            self.result["success"] = True
        except subprocess.CalledProcessError as e:
            self.result["output"] = e.output
            self.result["success"] = False
        return self

    def get_result(self):
        return self.result

    def get_output(self):
        return self.result["output"]

    def passed(self):
        return self.result["success"]

# Testing using if ran directly
if __name__ == "__main__":
    term = Term()
    term.set_command("ls").add_argument("-l").run()
    print(term.get_result())
    term.reset()
    
