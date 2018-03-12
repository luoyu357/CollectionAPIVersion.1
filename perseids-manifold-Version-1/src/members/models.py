from src.utils.base.models import Model


class MemberResultSet(Model):
    def __init__(self, contents=None, nextCursor=None, prevCursor=None):
        assert all(map(lambda r: r is not None, [contents]))
        self.contents = contents
        if nextCursor is not None:
            self.nextCursor = nextCursor
        if prevCursor :
            self.prevCursor = prevCursor


class MemberItem(Model):
    def __init__(self, id=None, location=None, datatype=None, ontology=None, mappings=None, provenance=None):
        assert all(map(lambda r: r is not None, [id, location, provenance]))
        self.id = id
        self.location = location
        if datatype is not None:
            self.datatype = datatype
        if ontology is not None:
            self.ontology = ontology
        if mappings is not None:
            self.mappings = mappings if type(mappings) is CollectionItemMappingMetadata else CollectionItemMappingMetadata(**mappings)
        if provenance is not None:
            self.provenance = provenance if type(provenance) is MemberProvenance else MemberProvenance(**provenance)


class CollectionItemMappingMetadata(Model):
    def __init__(self, role=None, index=None, dateAdded=None):
        assert any(map(lambda r: r is not None, [role, index, dateAdded]))
        self.role = role
        self.index = index
        self.dateAdded = dateAdded

class MemberProvenance(Model):
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

classList = [MemberItem, CollectionItemMappingMetadata, MemberProvenance]
