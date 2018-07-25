.. _resolved_issues_in_3.0.5:

========================
Resolved Issues in 3.0.5
========================

vOneCloud 3.0.5 is a maintenance release with the following bugfixes:

- Race condition in the datastore monitoring drivers.
- Fix for broken host overcommitment.
- Image selection shouldn’t list images in ERROR state.
- Cluster update dialog breaks RESERVED_* attributes.
- Improve Network Topology.
- Duplicated NIC when save a template.
- Size error when instantiate vCenter template.
- Added missing commands to onedb to manipulate history records.
- VMGroup & DS datatables broken in vCenter Cloud View.
- Fix for error retrieve VMGroup.
- Downloader may get too small VMDK part to estimate image size.
- Added support for setting the CPU model.
- Enable Sunstone VM Log Scrollbar at the end of the file by default.
- Accounting tables not ordered by date correctly.
- DS quotas shouldnt show the system type.
- Does not retrieve the capacity unit in volatile disks.
- CPU Model broken if CUSTOMIZATION attribute doesn't exist.
- Error importing VM Templates from vCenter with no RP attached.
- Fix CPU model and live migration problem.
- Sunstone VM template wizard resets CPU_MODEL.
- Cannot resize VM disk.
- Cannot instantiate VM with volatile image.
- Monitor fails when vCenter clusters shared moref between vCenter instances.
- Sunstone VM template wizard resets CPU_MODEL.
- Sunstone datastore creation fails on missing DS_MAD, TM_MAD.
- Broken vCenter REQUIRED_ATTRS in DS creation.
- Doesn’t retrieve VMs in VMGroup datatable.
- Set content-type for oneflow requests. Prevent RangeError when parsing big templates.
- Fix ‘LastPass detected a login form that is insecure’ message.
- Users can remove VM_RESTRICTED_ATTR fields.
- Sunstone: No way for update VM configuration if it has restricted vector atributes.
- Resolved problems related to network and disk monitoring.
- VCenter driver should allow template instantiation without mac duplication.
- Floating IP lease is not released after router removal.
