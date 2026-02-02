# Project Plan

1) Create a Data Model combining MIAPPE and SOSA
MIAPPE Model https://github.com/MIAPPE/MIAPPE/blob/master/MIAPPE_diagram.svg
SSN/SOSA Model https://www.w3.org/TR/vocab-ssn/

2) From the Data Model, write a program which can convert actual data and generate a graph structure according to the data model.

3) Apply the porgramm to example data and generate a graph structure.



## Minimal Information about Field Phenotyping Experiments Overview

Here, the central planning stages are documented for the project. This will guide me through the project step-by-step. These steps include a schedule for:
- Literature Review
- Protoyping
- Paper Structure and Writing

This document will track the progress of the project. Furthermore here I will provide some space for loose notes and ideas that might be useful for the project.

The goal of this particular project is to create a standardized template for documenting field phenotyping experiements, building upon the existing MIAPPE standard, and adopting further metadata standards to cover terminologies and concepts from the domain of remote sensing and computer vision and robotics. The final template should be simple and userfriendly without sacrificing semantic expressivity and FAIR compliance. To do so, I will merge relevant ontologies and vocabularies into onde MIAFPE ontology, generate a data model and finally implement the template in a user-friendly format, e.g. as a web application or a fillable PDF form.

Furthermore, this project aims on tranforming the documentation into a machine-readable format, e.g. JSON-LD or RDF. These machine-readable formats will be designed to be in an appropriate shape in order to allow the development of embeddings for machine learning applications in the future. Since the datamodel resemble a graphlike structure, it is likely that graph neural networks (GNNs) will be a suitable choice for such applications.

For March 2026, I need to have a working protoype as well as a knowledge base.


## Schedule 
| Task                          | Start Date | End Date   | Status       |
|-------------------------------|------------|------------|--------------|
| Prototype Planning | 2026-01-05 | 2026-01-07 | Started     |
| Prototyping                   | 2026-01-07 | 2026-01-09 | Not Started  |
| Literature Review             | 2026-01-12 | 2026-01-16 | Not Started  |
| Paper Structure Planning      | 2026-01-16 | 2026-01-18 | Not Started  |
| Writing First Draft          | 2026-01-18 | 2026-01-30 | Not Started  |


## Paper Structure

Prelimary structure of the paper (2026-01-05):

- Introduction
    - Background emergence of interdisciplinary research in plant phenotyping adapting new technologies from computer vision, robotics and remote sensing
    - Motivation of standardized documentation of experiemental data
    - Minimum Information standards in life sciences.
    - Ontologies and Vocabularies for metadata standardization
    - FAIR principles and the advent of machine-readable metadata
    - Aim of this work: 
        - Create a standardized template for documenting field phenotyping experiements, building upon the existing MIAPPE standard, and adopting further metadata standards to cover terminologies and concepts from the domain of remote sensing and computer vision and robotics.
        - Implement the template in a user-friendly format, e.g. as a web application or a fillable PDF form.
        - Transforming the documentation into a machine-readable format, e.g. JSON-LD or RDF.
- Related Work
    - Overview of existing MI standards in life sciences
    - Overview of existing ontologies and vocabularies relevant for plant phenotyping, remote sensing, computer vision and robotics
    - Overview of existing tools and templates for documenting field phenotyping experiments
    - Linked Data
- Methods
    - Ontology and Vocabulary Selection and Merging
    - Data Model Design
    - Template Implementation
    - Machine-Readable Format Design
- Results
    - Finalized Template
    - Machine-Readable Format
- Discussion
    - Evaluation of the Template
    - Comparison with Existing Standards
    - Limitations and Future Work -> here I would love to discuss the potential of having machine-readable metadata for training machine learning models, e.g. GNNs in order to find patterns in phenotyping experiements, that could help identify 'contextual' similarities between experiements, which could be potentially useful for machine learning tasks, meta analyses or even experimental design.


## Prototyping Steps

GOALS:
Create an "ontology-based" template for documenting field phenotyping experiements and data derived thereof, that is build upon MIAPPE as an already existing standard, which is further modified (and made modifiable) to include external ontologies and link concepts within these ontologies. This means we include an abstract concept ontology to the MIAPPE ontology, which can be used as a template to fill in this conceptual ontology with an explicit ontology when relevant to a certain experiment.

In other words, the idea is to create a concept ontology which is embedded into an existing ontology, such as the MIAPPE ontology. If applicable, the ontology concept can be filled with existing concepts from an external ontology, e.g. SOSA/SSN for Sensors, or OBOE for observations, etc.

- Step 1: Gather existing Ontologies and Vocabularies relevant for the project



## Literature Selection

Within this section I will collect relevant literature for the project and give a short summary which mainly focusses on the reasoning why this paper is relevant for the project.





## Notes and Ideas

- Potential Project Partners: WUR, APPN, Fraunhofer, Roland, Pommiers, Björn
- Try to emphasize a focus on data file contents and relationship between data files within an experiment
- Try to find a significant list of usecases that are already implementing MIAPPE or similar standards and identify interdisciplinary components within these uescases and their documentation needs
- Graph embedding: https://towardsdatascience.com/graph-embeddings-explained-f0d8d1c49ec/


We start with collecting relevant terms and properties from existting ontologies in order to transform actual data from the benchmark data set into a graph-like data model. For the prototype we concentrate on building a data model on base of the following ontologies:

- Prov-O: https://www.w3.org/TR/prov-o/
- MIAPPE Ontology: https://github.com/MIAPPE/MIAPPE-ontology
- Semantic Sensor Network Ontology: https://www.w3.org/TR/vocab-ssn/
- OBOE: https://github.com/NCEAS/oboe
- DataSet-Variable Ontology: https://ritamargherita.github.io/DataSet-Variable-Ontology/


# Systematic Literature Review

# Selection of relevant Ontologies

## General Ontologies
- Dublin Core: https://www.dublincore.org/specifications/dublin-core/dc
- PROV Ontology: https://www.w3.org/TR/prov-o/
- rdf	http://www.w3.org/1999/02/22-rdf-syntax-ns#	The RDF namespace [RDF-CONCEPTS]
- xsd	http://www.w3.org/2000/10/XMLSchema#	XML Schema Namespace [XMLSCHEMA11-2]
- owl	http://www.w3.org/2002/07/owl#	The OWL namespace [OWL2-OVERVIEW]

- AGROVOC: https://www.fao.org/agrovoc/linked-data

THSI COULD BE ALSO BE USEFUL:
https://vocabularyserver.com/cnr/ml/earth/en/index.php?tema=1240&/equipment-and-technological-systems

## MIAPPE Ontology
- MIAPPE Ontology GitHub: https://github.com/MIAPPE/MIAPPE-ontology
- AgroPortal: https://agroportal.lirmm.fr/ontologies/PPEO



## Semantic Sensor Network Ontology
https://github.com/w3c/sdw-sosa-ssn

https://www.w3.org/TR/vocab-ssn/

https://github.com/w3c/sdw/tree/gh-pages

## GEOBIA

https://www.geobia.com/#how-it-works

## OBOE

https://github.com/NCEAS/oboe


# Further Reads
https://stackoverflow.com/questions/8373425/populate-an-existing-ontology-from-a-csv-file-using-jena
https://stackoverflow.com/questions/13147864/how-to-create-an-ontology-from-raw-data-csv
https://nbisweden.github.io/module-metadata-dm-practices/05-finding-ontologies/index.html
https://jena.apache.org/documentation/ontology/
https://scs-ontouml.eemcs.utwente.nl/catalog/b663ca18-8085-44a7-bcfe-2c2b5ba1faa8
https://github.com/w3c/sdw-sosa-ssn

ML : https://mlcommons.org/working-groups/data/croissant/


# Ontologies for Further descibing Experiments and Data

experimental factor ontology:
https://www.ebi.ac.uk/ols4/ontologies/efo?tab=classes

environment ontology:
https://www.ebi.ac.uk/ols4/ontologies/envo?tab=classes&viewMode=list


protein ontology:
https://www.ebi.ac.uk/ols4/ontologies/pr

gen ontology:
https://www.ebi.ac.uk/ols4/ontologies/go

agronomy ontology:
https://www.ebi.ac.uk/ols4/ontologies/agro?tab=classes

Biological Spatial Ontology:
https://www.ebi.ac.uk/ols4/ontologies/bspo?tab=classes

chemical entities of biological interest:
https://www.ebi.ac.uk/ols4/ontologies/chebi?tab=classes

plant anatomical entity Plant Ontology:
http://purl.obolibrary.org/obo/PO_0025131

data catalog vocabulary:
http://www.w3.org/ns/dcat

provenance ontology:
https://www.ebi.ac.uk/ols4/ontologies/prov

dcterms:
http://purl.org/dc/terms/

data use ontology:
http://purl.obolibrary.org/obo/duo.owl

Information artifact ontology:
http://purl.obolibrary.org/obo/iao.owl

INRAE thesaurus:
http://opendata.inrae.fr/thesaurusINRAE/thesaurusINRAE
