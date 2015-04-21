.. _app_conf_trouble:

================================================================================
Troubleshooting
================================================================================

This section details what actions to take if any of the vOneCloud appliance configuration functions fails.

Cannot Check for Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the vOneCloud Repository cannot be reached this message will be displayed:

    OpenNebula Systems vOneCloud Repository is unreachable. Cannot check for upgrades. Read the Troubleshooting guide for more info.

This means that the appliance cannot reach the appliance repository at vonecloud.com. In the first place, check from your browser that this website is up: `https://downloads.vonecloud.com/version <https://downloads.vonecloud.com/version>`_, it should display a message like:

    {"error":"Invalid Data."}

If that works, then it's probably a networking configuration error. Make sure that the network of the appliance has been properly set (see :ref:`here <control_console_basic_configuration>` ). It also might be a proxy problem if the appliance requires a proxy to access the internet. If you are sure these configuration parameters are correct, perform a :ref:`manual login to the appliance <advanced_login>` and check the following items:

* Inspect the routes `ip route`
* If you are not using a proxy, make sure you can reach the Google DNS to test internet connection: `ping 8.8.8.8`.
* Run the following command: `curl -kv  https://downloads.vonecloud.com/version`. If you are using a proxy run this instead: `HTTPS_PROXY=http://<proxy_user>:<proxy_pass>@<proxy_host>:<proxy_port> curl -kv  https://downloads.vonecloud.com/version`.

If you are sure the network is properly configured, please feel free to submit a support to `vOneCloud Support <https://support.vonecloud.com/>`__.

.. _app_conf_trouble_debug:

Debug Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An Admin Task called ``Debug Info`` generates a gzipped tar file which can be downloaded that contains all the required information to debug the cloud if the OpenNebula user runs into a problem. This file can be then sent to `vOneCloud Support <https://support.vonecloud.com/>`__. Note that this sends information on all the resources of the cloud and the OpenNebula log.

.. note:: Please examine this information before sending it over if you have concerns about sensitive data that might be automatically bundled in the file.

To generate the debug information follow these steps:

.. image:: /images/generate_debug_info.png
    :align: center

To download the file click on the ``Debug Info`` job and download the file:

.. image:: /images/download_debug_info.png
    :align: center

.. _app_conf_trouble_job_failure:

Job Failure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A job should never fail. If it fails you should submit a support ticket with the attached Job Crashed Report (link found in the Job page) to `vOneCloud Support <https://support.vonecloud.com/>`__.



