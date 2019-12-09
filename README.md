# Bionano_kinship

//  Created by Walfred MA in 2019, wangfei.ma@ucsf.edu.
//  Copyright © 2019 UCSF-Kwoklab. All rights reserved.

Test kinship of bionano samples based on common structural variations.

    1. selected only deletions from each assembly with a high confidence value and size>1k.

    2. Based on their coordinates on the reference, find SVs within 500bps distance.

    3. choose one sample with no known kinship between either sample as the control and filtered all SVs overlapped with it. (This meant to filter out minor alleles of the reference)

    4. determined the percentage of overlapped SVs in each assembly, and pick the higher percentage to adjust the coverage discrepancy.


Input:

    -c: the control sample 

    -f: the test samples

it outputs the common sv ratio. 


Here are general results:

    Same assembly	                                               100%
    Same sample, different assembly                             	48%
    Mother vs kid	                                              34-36%
    No relationship	                                              22-26%
