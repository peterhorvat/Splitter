import argparse

from src.splitting.excel import split

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="splitting.excel.split() generates separate Excel files for each page",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("src", help="Excel file location")
    parser.add_argument("--dest", help="Destination to save the generated files")

    args = parser.parse_args()
    split(args.src, dest=args.dest)
