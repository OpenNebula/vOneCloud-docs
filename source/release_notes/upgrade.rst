.. _upgrade:

=======
Upgrade
=======

.. warning:: If you click on **Upgrade** or **Upgrade Now** (to upgrade the vOneCloud version, or the system packages, respectively), you will see that a few jobs appear in `pending` state in the job queue. You will not receive any further user feedback until it finishes executing. This may take a long time: 15 minutes for **Upgrade**, and even more than an hour for **Upgrade Now**, depending on your internet access speed. If a job failed, it will turn to red, if it's successful, it will turn to green. So please, **be patient until all jobs finish executing**.

Upgrade from versions previous to 3.0 cannot be performed automatically. If you hold an active support subscription, please `contact OpenNebula Systems <mailto:support@opennebula.systems&subject="Upgrade to vOneCloud 3.0">`__ to schedule a vOneCloud upgrade.

When a new vOneCloud release is available for download, users with an active support subscription will be notified in the Sunstone interface (in particular, in the Control Panel link), as well as in the main Dashboard area of the Control Panel.

Operating system upgrade
^^^^^^^^^^^^^^^^^^^^^^^^

.. warning:: On vOneCloud 3.0.0 and 3.0.1, don't use **"Upgrade system"** in the Control Panel to upgrade the underlying operating system. First, upgrade the vOneCloud to 3.0.2 (or newer), then it's safe to run the OS upgrade.

Appliances with the vOneCloud 3.0.0 and 3.0.1 are based on the CentOS 7.3, and the **"Upgrade system"** triggers massive upgrade to the CentOS 7.4. During the upgrade, core vOneCloud services are restarted, and upgrade is terminated in the middle leaving the OS inconsistent. First, upgrade your appliance to the vOneCloud 3.0.2 (or newer) which addresses this problem. Then it's safe to use the **"Upgrade system"** feature via the Control Panel.
