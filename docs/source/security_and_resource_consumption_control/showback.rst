.. _showback:

========
Showback
========

vOneCloud ships with functionality to report resource usage cost. Showback reports are genereted daily (at midnight)using the information retrieved from OpenNebula.

**Set the VM Cost**

Each VM Template can optionally define a cost. The cost is defined as cost per cpu per hour, and cost per memory MB per hour. The cost units are abstract and their equivalent to monetary or other cost metrics have to be defined in each deployment.

This cost is defined per VM Template by the Cloud Administrator at the time of creating or updating a VM Template, applying a cost to the total Memory and CPU of the VMs that will be spawn from this VM Template.

.. image:: /images/set_template_cost.png
    :align: center


**Retrieve Monthly Reports**

Any user or administrator can see their monthly showback reports clicking on their user icon to access Settings.


.. image:: /images/get_to_settings.png
    :align: center

And clicking on the Showback tab, obtain the cost consumed by clicking on the "Get Showback"


.. image:: /images/show_showback.png
    :align: center

Learn more on the :doc:`Showback functionality <administration/users_and_groups/showback.html>`.
