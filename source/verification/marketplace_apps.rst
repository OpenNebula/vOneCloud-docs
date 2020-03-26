.. _marketplace_apps:

================
Marketplace Apps
================

Another verification step that can be performed involves importing a marketplace app into your vCenter server.

The overall process consists on importing an appliance's image from the OpenNebula public marketplace into a vCenter datastore and add it to a VM Template.

Following the next steps, you will be able to import a marketplace app into vCenter.

- Import a vcenter template. You can follow :ref:`Import a template <import_vm_templates>`. You can create a new empty template, without disks, in vCenter or use an existing vCenter VM Template.

- Remove disks from the imported VM Template. Skip this step if you imported an empty VM Template.

At this point we have a vCenter VM Template ready to have a marketplace image attached.

- Access to marketplace and search for the desired app, in this example, we're searching a Centos 7 app. Click on the "Import into datastore" icon.

.. image:: /images/marketplace_apps.png

.. note:: Remember that you can use also KVM apps. KVM apps are in qcow2 format and are converter into vmdk when downloading to a vCenter datastore.

- Select the target datastore, where the image will be saved, change the name if needed and click "Download".

.. image:: /images/marketplace_download.png

- Go to ``Storage --> Images`` and wait until Status change from LOCKED to READY. It may take some time depending on the app size.

Status LOCKED means that app is still in the downloading process.

.. image:: /images/marketplace_downloading.png

Status READY means that app is already downloaded.

.. image:: /images/marketplace_image_ready.png

- Remove the unnecessary template creating at downloading time. This template is not valid for a vCenter environment.

.. image:: /images/marketplace_template_trash.png

- Click on "Delete"

.. image:: /images/marketplace_template_delete.png

.. warning:: Do no click on "Delete all images". If you remove all images you'll remove the app image that is needed to attach to the template.

- Go to ``Templates --> VMs`` , select your imported template and click on "Update"

.. image:: /images/marketplace_template_update.png

- Click on the "Storage" tab and change the disk image to the downloading app image, in our example, CentOS 7 image. Click on update to apply the changes.

.. image:: /images/marketplace_template_update_disk.png

- Also you can customize network or context to easily connect by ssh when the instance was deployed.

Select the desired network.

.. image:: /images/marketplace_template_update_net.png

In this example our selected network has an AR associated.

.. image:: /images/marketplace_vnet_ar.png

Modify context parameter to add a SSH public key. Marking as check "Add SSH contextualization"

Mark as check "Add Network contextualization" to allow OpenNebula can modify IP Address on the VM.

.. image:: /images/marketplace_template_update_context.png

.. note:: Refer to OpenNebula doc "vCenter Contextualization and Customization" for more details about contextualization.

- Now you can follow the steps provided in the previous verification :ref:`Run a Virtual Machine <run_vm>` to instantiate a new VM from this VM Template.

- Alternatively you can go to ``Templates --> VMs`` , select the template and click on "Instantiate"

.. image:: /images/marketplace_template_instantiate.png

- Choose a VM name or leave empty if you want OpenNebula rename the VM, and change the parameters you need to modify as CPU, Memory... and click on "Instantiate"

.. image:: /images/marketplace_template_instantiating.png

Once the instantiation is completed, check the IP in ``Instances --> VMs``

.. image:: /images/marketplace_instance_ip.png

That's it! You have a fully featured and healthy cloud environment.
And connect to the VM using SSH

.. image:: /images/marketplace_instance_ssh.png
