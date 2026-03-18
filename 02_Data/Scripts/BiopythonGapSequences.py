# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:48:43 2026

@author: moyar
"""

from Bio import SeqIO
from Bio.Seq import Seq, MutableSeq
from Bio.SeqRecord import SeqRecord
import os

input_fasta = "AAA35797.fasta"
output_dir = "output"
deletion_sizes = [10, 30]   # as in Golubchik 2007
num_copies = 10             # number of mutated sequences

# Load original sequence
record = SeqIO.read(input_fasta, "fasta")
original_seq = record.seq
seq_len = len(original_seq)

print(f"Loaded sequence {record.id} with length {seq_len} aa")

# Create gapped sequences
def generate_deleted_sequences(del_size, pattern="A"):
    min_start = 40  #  as in Golubchik AAA35797 reference sequence
    sequences = []
    sequences.append(SeqRecord(original_seq, id="original", description=""))
    for i in range(num_copies):
        mut = MutableSeq(str(original_seq))

        # Deletion start position A (10) or B (30)
        if pattern == "A":
            start = min_start + i
        elif pattern == "B":
            start = min_start + i * del_size
        else:
            raise ValueError("Pattern must be 'A' or 'B'")

        # Stop if deletion would exceed sequence length
        if start + del_size > seq_len:
            break

        # Insert gaps
        mut[start:start+del_size] = "-" * del_size

        seq_id = f"copy_{i+1}_del{del_size}_{pattern}"
        sequences.append(SeqRecord(Seq(str(mut)), id=seq_id, description=""))

    return sequences

# Generate and save datsets
for del_size in deletion_sizes:
    for pattern in ["A", "B"]:
        seqs = generate_deleted_sequences(del_size, pattern)
        outfile = os.path.join(output_dir, f"refalign_{del_size}aa_pattern{pattern}.fasta")

        # Remove old file if it exists
        if os.path.exists(outfile):
            os.remove(outfile)
            print(f"Removed old file: {outfile}")

        # Write the new corrected file
        SeqIO.write(seqs, outfile, "fasta")
        print(f"Saved new file: {outfile}")