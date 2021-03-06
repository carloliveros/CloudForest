FAQ:
====

Why should you use CloudForest to infer a Species-Tree?

	`Incomplete Lineage Sorting`_ (ILS) is becoming increasing recognized as influential process in genomic evolution. ILS describes what happens when by random chance different versions of the same allele end up in the 'wrong' species during speciation and thus produce conflicting phylogenies along the genome. If you are interested in inferring the phylogenetic relationships between species from genome sized data (= hundreds of loci) it's important to account for ILS. Unfortuantely traditional 'concatenation style analyses' do not account for ILS. Cloudforest provides a pipeline that incorporates ILS into phylogenetic inference from thousands of independant loci. For inferring many thousands of trees, you'll need to do this if you want to bootstrap your dataset, as well as a wrapper for the R package `Phybase`_ which provides a number of methods for generating species-trees from gene-trees.

Why should you use CloudForest



.. _Incomplete Lineage Sorting: http://en.wikipedia.org/wiki/Incomplete_lineage_sorting
.. _Phybase: http://code.google.com/p/phybase/