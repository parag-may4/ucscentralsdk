"""This module contains the general information for IdentRequestEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentRequestEpConsts():
    pass


class IdentRequestEp(ManagedObject):
    """This is IdentRequestEp class."""

    consts = IdentRequestEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("IdentRequestEp", "identRequestEp", "IdentQ", VersionMeta.Version111a, "InputOutput", 0xf, [], ["read-only"], [u'fdBlade', u'fdRackUnit', u'lsServer'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "req_dn": MoPropertyMeta("req_dn", "reqDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "req_id": MoPropertyMeta("req_id", "reqId", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "reqDn": "req_dn", 
        "reqId": "req_id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.req_dn = None
        self.req_id = None
        self.status = None

        ManagedObject.__init__(self, "IdentRequestEp", parent_mo_or_dn, **kwargs)

