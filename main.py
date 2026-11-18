# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt, the same bytes on every run.
# No network, no randomness, no clock: the text is a constant, so the two
# grader runs cannot differ. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space; the judge reads exactly the
# bytes written, line ends included, so every line end here is deliberate.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "All day the words have come in a hurry, each one asking for an answer. "
    "Here, none of them do.\n"
    "\n"
    "The light is the low amber of late afternoon, moving across the "
    "floorboards the way it always has, in no particular hurry. Dust drifts "
    "in it, taking its time. Somewhere a tap is dripping into the sink, one "
    "drop at a time, keeping time nobody is watching.\n"
    "\n"
    "There is a chair by the window with nothing on it but the light, and "
    "the evening has already decided to be long. The dust will still be "
    "drifting when you look again, and the light, and the slow dripping, "
    "and none of them will ask you for a thing."
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
