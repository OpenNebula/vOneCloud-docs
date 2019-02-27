.. _marketplace:

================================================================================
Marketplace
================================================================================

OpenNebula Systems provides a public and official Marketplace, universally available to all the OpenNebula’s. The OpenNebula Marketplace is a catalog of third party virtual appliances ready to run in OpenNebula environments. This Marketplace is available  `here <http://marketplace.opennebula.systems>`__. More information on the public Marketplace can be found :onedoc:`here <advanced_components/marketplace/market_one.html>`.

Additionally, admins can create private marketplaces:

  - :onedoc:`HTTP Marketplaces <advanced_components/marketplace/market_http.html>`
  - :onedoc:`S3 Marketplaces <advanced_components/marketplace/market_s3.html>`

.. note:: Please note that if you make changes to /etc/one/oned.conf they'll be overwritten by the automatic update process. You'll need to re add any changes after the update.

Requirements
============

The url http://marketplace.opennebula.systems must be reachable from the OpenNebula Frontend.


Using MarketplaceApps
=====================

In order to use a vCenter app it is needed to attach the image to one vCenter VM Template which had been previously imported. An existing VM Template can be cloned and its disks replaced with the image from the marketplace. Once the VM Template its ready the appliance can be instantiated.

**Listing MarketplaceApps**

.. image:: /images/listing_marketplaceapps.png
    :align: center


**Show a particular MarketplaceApp**

.. image:: /images/show_marketplaceapp.png
    :align: center

**Create a MarketplaceApp**

.. image:: /images/create_marketplaceapp.png
    :align: center

**Additional Commands**

Like any other vOneCloud resource, MarketplaceApps respond to the base actions, namely:

- delete
- update
- chgrp
- chown
- chmod
- enable
- disable
