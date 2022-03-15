"""script to remove the version numbers from pip freeze txt files so that
    calls to pip install -r will grab the newest version of the package in
    an attempt to avoid compatibility issues."""
import argparse


def main(filename: str) -> None:
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if '==' not in line:
                # the entire line will be simply returned, don't add \n
                continue
            lines[i] = f"{line.split('==')[0]}\n"
        f.seek(0)  # jump to beginning of file
        f.truncate()  # clear the file from the beginning onwards
        f.writelines(lines)  # add the modified lines to the blank file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True,
                        help='filename, eg. `requirements.txt`')
    filename = parser.parse_args().file
    main(filename)
