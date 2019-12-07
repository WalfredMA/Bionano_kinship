# Bionano_kinship

Test kinship of bionano samples based on common structural variations.

    1. selected only deletions from each assembly with a high confidence value and size>1k.

    2. Based on their coordinates on the reference, find SVs within 500bps distance.

    3. choose one sample with no known kinship between either sample as the control and filtered all SVs overlapped with it. (This meant to filter out minor alleles of the reference)

    4. determined the percentage of overlapped SVs in each assembly, and pick the higher percentage to adjust the coverage discrepancy.


Input:

    -q: the query sample 

    -r: the output sample

output:

