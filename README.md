# MSA_Assessment - ***Project title: Assessing the accuracy of multiple sequence alignments, when analysing proteins***

> **Is it possible to rank accuracy of multiple sequence alignments?**


Python code was written and executed in Spyder (version 6.1.3 | Python 3.12.11 64-bit | Qt 5.15.15 | PyQt5 5.15.11 Windows 11 (AMD64) )

Alignments were generated and visualised using Jalview (version 2.11.5.1)

Accuracy of MSA methods is calculated by Total Column Score by AliDist software by Lars Jermiin

Graphs and figures made

## Guide to understanding file names: 

**Deletion Size**

10aa - 10 amino acids removed from a sequence to introduce a gap

30aa - 30 amino acids removed freom a sequence to introduce a gap

**Gap Pattern** 

A - pattern A: gaps are overlapping

- Each deletion window shifts by one residue along the sequence.
- Example: variant n deletes residues i–i+9; variant n+1 deletes i+1–i+10.

B - pattern B: gaps are not overlapping 

- Each deletion window starts immediately after the previous one ends.
- Example: variant n deletes i–i+9; variant n+1 deletes i+10–i+19.

## ***MSA References (from Jalview)*** 

### **ClustalW** 

Alignment with ClustalWS using service hosted at http://www.compbio.dundee.ac.uk/jabaws
SERVICE: ClustalWS version 2.1

JABAWS v. 2.2
REFERENCE: Larkin MA, Blackshields G, Brown NP, Chenna R, McGettigan PA, McWilliam H, Valentin F, Wallace IM, Wilm A, Lopez R, Thompson JD, Gibson TJ, Higgins DG,
"Clustal W and Clustal X version 2.0"
Bioinformatics, 23: 2947 (2007)

MORE INFORMATION: http://www.clustal.org/clustal2/

### **Clustal Omega** 

Alignment with ClustalOWS using service hosted at http://www.compbio.dundee.ac.uk/jabaws
SERVICE: ClustalOWS version 1.2.4

JABAWS v. 2.2
REFERENCE: Sievers F, Wilm A, Dineen D, Gibson TJ, Karplus K, Li W, Lopez R, McWilliam H, Remmert M, Söding J, Thompson JD, Higgins DG,
"Fast, scalable generation of high quality protein multiple sequence alignments using Clustal Omega"
Mol Syst Biol. 7:539 (2011)

MORE INFORMATION: http://www.clustal.org/omega/

### **MAFFT (G-INS-i)**

Alignment with MafftWS using service hosted at http://www.compbio.dundee.ac.uk/jabaws
SERVICE: MafftWS version 7.310

JABAWS v. 2.2
REFERENCE: Katoh K, Toh H,
"Parallelization of the MAFFT multiple sequence alignment program"
Bioinformatics 26:1899 (2010)

MORE INFORMATION: http://mafft.cbrc.jp/alignment/software/

Using Server preset: G-INS-i (Accuracy-oriented)

### **MUSCLE**

Alignment with MuscleWS using service hosted at http://www.compbio.dundee.ac.uk/jabaws
SERVICE: MuscleWS version 3.8.31

JABAWS v. 2.2
REFERENCE: Edgar RC,
"MUSCLE: multiple sequence alignment with high accuracy and high throughput"
Nucleic Acids Res. 32(5):1792 (2004)

MORE INFORMATION: http://www.drive5.com/muscle/

### **ProbCons**

Alignment with ProbconsWS using service hosted at http://www.compbio.dundee.ac.uk/jabaws
SERVICE: ProbconsWS version 1.12

JABAWS v. 2.2
REFERENCE: Do CB, Mahabhashyam MSP, Brudno M, and Batzoglou S,
"PROBCONS: Probabilistic Consistency-based Multiple Sequence Alignment"
Genome Research 15:330 (2005)

MORE INFORMATION: http://probcons.stanford.edu/

### **T-Coffee**

Alignment with TcoffeeWS using service hosted at http://www.compbio.dundee.ac.uk/jabaws
SERVICE: TcoffeeWS version 11.00.8cbe486

JABAWS v. 2.2
REFERENCE: Notredame C, Higgins DG, Heringa L,
"T-Coffee: A novel method for multiple sequence alignments"
JMB, 302(1):205 (2000)

MORE INFORMATION: http://tcoffee.crg.cat/apps/tcoffee/index.html
