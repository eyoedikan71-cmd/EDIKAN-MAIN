import argparse
parser = argparse.ArgumentParser(description="Simple argparse demo.")
parser.add_argument("name", type=str, default="students", help="Your name")

args = parser.parse_args()

name = args.name
print(name)