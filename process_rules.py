#!/usr/bin/env python3
import os
import re
import sys

def clean_name(name):
  """Convert section names to directory/file names by replacing spaces with hyphens and removing special characters."""
  # Remove newline characters
  name = name.replace('\n', '')

  # Remove any special characters that shouldn't be in filenames
  cleaned = re.sub(r'[^\w\s-]', '', name)
  # Replace spaces with hyphens
  cleaned = cleaned.replace(' ', '-').lower()
  return cleaned

def parse_rules(in_str):
  """Create filedict of the individual rules section, broken out by section and subsection"""
  output = {}

  # Use regex pattern to split input string into subsections (e.g. "1. Game Concepts")
  # This is the fuckin' worst lol.
  sections = re.split(r'(?:\n|^)(\d{1}\.\s.*?\n)', in_str)[1:]
  print(f"Sections: {len(sections) // 2}\n")
  for i, section_header in enumerate(sections[::2]):
    section_body = sections[2*i + 1]
    section_name = clean_name(section_header)
    print(f"Section {i + 1}: {section_name}")
    # print(f"Section body start: {section_body[0:20]}")

    subsections = re.split(r'(?:\n|^)(\d{3}\.\s.*?\n)', section_body)[1:]
    print(f"Subsections: {len(subsections) // 2}")
    for j, subsection_header in enumerate(subsections[::2]):
      subsection_body = subsections[2*j + 1]
      subsection_name = clean_name(subsection_header)
      print(f"Subsection {j}: {subsection_name}")

      output[f"rules/{section_name}/{subsection_name}.md"] = subsection_body.strip()

  return output

def process_file(input_file, output_dir):
    """Parse the rules file and organize it into markdown files."""
    with open(input_file, 'r') as file:
      content = file.read()

    # Instantiate output dict by filename
    output = {}

    # Step 1: Split files into subsection strings
    
    # 1a: Split intro from remainder
    start_index = content.find("Contents")
    if start_index != -1:
      output["INTRO.md"] = content[:start_index].strip()
      content = content[start_index:]
    
    # 1b: Split Table of Contents from remainder
    start_index = content.find("1. Game Concepts", 100, len(content)) # Skips duplicate header from top of TOC
    if start_index != -1:
      output["TABLE_OF_CONTENTS.md"] = content[:start_index].strip()
      content = content[start_index:]

    # 1c: Split off rules from remainder
    start_index = content.find("Glossary")
    if start_index != -1:
      output["RULES.md"] = content[:start_index].strip()
      content = content[start_index:]

    # 1d: Split off glossary from remainder
    start_index = content.find("Credits")
    if start_index != -1:
      output["GLOSSARY.md"] = content[:start_index].strip()
      content = content[start_index:]

    # 1e: Finish with credits.
    start_index=0
    output["CREDITS.md"] = content[:]

    # Process rules into subsections and add to output dict
    rules_dict = parse_rules(output["RULES.md"])
    output = {**output, **rules_dict}

    for filename in output.keys():
      print(filename)
      print()

    # Write the output to markdown files. Create subdirectories as needed
    for filename, content in output.items():

      # Skip fil
      if filename == "RULES.md":
        continue

      filedir = os.path.dirname(filename)
      if not os.path.exists(os.path.join(output_dir, filedir)):
        os.makedirs(os.path.join(output_dir, filedir))

      with open(os.path.join(output_dir, filename), "w") as f:
        f.write(content)
    

if __name__ == "__main__":
  if len(sys.argv) > 1:
    input_file = sys.argv[1]
  else:
    input_file = "in/rules.txt"
    if not os.path.exists(input_file):
      input_file = "in/rules-simple.txt"
  
  output_dir = "out"
  
  if len(sys.argv) > 2:
    output_dir = sys.argv[2]

  # Create out directory if it doesn't exist
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  
  process_file(input_file, output_dir)
