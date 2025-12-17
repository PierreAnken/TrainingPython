import random
import string

def random_name(prefix="node"):
    suffix = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"{prefix}_{suffix}"


def generate_structure(depth, max_children):
    root = {"name": random_name("root"), "children": []}

    current_level = [root]

    for _ in range(depth):
        next_level = []

        for node in current_level:
            num_children = random.randint(0, max_children)

            for _ in range(num_children):
                child = {
                    "name": random_name("node"),
                    "children": []
                }
                node["children"].append(child)
                next_level.append(child)

        current_level = next_level

    return root
