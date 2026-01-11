#!/usr/bin/env python3
import sys

def convert_cnf_simple(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read().splitlines()

    var_count = 0
    clause_count = 0
    show_vars = []
    clauses = []

    for line in content:
        line = line.strip()
        if not line:
            continue

        if line.startswith('p cnf'):
            parts = line.split()
            var_count = int(parts[2])
            clause_count = int(parts[3])
            continue

        if line.startswith('c p show'):
            parts = line.split()
            show_vars = [int(x) for x in parts[3:] if x != '0']
            continue

        if not line.startswith('c'):
            clauses.append(line)

    # Prepare output
    output_lines = []
    output_lines.append(f"p cnf {var_count} {clause_count}")

    # Add 'a' line (existential variables)
    if show_vars:
        output_lines.append('a ' + ' '.join(str(v) for v in show_vars) + ' 0')
    else:
        output_lines.append('a 0')

    # Add 'e' line (universal variables)
    all_vars = list(range(1, var_count + 1))
    universal_vars = [v for v in all_vars if v not in show_vars]

    if universal_vars:
        output_lines.append('e ' + ' '.join(str(v) for v in universal_vars) + ' 0')
    else:
        output_lines.append('e 0')

    # Add clauses
    output_lines.extend(clauses)

    # Write output
    with open(output_file, 'w') as f:
        f.write('\n'.join(output_lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.cnf output.cnf")
        sys.exit(1)

    convert_cnf_simple(sys.argv[1], sys.argv[2])
    print(f"Converted {sys.argv[1]} to {sys.argv[2]}")
