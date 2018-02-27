BreseqFindCoverage is a small program for finding coverage and depth of SNVs after analysis of Breseq in its single colony mode.

Breseq is a very useful tool in SNV analysis. It works fast, and tiring entering pipelines with Bowtie and SAMTools is no longer needed.
However, Breseq had still some mimor problems, and one of them is lacking of coverage and depth output in single conlony mode 
(though was given in population mode). Actually, the information of coverage and depth was stored in a file call evidence.gd in evidence file.
Thus a small program is enough to solve the problem.

This small program only require enter of your Breseq output file (e.g. /file) and the program would find the evidence.gd 
(e.g. /file/output/evidence/evidence.gd) and output predicted mutations with their coverage and depth to output file (/file/index.csv)
