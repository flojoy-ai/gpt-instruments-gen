import os
import re


def replace_spaces_with_hyphen(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                # this first replaces all the spaces with hyphens
                # if there are multiple spaces, it will replace them with a single hyphen
                # then it removes the hyphen at the beginning and end of the string
                new_filename = re.sub(r"\s+", "-", filename)[:-3].strip("-") + ".md"

                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)

                os.rename(old_path, new_path)


if __name__ == "__main__":
    directory_path = "docusaurus"
    replace_spaces_with_hyphen(directory_path)
