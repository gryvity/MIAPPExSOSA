# MIAPPE

## References

https://doi.org/10.1038/s41597-023-02364-z

https://doi.org/10.1111/tpj.14179

https://doi.org/10.34133/2019/1671403


Promoting coherent minimum reporting
guidelines for biological and biomedical
investigations: the MIBBI project



https://www.berrybase.de/loadBasket/weyzuH1iSr4


# DataSet Search
[docs/material/datasearch_2019.pdf]

Chapman, A., Simperl, E., Koesten, L. et al. Dataset search: a survey. The VLDB Journal 29, 251–272 (2020). https://doi.org/10.1007/s00778-019-00564-x


-> Data Search or Data Retrieval as an emerging research field encompassing frameworks, methods or tools that allows user to identify relevant data against a collection of datasets. 
-> "Dataset Search is largely keyword-based over published metadata, whether it is performed oder web crawls [...] or within organizational holdings [...]. There are several problems with this approach. Available metadata may not encompass the actual information a user needs to assess whether the dataset is fit for a given task [https://doi.org/10.1145/3025453.3025838]. [...] in a dataset search context, approaches need to consider additional aspects such as data provenance, annotations, quaility, granularity of content, and schema to effectively evaluate a dataset's fitness for a particular use."
-> Definition of a dataset by SDMX: "A Collection of related observations, organized according to a predefined structure" 
-> In the paper two search approaches are illustrated: 1) Basic dataset search and 2) Constructive dataset search.
-> Basic Dataset Search: Datasets are organized and published for consumption and reuse. A user issues a query that returns a list of datasets, not tuples, documents or corpora. The user must then rank the datasets according to their fitness for the intended use.
-> Constructive Dataeset Search: The user organizes and integrates data from multiple datasets to create a new dataset that is fit for a particular purpose. 
-> Main differences: Basic Dataset Search involves a dataset to be of data from related observation, organized acccording a structure defined by the publisher. In Constructive Dataset Search, the user defines the structure of the dataset to be created.
-> Overview of Dataset Search: Here the process is illustrated into 4 main steps: 1) Query Language, 2) Query Handling, 3) Data Handling, 4) Results Presentation. The process can be followed using different approaches: database oriented, keyword-based, entity search or web tables.
    [SITE NOTE:] Z39.50 is an international standard client–server, application layer communications protocol for searching and retrieving information from a database over a TCP/IP computer network, developed and maintained by the Library of Congress. It is covered by ANSI/NISO standard Z39.50, and ISO standard 23950. 
-> A Query (in what shape so ever whether expressed in SQL or CQL, etc.) is used to search over metadata producing results on how similar the metadata is to the search terms. Metadata can be expressed in vocabularies to provide a uniform way of eensuring consistency. But providing the metadata is mostly a manual and hence resource-intense task, resulting in incomplete or inaccurate metadata.
-> [I WANT TO HIGHLIGHT THIS PARAGRAPH]: "In entity-centric search information is organized and accessed via entities of interest, and their attributes and relationships. [...] The problem has been tackled mostly by the semanticweb and knowledge discovery communities. From a semantic web perspective, efforts have beendirected toward creating machine-understandable graph-directed toward creating machine-understandable graph-based representations of data [79]. 
    [79] Heath, Tom, and Christian Bizer. Linked Data: Evolving the Web into a Global Data Space. 1st ed. Cham: Springer, 2011. Web.
-> Two related concerns with interlinking: 1) Entity resolution and 2) link discovery.
-> [ALSO AN INTERESTING PARAGRAPH]: "Table completion. This task also relies heavily on table similarity as the mechanism for finding potential values that can be added to a table. [...] defines the notion of row population, which adds new rows to a table. For simplicity, we view this as a type of table completion in which the values to be completed form an additional row. Even more broadly, one could provide a set of columns as a query and have the system fill in the remaining rows [...]. The task of table completion can be seen as entity-set completion, where the goal is to complete a list given a set of seed entities [...]. This task is relevant for a number of other scenarios, including entity- centric search [...] and knowledge-base completion [...]. The completion of rows is similar to the broad problem of impu- tation and dealing with incomplete data [...]. Specific work in the context of the web has looked at performing impu- tation through the use of external data [...]. Much of that work has used web tables as the data source, and hidden/deep web techniques as discussed above could be applied."
-> A common theme of current dataset search strategies rely on datasets being tagged with appropriate information in the correct format.
-> Section 3.2.1 (Basic, Centralized Search - Search over linked data) provides a list of literature addressing the implementation for searching linked data in in a native semantically heterogeneous and distributed environment
-> [CrossRef arxiv:1810.12423] Claims that standard metadata does not provide enogh information for data reuse.
-> "Currently dataset search is mainly performed over metadata, so the users understanding of what the dataset contains before download is limited by the quality, comprehensiveness and nature of metadata.
-> [https://doi.org/10.1145/3025453.3025838]: Three major factors that matter to data practitionerswhen selecting datasets: relevance, usability and quality.
|- OPEN PROBLEMS -|
-> in 2011 the European Commission identified 6 barriers for open data which also apply to dataset search:
    - lack of information that ccertain data exists and is available.
    - a lack of clarity of which public authority holds the data 
    - a lack of clarity of the terms of reuse
    - data in formats which is difficult or expensive to use
    - complicated licensing procedure or fees
    - exclusive reuse agreements or reuse restrictions