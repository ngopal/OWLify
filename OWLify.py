##############################################################################
#
# Written by Nikhil Gopal. Dec 1, 2012
#
# OWLify - A set of functions which allows programmers to generate OWL
# code from Python.
#
##############################################################################

class OWL:

    def __init__(self, namespace, outfile, propurl):
        self.namespace = str(namespace)
	self.outfile = outfile
        #self.outfile = 'output.owl'
        #self.propurl = 'http://staff.washington.edu/ngopal/prenatal.owl'
	self.propurl = propurl
        self.doc = ''
        self.start()

    def start(self):
        stub = ''
        stub += '<?xml version=' + '\"' + str(1.0) + '\"?>\n\n'
        stub += '<!DOCTYPE Ontology [\n'
        stub += '<!ENTITY xsd ' + '\"http://www.w3.org/2001/XMLSchema#\" >\n'
        stub += '<!ENTITY xml ' + '\"http://www.w3.org/XML/1998/namespace\" >\n'
        stub += '<!ENTITY rdfs ' + '\"http://www.w3.org/2000/01/rdf-schema#\" >\n'
        stub += '<!ENTITY rdf ' + '\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" >\n'
        stub += ']>\n\n'
        stub += '<Ontology xmlns=' + '\"http://www.w3.org/2002/07/owl#\"\n'
        stub += 'xml:base=\"http://www.w3.org/2002/07/owl#\"\n'
        stub += 'xmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n'
        stub += 'xmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n'
        stub += 'xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n'
        stub += 'xmlns:xml=\"http://www.w3.org/XML/1998/namespace\">\n'
        stub += '<Prefix name=\"rdf\" IRI=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"/>\n'
        stub += '<Prefix name=\"rdfs\" IRI=\"http://www.w3.org/2000/01/rdf-schema#\"/>\n'
        stub += '<Prefix name=\"xsd\" IRI=\"http://www.w3.org/2001/XMLSchema#\"/>\n'
        stub += '<Prefix name=\"owl\" IRI=\"http://www.w3.org/2002/07/owl#\"/>\n\n'
        stub += '<Declaration>\n'
        stub += '\t<Class IRI=\"'+self.namespace+'#\"/>\n'
        stub += '</Declaration>\n'
        print stub
        self.doc += stub
        return 0

    def addClass(self, classname):
        stub = '<Declaration>\n'
        stub += '\t<Class IRI=\"' + self.namespace + '#' + classname + '\"/>\n'
        stub += '</Declaration>'
        print stub
        self.doc += stub
        return 0

    def addSubClass(self, classname, superclassname):
        stub = '<SubClassOf>\n'
        stub += '\t<Class IRI=\"' + self.namespace + '#' + classname + '\"/>\n'
        stub += '<Class IRI=\"' + self.namespace + '#' + superclassname + '\"/>\n'
        stub += '</SubClassOf>\n'
        print stub
        self.doc += stub
        return 0

    def addProperty(self, prop):
        stub = '<Declaration>\n'
        stub += '\t<ObjectProperty IRI=\"' + self.propurl + '#' + prop + '\"/>\n'
        stub += '</Declaration>\n'
        print stub
        self.doc += stub
        return 0

    def assertSubClassTriple(self, classname, propertyname, propertyvalue, relation):
        if relation == 'some':
            relstart = '\t<ObjectSomeValuesFrom>\n'
            relend = '\t</ObjectSomeValuesFrom>\n'
        else:
            relstart = '\t<ObjectAllValuesFrom>\n'
            relend = '\t</ObjectAllValuesFrom>\n'
        stub = '<SubClassOf>\n'
        stub += '\t<Class IRI=\"' + self.namespace + '#' + classname + '\"/>\n'
        stub += relstart
        stub += '\t\t<ObjectProperty IRI=\"' + self.propurl + '#' + propertyname + '\"/>\n'
        stub += '\t\t<Class IRI=\"' + self.namespace + '#' + propertyvalue + '\"/>\n'
        stub += relend
        stub += '</SubClassOf>\n'
        print stub
        self.doc += stub
        return 0

    def addAnnotation(self, classname, message):
        stub = '<AnnotationAssertion>\n'
        stub += '\t<AnnotationProperty abbreviatedIRI=\"rdfs:comment\"/>'
        stub += '\t\t<IRI>' + self.namespace + '#' + classname + '</IRI>\n'
        stub += '\t<Literal datatypeIRI=\"&rdf;PlainLiteral\">' + str(message)  + '</Literal>\n'
        stub += '</AnnotationAssertion>'
        print stub
        self.doc += stub
        return 0

    def writeFile(self):
        fileh = open(self.outfile, 'w')
        self.doc += '</Ontology>\n'
        fileh.write(self.doc)
        fileh.close()
