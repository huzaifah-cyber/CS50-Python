# If the input does not contain any such URL at all, return None.
#  http://youtube.com/embed/xvFZjo5PgG0
#  https://youtube.com/embed/xvFZjo5PgG0
#  https://www.youtube.com/embed/xvFZjo5PgG0
#  GOAL = https://youtu.be/xvFZjo5PgG0
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"
# frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^<iframe (?:width=\d+ height=\d+ )?src=https?://(?:www\.)?youtube\.com/embed/(\w+)", s.replace("\"", "")):
        return "https://youtu.be/"+match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()