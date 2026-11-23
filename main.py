import os
import sys

# Dad Joke Showdown — one dad joke, composed from its two beats:
# the setup (a dad goes shopping for dad jokes) and the punchline
# (the clerk answers with the joke itself: aisle = I'll).
setup = "I asked the grocery clerk if they had any dad jokes."
punchline = "He said, 'Aisle be right back with one.'"
line = setup + " " + punchline

print(line)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)

data = line.encode("utf-8")
# The gate counts characters (1-200), not bytes: assert on chars first.
assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
assert 1 <= len(data) <= 200, f"entry must be 1-200 bytes, got {len(data)}"
assert len(line.strip()) > 0
# The turn must survive assembly: the connector homophone ("Aisle" = "I'll")
# is in the punchline, the punchline is the last beat, and nothing follows it.
assert "Aisle" in punchline, "punchline lost its connector"
assert line.endswith(punchline), "punchline must arrive at the end"
assert "  " not in line, "no doubled spaces in the delivered line"
# Round-trip check: what the grader reads must be exactly the line.
assert open("/output/entry.txt", encoding="utf-8").read() == line
sys.exit(0)
