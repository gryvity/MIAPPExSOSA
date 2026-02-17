

'''
# OntComp 
 
OntComp [Ontology Composer] is a tool to dynamically merge Data Models. 
You can load classes, properties and Individuals from existing Ontologies, and add new classes and properties.
Relations and Objects can be added via the (s,p,o,(t)) format.

## Usage



'''

from owlready2 import get_ontology
import rdflib
# import types 


class OntComp(object):
    def __init__(self, config, local : list | None = None):
        """
        Ontology Composer
        
        :param config: YAML File containing all Onotology Params
        :param local: List of local Ontology Files (currently owl and ttl supported)

        """
        self.source_ontologies = self._configurations(config)

        


    def _configurations(self, fpath : str) -> dict:
        with open(fpath, "rb") as file:
            content = file.read()
        return content
    
    def load_source_ontology(self, opath):
        pass

    def unify_name(self, name : str, ntype : str) -> str:
        """
        :param name: Name of a Class or a Porperty
        :type name: str
        :param ntype: Type "class" or "prop"
        :type ntype: str
        :return: Returns name in camelCase
        :rtype: str
        """
        if ntype ==  "class":
            name = name[0].upper() + name[1:]
        if "_" in name:
            name = "".join([np.capitalize() for np in name.split("_")])
        if ntype == "prop":
            name = name[0].lower() + name[1:]
        return name
        



if __name__ == "__main__":

    # LOCAL
    local = True
    if local:
        import os   
    
        onto_dir= 'data/ontologies'
        onto_imports_files = [
            'ppeo.owl',
            'sosa.owl',
            'ssn.ttl'
        ]   
        onto_paths = [os.path.join(onto_dir, "local_import", x) for x in onto_imports_files]
        
    else:
        pass

    local_iri = os.path.join(onto_dir, "miappexsosa.owl")
    
    config_fpath = "ontologycomposer/config/miappexsosa_config.yaml"



    onto = OntComp(config_fpath, local = onto_paths)
    print(onto.source_ontologies)
