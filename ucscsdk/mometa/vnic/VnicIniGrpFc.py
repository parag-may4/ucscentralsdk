"""This module contains the general information for VnicIniGrpFc ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicIniGrpFcConsts():
    ADMIN_HOST_PORT_1 = "1"
    ADMIN_HOST_PORT_2 = "2"
    ADMIN_HOST_PORT_ANY = "ANY"
    ADMIN_HOST_PORT_NONE = "NONE"
    ADMIN_VCON_1 = "1"
    ADMIN_VCON_2 = "2"
    ADMIN_VCON_3 = "3"
    ADMIN_VCON_4 = "4"
    ADMIN_VCON_ANY = "any"
    CDN_SOURCE_USER_DEFINED = "user-defined"
    CDN_SOURCE_VNIC_NAME = "vnic-name"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    INST_TYPE_DEFAULT = "default"
    INST_TYPE_DYNAMIC = "dynamic"
    INST_TYPE_DYNAMIC_VF = "dynamic-vf"
    INST_TYPE_MANUAL = "manual"
    OPER_HOST_PORT_1 = "1"
    OPER_HOST_PORT_2 = "2"
    OPER_HOST_PORT_ANY = "ANY"
    OPER_HOST_PORT_NONE = "NONE"
    OPER_ORDER_UNSPECIFIED = "unspecified"
    OPER_SPEED_LINE_RATE = "line-rate"
    OPER_VCON_1 = "1"
    OPER_VCON_2 = "2"
    OPER_VCON_3 = "3"
    OPER_VCON_4 = "4"
    OPER_VCON_ANY = "any"
    ORDER_UNSPECIFIED = "unspecified"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    REDUNDANCY_PAIR_TYPE_NONE = "none"
    REDUNDANCY_PAIR_TYPE_PRIMARY = "primary"
    REDUNDANCY_PAIR_TYPE_SECONDARY = "secondary"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"


class VnicIniGrpFc(ManagedObject):
    """This is VnicIniGrpFc class."""

    consts = VnicIniGrpFcConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIniGrpFc", "vnicIniGrpFc", "inigrp-fc", VersionMeta.Version141a, "InputOutput", 0x1ffff, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], [u'lsServer', u'vnicFcGroupDef'], [u'fabricEthMonSrcEp', u'fabricFcMonSrcEp', u'faultInst', u'vnicIniGrpFcIf'], ["Get"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "admin_cdn_name": MoPropertyMeta("admin_cdn_name", "adminCdnName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "admin_host_port": MoPropertyMeta("admin_host_port", "adminHostPort", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "ANY", "NONE"], []), 
        "admin_vcon": MoPropertyMeta("admin_vcon", "adminVcon", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "2", "3", "4", "any"], []), 
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cdn_source": MoPropertyMeta("cdn_source", "cdnSource", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["user-defined", "vnic-name"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-roce-sriov|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-roce-vxlan|unsupported-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources),){0,64}(defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-roce-sriov|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-roce-vxlan|unsupported-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "equipment_dn": MoPropertyMeta("equipment_dn", "equipmentDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "nw_templ_name": MoPropertyMeta("nw_templ_name", "nwTemplName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_cdn_name": MoPropertyMeta("oper_cdn_name", "operCdnName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_host_port": MoPropertyMeta("oper_host_port", "operHostPort", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "ANY", "NONE"], []), 
        "oper_order": MoPropertyMeta("oper_order", "operOrder", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["line-rate"], ["8-40000000"]), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vcon": MoPropertyMeta("oper_vcon", "operVcon", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4", "any"], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["unspecified"], ["0-256"]), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "redundancy_pair_type": MoPropertyMeta("redundancy_pair_type", "redundancyPairType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "primary", "secondary"], []), 
        "redundancy_peer": MoPropertyMeta("redundancy_peer", "redundancyPeer", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2000, 0, 256, None, [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "adminCdnName": "admin_cdn_name", 
        "adminHostPort": "admin_host_port", 
        "adminVcon": "admin_vcon", 
        "bootDev": "boot_dev", 
        "cdnSource": "cdn_source", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "equipmentDn": "equipment_dn", 
        "fltAggr": "flt_aggr", 
        "identPoolName": "ident_pool_name", 
        "instType": "inst_type", 
        "name": "name", 
        "nwTemplName": "nw_templ_name", 
        "operCdnName": "oper_cdn_name", 
        "operHostPort": "oper_host_port", 
        "operOrder": "oper_order", 
        "operSpeed": "oper_speed", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operVcon": "oper_vcon", 
        "order": "order", 
        "owner": "owner", 
        "pinToGroupName": "pin_to_group_name", 
        "qosPolicyName": "qos_policy_name", 
        "redundancyPairType": "redundancy_pair_type", 
        "redundancyPeer": "redundancy_peer", 
        "rn": "rn", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_profile_name = None
        self.admin_cdn_name = None
        self.admin_host_port = None
        self.admin_vcon = None
        self.boot_dev = None
        self.cdn_source = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.equipment_dn = None
        self.flt_aggr = None
        self.ident_pool_name = None
        self.inst_type = None
        self.name = None
        self.nw_templ_name = None
        self.oper_cdn_name = None
        self.oper_host_port = None
        self.oper_order = None
        self.oper_speed = None
        self.oper_stats_policy_name = None
        self.oper_vcon = None
        self.order = None
        self.owner = None
        self.pin_to_group_name = None
        self.qos_policy_name = None
        self.redundancy_pair_type = None
        self.redundancy_peer = None
        self.stats_policy_name = None
        self.status = None
        self.switch_id = None
        self.type = None

        ManagedObject.__init__(self, "VnicIniGrpFc", parent_mo_or_dn, **kwargs)

