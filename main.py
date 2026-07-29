import pandas as pd


from Bio import SeqIO
count = 0
for record in SeqIO.parse("sequence.fasta", "fasta"):
  count += 1
print("Total records: ", count)
from Bio import SeqIO
shortest = min(SeqIO.parse("sequence.fasta", "fasta"), key=lambda record: len(record.seq))
print("ID:", shortest.id)
print("Length:", len(shortest.seq))


from Bio import SeqIO

stops = ["TAA", "TAG", "TGA"]

def longest_orf(seq, frame):
    max_len = 0
    start_pos = None

    i = frame
    while i <= len(seq) - 3:
        codon = seq[i:i+3]

        if codon == "ATG":
            j = i

            while j <= len(seq) - 3:
                stop = seq[j:j+3]

                if stop in stops:
                    length = j + 3 - i

                    if length > max_len:
                        max_len = length
                        start_pos = i + 1

                    break

                j += 3

        i += 3

    return max_len, start_pos


best = 0

for record in SeqIO.parse("sequence.fasta", "fasta"):
    seq = str(record.seq)

    length, pos = longest_orf(seq, 1)

    if length > best:
        best = length

print("Longest ORF in frame 2:", best)
best_len = 0
best_pos = 0

for record in SeqIO.parse("sequence.fasta", "fasta"):
    seq = str(record.seq)

    length, pos = longest_orf(seq, 2)   # Reading frame 3

    if length > best_len:
        best_len = length
        best_pos = pos

print("Starting position:", best_pos)
best = 0

for record in SeqIO.parse("sequence.fasta", "fasta"):
    seq = str(record.seq)

    for frame in [0, 1, 2]:
        length, pos = longest_orf(seq, frame)

        if length > best:
            best = length

print("Longest ORF:", best)
best = 0

for record in SeqIO.parse("sequence.fasta", "fasta"):

    if record.id == "gi|142022655|gb|EQ086233.1|16":

        seq = str(record.seq)

        for frame in [0, 1, 2]:
            length, pos = longest_orf(seq, frame)

            if length > best:
                best = length

print("Longest forward ORF:", best)

from Bio import SeqIO
from collections import Counter

counts = Counter()

for record in SeqIO.parse("sequence.fasta", "fasta"):
    seq = str(record.seq)

    for i in range(len(seq) - 5):
        repeat = seq[i:i+6]
        counts[repeat] += 1

repeat, frequency = counts.most_common(1)[0]

print("Most frequent repeat:", repeat)
print("Count:", frequency)

from Bio import SeqIO
from collections import Counter

counts = Counter()

for record in SeqIO.parse("sequence.fasta", "fasta"):
    seq = str(record.seq)

    for i in range(len(seq) - 11):
        repeat = seq[i:i+12]
        counts[repeat] += 1

max_count = max(counts.values())

num = 0

for value in counts.values():
    if value == max_count:
        num += 1

print("Maximum count:", max_count)
print("Number of 12-mers with maximum count:", num)

from Bio import SeqIO
from collections import Counter

counts = Counter()

for record in SeqIO.parse("sequence.fasta", "fasta"):
    seq = str(record.seq)

    for i in range(len(seq) - 6):
        repeat = seq[i:i+7]
        counts[repeat] += 1

repeat, frequency = counts.most_common(1)[0]

print("Most frequent 7-mer:", repeat)
print("Count:", frequency)
df = pd.read_csv('sequence.fasta')
df.to_csv("genes.csv", index=False)
print("CSV Created Succesfully")
print(df.head(3))
print(df.tail(3))
print(df.shape)
print(df.info())
import pandas as pd
data = { "Gene" : ["BRAC1", "TP53", "EGFR", "MYC"],
       "Expression": [120, 95, 210, 180]}
df = pd.DataFrame(data)
print(df.describe())
print(df.loc[2])
print(df.loc[2], "Expression")
print(df.iloc[2,1])
print(df.iloc[0])
print(df.iloc[3,1])
print(df.iloc[:,0])
print(df[df["Expression"] >= 180])
print(df[df["Gene"] == "EGFR"])
print(df.sort_values("Expression", ascending=False))
print(df.sort_values("Gene"))
print(df.groupby("Gene")["Expression"].mean())