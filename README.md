# mutation
Small Python program to induce mutations in a protein sequence

For inducing mutations in which the user knows the amino acid to be affected and its position, the user can enter both pieces of information to delete or change that amino acid. 

Reads input file containing protein sequence as a text file in FASTA format. Optimized for FASTA files obtained from BLAST with complete sequences. Outputs the same information with minor changes in the sequence depending on the mutation.

delete.py allows you to delete an amino acid given its position

substitute.py allows you to swap one amino acid with another given the original amino acid's position
