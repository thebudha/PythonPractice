import os


def read_file(filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8-sig') as file:
                content = file.read().splitlines()
            if content:
                print('\n'.join(content))
            return content

        with open(filename, 'w', encoding='utf-8') as file:
            pass
        return []
    except OSError:
        print(f"{filename} could not be opened.")
        raise


def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(content))
        print(f"{filename} saved.")
    except OSError:
        print(f"{filename} could not be saved.")
        raise

def prompt_user(filename, content):
    print("Type text to add to the file, 'SAVE' to save and exit, or 'EXIT' to leave without saving.")
    while True:
        line = input()
        if line == 'SAVE':
            return content
        if line == 'EXIT':
            print(f"{filename} not saved.")
            raise SystemExit
        content.append(line)


def main():
    filename = input("Enter the filename to open or create: ").strip()

    try:
        content = read_file(filename)
    except OSError:
        return

    try:
        content = prompt_user(filename, content)
    except SystemExit:
        return

    try:
        write_file(filename, content)
    except OSError:
        return


if __name__ == "__main__":
    main()