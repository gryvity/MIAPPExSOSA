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


## Temporary

Hello I need your assistance in bringing some structure into a complex task. I will outline the project`s intent and the plan of achieving it, as well as provide you with some data which is necessary for building a protoype. I would like you to help me in the task of planning the prototyping steps with me.

I am currently working as a data scientist in plant science and have the task to make phenotyping data FAIR (according the FAIR principles by Wilkinson et al.). To do so, I am focussing on helping the researchers in documenting their experiments, mostly in form of tables (e.g. Excel sheets). Mostly I recomment MIAPPE, since this is a community standard designed for plant phenotyping experiments. MIAPPE is basically a checklist, which helps researchers to give metadata about their experiements, which is helpful for potential resuse of the data in the future, e.g. for machine learning applications or meta alayses, or to prevent redundancy. But MIAPPE as a table does have some limitations: Althoug MIAPPE has been transformed into an ontology (https://github.com/MIAPPE/MIAPPE-ontology) (see also attached file: PPEO.owl), it misses a user-friendly way to fill further metadata in a standardized way, for example for sensors, procedures, remote sensing techniques, computer vision methods, robotics platforms etc. These domains are becoming more and more relevant for plant phenotying, since more and more data is being collected with these technologies. The formalisation of MIAPPE as an ontology provides data modeling capabilities, which could be used in knowledge discovery utilizing the potential of the complex graphlike structure of ontologies, however, metadata provided in the miappe format is mostly 'just an excel table'. I woul like to design a versatil adaptation of MIAPPE as a ontology-based data model, which provides the possibility to easily extend it with further ontologies, meaning easily integrating data model into MIAPPE data models, which allows reseaerchers to provide more detailed metadata, without sacrifizing user-friendliness and the 'minimum information approach'.

To be more concrete I am planning to realize the following features in a prototype:
- from the MIAPPE Ontology construct a graph data model (design the classes, properties and relationships).
- provide access points into the data model for ontology extensions, for (1) selected ontologies relevant for field phenotyping experiemnts such as SOSA/SSN (for sensors and observations), OBOE (for observations and measurements), and (2) a general concept ontology, which can be used to fill in arbitrary ontologies into the data model.
- as a software implementation, I am thinking it starts from the data model site, using MIAPPE as it's core, and from that data model checklist tables can be generated, e.g. when genrating an excel just from the miappe core we have an excel file which resembles the current miappe standard. While adding more ontologies to the data model, we simply extend the excel file with more data sheets.
- when a researcher fills in the excel file, we can easily transform the table into a machine-readable graph format.

One aspect which is important to keep in mind, that each entry in the table needs to be linked to a concept in the ontology, therefor we need to include property information in the table as well and provide identifiers for each entry. As a quality of life way to do so it would be nice if IDs are automatically generated when filling in the tables (but leave the possibility to manually set them as well).

As you can see I am trying to think this problem from the data model as center peace. For now it would be helpful to have a prototype which allows select a set of ontologies (for somplicity just SOSA/SSN (https://www.w3.org/TR/vocab-ssn/)) and generate a table which resembles the MIAPPE standard, with extra fields for the selected ontologies. For now I will not implement something that generates IDs but instead leave it for the researcher to do it manually. I also want to add columns which provide class/data properties, where the researcher can provide the links to the ontology concepts. After finalizing the excel table, the researcher should be able to transform the table into a machine-readable JSON-LD or RDF format.

For realizing the project, I am thinking of implementing the prototype in python. That means I need a program, which can read an OWL file, and converts it into a table format. For the data model design it is probably helpful to have a visual presentation of the data model and to have a master owl file, where we can control the linkages by defining object properties' domains and ranges and also by defining synonyms for classes and properties. For the prototype it would be sufficient to have the MIAPPE ontology as well as the SSN/SOSA ontology as files as well as the master owl file, which links the two ontologies together. From this master file we can generate a table format. 

I am on a tight schedule, since I need to present the protoype as quickly as possible in a scientific paper. Therefore I would love to here your thoughts on the project, suggestions of the prototyping steps and any ideas you might have to make this project successful. 

< SEP >

I am reconsidering a few aspects and try to bring a new thought to it. The goal stays the same: compile a metadata format based on MIAPPE and SSN/SOSA with the idea of perfectly alligning these two ontologies with the prospect of eventually add other ontologies and terms from controlled vocabularies in the future. For now I am concerned with two tasks:
1) Create a Data Model which perfectly alligns MIAPPE and SSN/SOSA
2) Designing an Converter, which takes metadata from an excel file, and compiles a graph-like structure (the graph-structure given rules are defined by the data model).

For that reason I have a few examples of metadata entries, which I would like to use. For this project I need these parts:
- Ontology Files:
    - MIAPPE Ontology (PPEO.owl)
    - SSN/SOSA Ontology (https://www.w3.org/TR/vocab-ssn/)
- Master Ontology File, where I can edit the data model by defining classes, properties, relations and restrictions (domains and ranges)
- Edge and Node Prototypes for the graph structure.
- Conversion Script from Excel to Graph Structure

Can you please think of the following Scenario. Consider you have two very small ontologies, lets say People Ontology and Car Ontology. Consider yourself as an expert in modeling data for an insurance company who wants a clear picture of the situation oin case someone of your clients is reporting an accident. There exists an ontologies for People and an Ontology for cars, but you need a combination, that means you need to take classes and properties from these original ontologies and create new connections with new restrictions two it (e.g. a Person owns a Car (where the restriction is that only one Person can be owner of a car), or a Person is registered as Driver of a Car (where multiple Persons can be registered as Drivers of a Car)). It would be helpful if you create a Master Ontology File, which you can edit yourself without the need of designing a whole ontology for your case from scratch. With that you are now able to create a data model, which is an abstract model for your case, which can be applied once you receive a accident report. Lets say you want to investigate a case of an accident, where a A bunch of People are registered to a certain car. These people a related to each other in a certain way (e.g. family members, friends, colleagues etc.). All are registered as drivers to the car but only one is the owner. So in order to model this situation you need a script, which takes the data model, and a certain dataset (the case of that specific accident) and compiles a graph structure, which represents the situation. Can you imagine to realize this simple scenario?