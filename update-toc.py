#!/usr/bin/env python3
# pip install PyYAML

import os
import re
import yaml

if __name__ == "__main__":
    readme = ""
    with open("README.md", "r") as f:
        readme = f.read()
        match = re.search("## Table of contents", readme)
        if match:
            readme = readme[0:match.end()] + "\n"
    
    links = {}
    for filename in list(sorted(os.listdir())):
        if filename.endswith(".md") and filename != "README.md":
            with open(filename, "r") as f:
                if f.readline() == "---\n":
                    fm = yaml.safe_load(f.readline() + "\n" + f.readline())
                    if fm["category"] in links.keys():
                        links[fm["category"]].append("- [" + fm["title"] + "](" + filename + ")")
                    else:
                        links[fm["category"]] = ["- [" + fm["title"] + "](" + filename + ")"]
                else:
                    print("No frontmatter found in file: " + filename)

    with open("README.md", "w") as f:
        f.write(readme + "\n")
        for category in list(sorted(links.keys())):
            f.write("### " + category + "\n")
            for link in links[category]:
                f.write(link + "\n")
            f.write("\n")