"""Funniest One-Line Out-of-Office Reply — one absurd instruction, no setup.

Writes the reply to /output/entry.txt (or $OUTPUT_DIR/entry.txt for local
tests). The gate requires UTF-8 text of 1 to 160 characters, so the reply is
written exactly, with no trailing newline.
"""

import os

REPLY = (
    "I'm out of the office until Monday. "
    "If your email is urgent, please send it again, but louder."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse.
    # The gate counts characters, so check both the character count and
    # the byte count: an over-long UTF-8 line must never reach the judge.
    if not 1 <= len(REPLY) <= 160:
        raise SystemExit(f"reply is {len(REPLY)} chars, must be 1-160")
    if len(REPLY.encode("utf-8")) > 160:
        raise SystemExit("reply is over 160 bytes")
    if REPLY != REPLY.strip() or "\n" in REPLY:
        raise SystemExit("reply must be a single clean line")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
