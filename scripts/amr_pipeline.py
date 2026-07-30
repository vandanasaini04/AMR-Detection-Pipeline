from Bio.Blast import NCBIXML
import pandas as pd

results = []

with open("results/all_amr_results.xml") as handle:
    blast_records = NCBIXML.parse(handle)

    for record in blast_records:
        query_id = record.query.split()[0]
        query_length = record.query_length

        if record.alignments:
            alignment = record.alignments[0]
            hsp = alignment.hsps[0]

            identity = (hsp.identities / hsp.align_length) * 100
            coverage = (hsp.align_length / query_length) * 100

            if hsp.expect < 1e-5 and identity >= 40 and coverage >= 70:
                confidence = "Strong"
                amr_status = "Yes"

            elif hsp.expect < 1e-5:
                confidence = "Weak"
                amr_status = "Possible"

            else:
                confidence = "None"
                amr_status = "No"

            results.append({
                "Query_ID": query_id,
                "Hit_ID": alignment.hit_id,
                "Hit_Description": alignment.hit_def,
                "Identity_%": round(identity, 2),
                "Coverage_%": round(coverage, 2),
                "E_value": hsp.expect,
                "Confidence": confidence,
                "AMR_Status": amr_status
            })

        else:
            results.append({
                "Query_ID": query_id,
                "Hit_ID": "No Hit",
                "Hit_Description": "No AMR Match",
                "Identity_%": 0,
                "Coverage_%": 0,
                "E_value": "-",
                "Confidence": "None",
                "AMR_Status": "No"
            })

df = pd.DataFrame(results)

df.to_csv("results/amr_summary.csv", index=False)

print(df)

print("\nSummary")
print(f"Total proteins screened: {len(df)}")
print(f"AMR hits (Yes): {(df['AMR_Status'] == 'Yes').sum()}")
print(f"Possible AMR hits: {(df['AMR_Status'] == 'Possible').sum()}")
print(f"No AMR hits: {(df['AMR_Status'] == 'No').sum()}")
