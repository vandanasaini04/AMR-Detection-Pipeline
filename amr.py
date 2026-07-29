from Bio import SeqIO

fasta_file = "GCF_000013465.1_ASM1346v1_protein.faa"

records = list(SeqIO.parse(fasta_file, "fasta"))

print(f"Total sequences: {len(records)}")

for record in records[:5]:
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Length: {len(record.seq)}")
    print("---")
    from Bio import SeqIO
    from Bio.Blast import NCBIWWW

    fasta_file = "GCF_000013465.1_ASM1346v1_protein.faa"
    records = list(SeqIO.parse(fasta_file, "fasta"))

    # Start small — just first 3 sequences, since online BLAST is slow
    test_records = records[:3]

    for record in test_records:
        print(f"Running BLAST for {record.id}...")
        result_handle = NCBIWWW.qblast("blastp", "nr", record.seq)

        output_filename = f"blast_result_{record.id}.xml"
        with open(output_filename, "w") as out_file:
            out_file.write(result_handle.read())

        print(f"Saved result for {record.id} -> {output_filename}")

    print("Done with BLAST for test subset.")
    from Bio import SeqIO
    from Bio.Blast import NCBIWWW

    fasta_file = "GCF_000013465.1_ASM1346v1_protein.faa"
    records = list(SeqIO.parse(fasta_file, "fasta"))

    test_records = records[:3]

    for record in test_records:
        print(f"Running BLAST for {record.id}...")
        result_handle = NCBIWWW.qblast("blastp", "swissprot", record.seq)

        output_filename = f"blast_result_{record.id}.xml"
        with open(output_filename, "w") as out_file:
            out_file.write(result_handle.read())

        print(f"Saved result for {record.id} -> {output_filename}")

    print("Done with BLAST for test subset.")