"""Entry poin for the smart calculator CLI."""

from src.calculator import Calculator
from src.utils import is_exit_command

def main() -> None:
    calc = Calculator()

    print("Smart Calculator")
    print("Type expressions like '10 + 5' or '200 % 10'.")
    print("Type 'quit' or 'exit' to leave.\n")

    while True:
      try:
        raw = input(">").strip()
      except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        break

      if is_exit_command(raw):
        print("Goodbye!")
        break

      if not raw:
        continue

      result = calc.evaluate(raw)
      print(f"= {result}\n")

if __name__ == "__main__":
    main()