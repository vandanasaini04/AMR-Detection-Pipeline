# AMR Gene Detection Pipeline using BLAST+ and CARD

## Project Overview

This project identifies potential antimicrobial resistance (AMR) genes in the *Staphylococcus aureus* proteome by performing a local BLASTP search against the Comprehensive Antibiotic Resistance Database (CARD).

The workflow was developed using Python, Biopython, BLAST+, and the CARD protein database to identify proteins associated with antimicrobial resistance based on sequence similarity.

---

## Objectives

- Screen all *Staphylococcus aureus* proteins against the CARD database.
- Identify proteins associated with antimicrobial resistance.
- Filter BLAST results using sequence identity, query coverage, and E-value.
- Generate a final CSV report of predicted AMR genes.

---

## Tools Used

- Python 3
- Biopython
- Pandas
- BLAST+
- CARD (Comprehensive Antibiotic Resistance Database)

---

## Workflow

1. Download the *Staphylococcus aureus* protein FASTA file.
2. Download the CARD protein database.
3. Create a local BLAST protein database using `makeblastdb`.
4. Perform a BLASTP search against the CARD database.
5. Parse the BLAST XML output using Biopython.
6. Calculate:
   - Percentage Identity
   - Query Coverage
   - E-value
7. Classify each protein as:
   - **Yes** (High-confidence AMR)
   - **Possible** (Potential AMR)
   - **No** (No significant AMR evidence)
8. Export the final results to a CSV file.

---

## Classification Thresholds

### Yes (High-confidence)

- E-value < 1e-5
- Identity ≥ 40%
- Query Coverage ≥ 70%

### Possible

- E-value < 1e-5 but below the identity and/or coverage thresholds.

### No

- E-value ≥ 1e-5 or no significant alignment.

**Note:** These thresholds were selected to reduce false positives while retaining biologically meaningful sequence matches.

---

## Results

| Metric | Count |
|--------|------:|
| Total proteins screened | 2772 |
| High-confidence AMR hits | 31 |
| Possible AMR hits | 191 |
| No significant AMR match | 2550 |

---

## Output Files

The pipeline generates:

- `results/all_amr_results.xml`
- `results/amr_summary.csv`

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```