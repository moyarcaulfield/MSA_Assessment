from Bio import SeqIO
from Bio.Seq import Seq, MutableSeq
from Bio.SeqRecord import SeqRecord
import os

input_fasta = "AAA35797.fasta" 
output_dir = "output"
deletion_sizes = [10, 30]   
num_copies = 10             

record = SeqIO.read(input_fasta, "fasta")
original_seq = record.seq
seq_len = len(original_seq)

print(f"Loaded sequence {record.id} with length {seq_len} aa")

def generate_deleted_sequences(del_size, pattern="A"):
    min_start = 40  
    sequences = []
    sequences.append(SeqRecord(original_seq, id="original", description=""))
    for i in range(num_copies):
        mut = MutableSeq(str(original_seq))

        if pattern == "A":
            start = min_start + i
        elif pattern == "B":
            start = min_start + i * del_size
        else:
            raise ValueError("Pattern must be 'A' or 'B'")

        if start + del_size > seq_len:
            break
            
        mut[start:start+del_size] = "-" * del_size

        seq_id = f"copy_{i+1}_del{del_size}_{pattern}"
        sequences.append(SeqRecord(Seq(str(mut)), id=seq_id, description=""))

    return sequences

for del_size in deletion_sizes:
    for pattern in ["A", "B"]:
        seqs = generate_deleted_sequences(del_size, pattern)
        outfile = os.path.join(output_dir, f"refalign_{del_size}aa_pattern{pattern}.fasta")

        if os.path.exists(outfile):
            os.remove(outfile)
            print(f"Removed old file: {outfile}")

        SeqIO.write(seqs, outfile, "fasta")
        print(f"Saved new file: {outfile}")
