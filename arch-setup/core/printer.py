"""
This file handles everything related to printing to the console
"""

class Printer:
    def __init__(self):
        pass

    def colourise(self, content: str, colour: str) -> str:
        """
        Colourise the content
        """
        colours = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
        return colours[colour] + content + colours["reset"]

    def print(self, content: str, colour: str = "white") -> None:
        """
        Print the content
        """
        print(self.colourise(content, colour))

    def print_error(self, content: str) -> None:
        """
        Print the content in red
        """
        self.print(content, "red")

    def print_success(self, content: str) -> None:
        """
        Print the content in green
        """
        self.print(content, "green")

    def print_warning(self, content: str) -> None:
        """
        Print the content in yellow
        """
        self.print(content, "yellow")

    def print_info(self, content: str) -> None:
        """
        Print the content in blue
        """
        self.print(content, "blue")

    def print_bold(self, content: str) -> None:
        """
        Print the content in bold
        """
        print("\033[1m" + content + "\033[0m")

# Testing if ran directly
if __name__ == "__main__":
    printer = Printer()
    printer.print("This is a test")
    printer.print_error("This is an error")
    printer.print_success("This is a success")
    printer.print_warning("This is a warning")
    printer.print_info("This is an info")
    printer.print_bold("This is bold")
