.. _advanced_customizations:

================================================================================
Advanced Customizations
================================================================================

This section documents further customizations that can tailor the vOneCloud environment to your needs. However, these modifications will be lost after an upgrade. So please document the process exactly so you can replay it after upgrading the appliance.

All the customizations documented in this section require logging into the vOneCloud appliance, see the :ref:`Logging into the Appliance <advanced_login>` guide to access it.

These customizations are currently supported:

* :ref:`Rebrand vOneCloud <advanced_customizations_rebranding>`

.. warning::
    The following changes will be lost after an upgrade.

.. _advanced_customizations_rebranding:

Rebranding
--------------------------------------------------------------------------------

It is possible to change the logos of the Sunstone interface by replacing these files:

* Logo for the login screen: ``/usr/lib/one/sunstone/public/images/opennebula-sunstone-v4.0.png``. The original size is 355 x 78 px. The image will be force resized to a width of 355px.
* Logo for the admin view: ``/usr/lib/one/sunstone/public/images/opennebula-sunstone-v4.0-small.png``. The original size is 413 x 60 px.
* Logo for the group and cloud view: ``/usr/lib/one/sunstone/public/images/one_small_logo.png``. The original size is 563 x 194px.

The background of the login screen can be customized by replacing ``/usr/lib/one/sunstone/views/login.erb``, with these contents:

.. code-block:: html
    :emphasize-lines: 21

    <!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="shortcut icon" href="images/favicon.ico" />
        <title>OpenNebula Sunstone Login</title>
        <link rel="stylesheet" type="text/css" href="css/login.css" />
        <!--[if IE]>
        <script type="text/javascript" src="vendor/crypto-js/core-min.js"></script>
        <script type="text/javascript" src="vendor/crypto-js/enc-base64-min.js"></script>
        <![endif]-->

        <% if $conf[:env] == 'dev' %>
          <script src="bower_components/requirejs/require.js" data-main="app/login"></script>
        <% else %>
          <script src="dist/login.js"></script>
        <% end %>
      </head>

      <body style="
      background: url(images/%YOURIMAGE%) no-repeat center center fixed;
      -webkit-background-size: cover;
      -moz-background-size: cover;
      -o-background-size: cover;
      background-size: cover;
      ">

        <% if settings.config[:auth] == "x509" %>
        <%= erb :_login_x509 %>
        <% else %>
        <%= erb :_login_standard %>
        <% end %>

        <div id="footer" style="overflow:visible;">
          <a href="http://opennebula.org" target="_blank">OpenNebula 4.13.85</a>
          by
          <a href="http://opennebula.systems" target="_blank">OpenNebula Systems</a>
          .
        </div>
      </body>
    </html>

Make sure you replace ``%YOURIMAGE%`` in the above example with the name of your background. Upload your background image to ``/usr/lib/one/sunstone/public/images/``. For example, if we have a logo called ``server.jpg``, that line should read:

    background: url(images/server.jpg) no-repeat center center fixed;

And we should upload it to ``/usr/lib/one/sunstone/public/images/server.jpg``.

VM Template Logos
-----------------

It is possible to add new logos for the VM Templates to be displayed in Sunstone:

* Create your logo in PNG format (90 x 96 pixels).

* Log in into the appliance and place it in /usr/lib/one/sunstone/public/images/logos

* chmod +644 on the uploaded file

* In Sunstone vCenter Admin view, update the desired VM Template and select any of the built in logos. 

* Click on update again and switch to Advanced view.

* Change the the LOGO= line to LOGO="images/logos/<mylogo>.png


After any of these changes it's necessary to restart OpenNebula in the Control Panel.
