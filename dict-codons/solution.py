#!/usr/bin/env python3
"""Codon/Amino Acid table conversion"""

codon_table = """
Isoleucine    ATT ATC ATA
Leucine       CTT CTC CTA CTG TTA TTG
Valine        GTT GTC GTA GTG
Phenylalanine TTT TTC
Methionine    ATG
Cysteine      TGT TGC
Alanine       GCT GCC GCA GCG
Glycine       GGT GGC GGA GGG
Proline       CCT CCC CCA CCG
Threonine     ACT ACC ACA ACG
Serine        TCT TCC TCA TCG AGT AGC
Tyrosine      TAT TAC
Tryptophan    TGG
Glutamine     CAA CAG
Asparagine    AAT AAC
Histidine     CAT CAC
Glutamic_acid GAA GAG
Aspartic_acid GAT GAC
Lysine        AAA AAG
Arginine      CGT CGC CGA CGG AGA AGG
Stop          TAA TAG TGA
"""

aa2codons = {}
for line in codon_table.strip().splitlines():
    [aa, codons] = line.split(maxsplit=1)
    aa2codons[aa] = codons.split()

print('AA -> codons')
print(aa2codons)

codon2aa = {}
for aa, codons in aa2codons.items():
    for codon in codons:
        codon2aa[codon] = aa

print('Codon -> AA')
print(codon2aa)
