.. _vcenter_ds:

=================================
Storage DRS and datastore cluster
=================================

Thanks to vOneCloud's scheduler, you can manage your datastores clusters with load distribution but you may already be using `vCenter’s Storage DRS <http://pubs.vmware.com/vsphere-60/index.jsp?topic=%2Fcom.vmware.vsphere.hostclient.doc%2FGUID-598DF695-107E-406B-9C95-0AF961FC227A.html>`__ capabilities. Storage DRS allows you to manage the aggregated resources of a datastore cluster. If you're using Storage DRS, vOneCloud can delegate the decision of selecting a datastore to the Storage DRS cluster (SDRS) but as this behavior interferes with vOneCloud's scheduler and vSphere’s API impose some restrictions, there will be some limitations in StorageDRS support in vOneCloud.

When you import a SDRS cluster using onevcenter or Sunstone:

* The cluster will be imported as a SYSTEM datastore only.
* vOneCloud detects the datastores grouped by the SDRS cluster so you can still import those datastores as both IMAGE and SYSTEM datastores.
* Non-persistent images are not supported by a SDRS as vSphere’s API does not provide a way to create, copy or delete files to a SDRS cluster as a whole, however you can use persistent and volatile images with the VMs backed by your SDRS.
* Linked clones over SDRS are not supported by vOneCloud, so when a VM clone is created a full clone is performed.

In order to delegate the datastore selection to the SDRS cluster you must inform vOneCloud's scheduler that you want to use specifically the SYSTEM datastore representing the storage cluster. You can edit a VM template and select the storage cluster in the Scheduling tab. 

Current support has the following limitations:

* Images in StoragePods can't be imported through Sunstone although it's possible to import them from a datastore, which is a member of a storage cluster, if it has been imported previously as an individual datastore.
* New images like VMDK files cannot be created or uploaded to the StoragePod as it's set as a SYSTEM datastore. However, it's possible to create an image and upload it to a datastore which is a member of a storage cluster it has been imported previously as an individual datastore.
