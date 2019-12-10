# Bionano_kinship

//  Created by Walfred MA in 2019, wangfei.ma@ucsf.edu.
//  Copyright © 2019 UCSF-Kwoklab. All rights reserved.

Test kinship of bionano samples based on common structural variations.

    1. selected only deletions from each assembly with a high confidence value and size>1k.

    2. Based on their coordinates on the reference, find SVs within 500bps distance.

    3. choose one sample with no known kinship as the control and filtered all common SVs. (This meant to filter out minor alleles of the reference)

    4. determined the percentages of overlapped SVs in tested assemblies, and output the lower one.


Input:

    -c: the control sample 

    -f: the test samples

it outputs the common sv ratio. 

eg: Python2.7 

Here are general results:

    Same assembly	                                               100%
    Same sample, different assembly                             	48%
    Mother vs kid	                                              34-36%
    No relationship	                                              22-26%
