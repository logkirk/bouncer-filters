import json

from pathlib import Path

# Indentation for statistics output
INDENT = 4

# Define paths
INPUT_LIST = Path("input_list.txt")

WORD_LIST_DIR = Path("word_lists")
SOFT_COMMON_WORD_LIST = Path(WORD_LIST_DIR / "word_list_soft.txt")
STRICT_COMMON_WORD_LIST = Path(WORD_LIST_DIR / "word_list_strict.txt")

OUTPUT_DIR = Path("output")
OUTPUT_LIST_SOFT = Path(OUTPUT_DIR / "filter_list_soft.txt")
OUTPUT_LIST_STRICT = Path(OUTPUT_DIR / "filter_list_strict.txt")
OUTPUT_JSON_SOFT = Path(OUTPUT_DIR / "filter_list_soft.json")
OUTPUT_JSON_STRICT = Path(OUTPUT_DIR / "filter_list_strict.json")

# Read in word lists
with open(INPUT_LIST, "r") as f:
    input_words = f.readlines()

with open(SOFT_COMMON_WORD_LIST, "r") as f:
    soft_common_words = f.readlines()

with open(STRICT_COMMON_WORD_LIST, "r") as f:
    strict_common_words = f.readlines()

# Strip newlines
input_words = [word.strip() for word in input_words]
soft_common_words = [word.strip() for word in soft_common_words]
strict_common_words = [word.strip() for word in strict_common_words]

excluded_words_soft = []
passed_words_soft = []
excluded_words_strict = []
passed_words_strict = []
num_excluded_soft = 0
num_excluded_strict = 0
num_total = 0

# Filter words
for word in input_words:
    num_total += 1
    if word in soft_common_words:
        num_excluded_soft += 1
        excluded_words_soft.append(word)
    else:
        passed_words_soft.append(word)

    if word in strict_common_words:
        num_excluded_strict += 1
        excluded_words_strict.append(word)
    else:
        passed_words_strict.append(word)

# Intersect sets to determine which words were filtered by both lists
soft_set = set(excluded_words_soft)
strict_set = set(excluded_words_strict)
both_set = soft_set.intersection(strict_set)

# Remove words filtered by both lists
soft_set.difference_update(both_set)
strict_set.difference_update(both_set)

# Write output word lists
with open(OUTPUT_LIST_SOFT, "w+") as f:
    for word in passed_words_soft:
        f.write(word + "\n")

with open(OUTPUT_LIST_STRICT, "w+") as f:
    for word in passed_words_strict:
        f.write(word + "\n")

# Write output JSON filter lists
with open("template.json", "r") as f:
    template = json.load(f)

json_soft = [dict(template, phrase=word) for word in passed_words_soft]
with open(OUTPUT_JSON_SOFT, "w", encoding="utf-8") as f:
    json.dump(json_soft, f, ensure_ascii=True, indent=4)  # noqa

json_strict = [dict(template, phrase=word) for word in passed_words_strict]
with open(OUTPUT_JSON_STRICT, "w", encoding="utf-8") as f:
    json.dump(json_strict, f, ensure_ascii=True, indent=4)  # noqa

# Print statistics
print(f"Excluded only by the soft list ({SOFT_COMMON_WORD_LIST}):")
for word in soft_set:
    print(INDENT * " " + word)

print(f"\nExcluded only by the strict list ({STRICT_COMMON_WORD_LIST}):")
for word in strict_set:
    print(INDENT * " " + word)

print(f"\nExcluded by both lists:")
for word in both_set:
    print(INDENT * " " + word)

print("\nSummary")
print("=======")
print(INDENT * " " + "Total input words:", num_total)
print(INDENT * " " + "Excluded only by the soft list:", len(soft_set))
print(INDENT * " " + "Excluded only by the strict list:", len(strict_set))
print(INDENT * " " + "Excluded by both lists:", len(both_set))
print(INDENT * " " + "Total soft-filtered output words:", len(passed_words_soft))
print(INDENT * " " + "Total strict-filtered output words:", len(passed_words_strict))
