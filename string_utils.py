def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def split_before_each_uppercases(formula):
    end = 1
    start = 0
    split_formula = []
    if formula != "":
        for i in range(1, len(formula)):
            if formula[i].isupper():
                end = i
                split_formula.append(formula[start:end])
                start = i
        split_formula.append(formula[start:len(formula)])
        return split_formula
    else:
        return []

def split_at_digit(formula):
    digit_location = 1
    for i in range(1, len(formula)):
        if formula[i].isdigit():
            break
        else:
            digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric = int(formula[digit_location:])
        return prefix, numeric

def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_before_each_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        if atom_name in atom_counts:
            atom_counts[atom_name] += atom_count
        else:
            atom_counts[atom_name] = atom_count
    return atom_counts

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
