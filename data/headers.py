GOLDEN_FIRST_ROW = [
    "Paper No., Page No.", "First Author", "Part No.", "Type", "Manufacture",
    "Data", "", "Total Ionizing Dose", "", "", "",
    "Single Event Effects, H-heavy ion, P-proton, L-laser, N-neutrons", "", "",
    "", "", "", "", "Displacement Damage", "", "", "", "", ""
]
GOLDEN_SECOND_ROW = [
    "", "", "", "", "", "Terrestrial", "Flight", "Co60", "ELDRS", "Protons",
    "Electrons", "SEU", "SET", "SEFI", "SEL", "SEB", "SEGR", "Dose Rate",
    "Protons", "Neutrons", "", "", "", ""
]

FIRST_ROW_LOOKUP = {name: num for num, name in enumerate(GOLDEN_FIRST_ROW)}
SECOND_ROW_LOOKUP = {name: num for num, name in enumerate(GOLDEN_SECOND_ROW)}
