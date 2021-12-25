import argparse
import os
import random
import time

from colors import COLORS

TREE_STUMP = "|l lI |         "


def draw_tree(height=3, width=5):
    tree = [COLORS.YELLOW2.value + "★         "]

    for i in range(height):
        for j in range(width):
            leaves = "*" * (2 * (j + 2 * i) + 3)
            leaves = list(leaves)
            leaves[0] = COLORS.GREEN.value + "*" + leaves[0]

            random_index = random.randint(0, len(leaves) - 1)
            leaves[random_index] = (
                str(random.choice(list(COLORS)).value)
                + leaves[random_index]
                + COLORS.GREEN.value
            )
            leaves = "".join(leaves)
            tree.append(leaves)

    for _ in range(height):
        tree.append(COLORS.YELLOW.value + TREE_STUMP)

    print("\n".join(leaf.center(os.get_terminal_size().columns) for leaf in tree))


if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument(
        "-b",
        "--branch",
        type=int,
        default=3,
        help="Tree height. It will define the number of branches. Tree height ≥ 1",
    )
    args.add_argument(
        "-w",
        "--width",
        type=int,
        default=5,
        help="Tree width. It will define the number of leaves in its branch. Tree width ≥ 5",
    )
    config = args.parse_args()

    if config.branch < 1 or config.width < 5:
        args.error(
            "Please check branch or width value.\n\nTree height ≥ 1\nTree width ≥ 5\n"
        )

    while True:
        try:
            time.sleep(random.uniform(0.1, 0.3))
            os.system("cls" if os.name == "nt" else "clear")
            draw_tree(height=config.branch, width=config.width)
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")
            break
