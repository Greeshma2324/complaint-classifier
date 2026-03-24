import csv

# Allowed categories
CATEGORIES = [
    "Pothole", "Flooding", "Streetlight", "Waste", "Noise",
    "Road Damage", "Heritage Damage", "Heat Hazard", "Drain Blockage", "Other"
]

URGENT_KEYWORDS = ["injury", "child", "school", "hospital", "ambulance", "fire", "hazard", "fell", "collapse"]

def classify_complaint(text):
    text_lower = text.lower()

    # Category detection (simple logic)
    if "pothole" in text_lower:
        category = "Pothole"
    elif "water" in text_lower or "flood" in text_lower:
        category = "Flooding"
    elif "light" in text_lower:
        category = "Streetlight"
    elif "garbage" in text_lower or "waste" in text_lower:
        category = "Waste"
    elif "noise" in text_lower:
        category = "Noise"
    elif "road" in text_lower:
        category = "Road Damage"
    elif "heat" in text_lower:
        category = "Heat Hazard"
    elif "drain" in text_lower:
        category = "Drain Blockage"
    else:
        category = "Other"

    # Priority
    if any(word in text_lower for word in URGENT_KEYWORDS):
        priority = "Urgent"
    else:
        priority = "Standard"

    # Reason (simple)
    reason = text[:50]

    # Flag
    if category == "Other":
        flag = "NEEDS_REVIEW"
    else:
        flag = ""

    return category, priority, reason, flag


def process_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["category", "priority", "reason", "flag"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            text = row["complaint"]
            category, priority, reason, flag = classify_complaint(text)

            row["category"] = category
            row["priority"] = priority
            row["reason"] = reason
            row["flag"] = flag

            writer.writerow(row)


if __name__ == "__main__":
    process_csv("input.csv", "output.csv")