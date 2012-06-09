i3n
===

i3n is a set of tools I wrote and I use for my favorite window manager: i3.
The following tools are currently available:

- i3n-bar: run as i3bar status command and show annotation for each workspace
- i3n: cli tool providing helpers for i3 and used to control i3n-bar


Setup
-----

The fastest and more common way to install i3n is using pip::

    pip install i3n


If you use Debian, you can also use Tecknet repositories. Add this line in your
``/etc/apt/source.list`` file::

    deb http://debian.tecknet.org/debian squeeze tecknet
    deb-src http://debian.tecknet.org/debian squeeze tecknet

Add the Tecknet repositories key in your keyring::

    # wget http://debian.tecknet.org/debian/public.key -O - | apt-key add -

Then, update and install::

    # aptitude update
    # aptitude install i3n

Usage
-----

Configure i3bar to use i3nbar as status command, for example::

    bar {
        status_command i3n-bar {{ OUTPUT }}
    }

{{ OUTPUT }} is the name of your screen as shown in xrandr output.

If you use a multi-monitor setup, configure a bar for each output::


    bar {
        OUTPUT DVI-I-1
        status_command i3n-bar DVI-I-1
    }

    bar {
        OUTPUT DVI-I-2
        status_command i3n-bar DVI-I-2 --slave
    }


.. note::

   Only one i3n-bar process should run in master (without --slave argument)


Restart i3 (type ``i3 restart`` in a shell). Now you can annotate your
workspaces with i3n::

    i3n annotate "My annotation"


You can create a shortcut to annotate using zenity::

    bindsym $mod+Mod1+space exec i3n annotate "`zenity --entry`"
