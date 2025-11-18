import os
import sys

path = sys.argv[1]  # ex: "domains/user/profile"

full_path = os.path.join("src", path)

os.makedirs(full_path, exist_ok=True)

init_file = os.path.join(full_path, "__init__.py")
if not os.path.exists(init_file):
    open(init_file, "w").close()

print(f"Created module: {full_path}")
