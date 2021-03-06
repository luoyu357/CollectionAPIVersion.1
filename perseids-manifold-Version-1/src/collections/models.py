import datetime
from random import randint

from src.utils.base.errors import ModelError
from src.utils.base.models import Model


class CollectionResultSet(Model):
    def __init__(self, contents, nextCursor=None, prevCursor=None):
        self.contents = contents
        if nextCursor:
            self.nextCursor = nextCursor
        if prevCursor:
            self.prevCursor = prevCursor


class CollectionObject(Model):
    def __init__(self, id=None, capabilities=None, properties=None, description=None, provenance=None):
        if any(x is None for x in [id, capabilities, properties, provenance]):
            raise ModelError()
        self.id = id or 'http://example.org/mem/'+str(randint(100000, 999999)) # todo: make parsing safe and id minting formalized, e.g. give Service Object a function
        self.capabilities = capabilities if isinstance(capabilities, CollectionCapabilities) else CollectionCapabilities(**capabilities)
        self.properties = properties if isinstance(properties, CollectionProperties) else CollectionProperties(**properties)
        self.description = description
        self.provenance = provenance if isinstance(provenance, CollectionProvenance) else CollectionProvenance(**provenance)


class CollectionCapabilities(Model):
    def __init__(self,
                 isOrdered=None,
                 appendsToEnd=None,
                 supportsRoles=None,
                 membershipIsMutable=None,
                 propertiesAreMutable=None,
                 restrictedToType=None,
                 maxLength=None):
        if any(map(lambda x: x is None, [isOrdered,  appendsToEnd, supportsRoles, membershipIsMutable, propertiesAreMutable, restrictedToType, maxLength])):
            raise ModelError()
        self.isOrdered = isOrdered
        self.supportsRoles = supportsRoles
        self.appendsToEnd = appendsToEnd
        self.membershipIsMutable = membershipIsMutable
        self.propertiesAreMutable = propertiesAreMutable
        self.restrictedToType = restrictedToType
        self.maxLength = maxLength


class CollectionProperties(Model):
    def __init__(self,
                 ownership=None,
                 license=None,
                 modelType=None,
                 hasAccessRestrictions=None,
                 memberOf=None,
                 descriptionOntology=None,
                 dateCreated=None):
        if any(map(lambda x: x is None, [ownership, license, modelType, hasAccessRestrictions, descriptionOntology])):
            raise ModelError()
        self.ownership = ownership
        self.license = license
        self.modelType = modelType
        self.hasAccessRestrictions = hasAccessRestrictions
        self.descriptionOntology = descriptionOntology
        self.memberOf = []
        self.dateCreated = dateCreated or datetime.datetime.now().isoformat()
        if memberOf is not None:
            self.memberOf = sorted(memberOf)

class CollectionProvenance(Model):
    def __init__(self,
                 wasDerivedFrom=None,
                 wasRevisionOf=None,
                 wasQuotedFrom=None,
                 hasPrimarySource=None,
                 alternateOf=None,
                 specializationOf=None):
        self.wasDerivedFrom = wasDerivedFrom
        self.wasRevisionOf = wasRevisionOf
        self.wasQuotedFrom = wasQuotedFrom
        self.hasPrimarySource = hasPrimarySource
        self.alternateOf = alternateOf
        self.specializationOf = specializationOf

classList = [CollectionObject, CollectionCapabilities, CollectionProperties, CollectionProvenance]
