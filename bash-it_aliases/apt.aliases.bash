# shellcheck shell=bash
#
# -binaryanomaly

cite 'about-alias'
about-alias 'Apt and dpkg aliases for Ubuntu and Debian distros.'

# set apt aliases
function _set_pkg_aliases() {
	if _command_exists apt; then
		alias apts='apt-cache search'
		alias aptshow='apt-cache show'
        alias aptclean='sudo apt clean'
		alias aptinst='sudo apt install -V'
		alias aptupd='sudo apt-get update'
		alias aptupg='sudo apt-get dist-upgrade -V && sudo apt-get autoremove'
		alias aptupgd='sudo apt-get update && sudo apt-get dist-upgrade -V && sudo apt-get autoremove'
        alias aptautorm='sudo apt autoremove'
		alias aptrm='sudo apt-get remove'
		alias aptpurge='sudo apt-get purge && sudo apt autoremove'

		alias chkup='/usr/lib/update-notifier/apt-check -p --human-readable'
		alias chkboot='cat /var/run/reboot-required'

		alias pkgfiles='dpkg --listfiles'
        alias pkgf='dpkg --listfiles'
        alias pkgl='dpkg --list'
        alias pkglist='dpkg --list'
	fi
}

_set_pkg_aliases
