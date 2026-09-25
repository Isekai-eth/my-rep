"""Command-line interface for the clinical utility toolkit."""

import argparse

from .calculations import bmi


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate BMI.")
    parser.add_argument("--weight", type=float, required=True, help="Weight in kg")
    parser.add_argument("--height", type=float, required=True, help="Height in metres")
    args = parser.parse_args()
    print(f"BMI: {bmi(args.weight, args.height):.2f}")


if __name__ == "__main__":
    main()
