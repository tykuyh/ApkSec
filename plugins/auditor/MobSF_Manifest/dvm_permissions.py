
# Androguard is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Androguard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Androguard.  If not, see <http://www.gnu.org/licenses/>.

# frameworks/base/core/res/AndroidManifest.xml
########################################## PERMISSIONS ###################
DVM_PERMISSIONS = {
    "MANIFEST_PERMISSION": {
        "SEND_SMS": ["dangerous", "send SMS messages", "Allows application to send SMS messages. Malicious applications may cost you money by sending messages without your confirmation."],
        "SEND_SMS_NO_CONFIRMATION": ["dangerous", "send SMS messages", "send SMS messages via the Messaging app with no user input or confirmation"],
        "CALL_PHONE": ["dangerous", "directly call phone numbers", "Allows the application to call phone numbers without your intervention. Malicious applications may cause unexpected calls on your phone bill. Note that this does not allow the application to call emergency numbers."],
        "RECEIVE_SMS": ["dangerous", "receive SMS", "Allows application to receive and process SMS messages. Malicious applications may monitor your messages or delete them without showing them to you."],
        "RECEIVE_MMS": ["dangerous", "receive MMS", "Allows application to receive and process MMS messages. Malicious applications may monitor your messages or delete them without showing them to you."],
        "READ_SMS": ["dangerous", "read SMS or MMS", "Allows application to read SMS messages stored on your phone or SIM card. Malicious applications may read your confidential messages."],
        "WRITE_SMS": ["dangerous", "edit SMS or MMS", "Allows application to write to SMS messages stored on your phone or SIM card. Malicious applications may delete your messages."],
        "RECEIVE_WAP_PUSH": ["dangerous", "receive WAP", "Allows application to receive and process WAP messages. Malicious applications may monitor your messages or delete them without showing them to you."],
        "READ_CONTACTS": ["dangerous", "read contact data", "Allows an application to read all of the contact (address) data stored on your phone. Malicious applications can use this to send your data to other people."],
        "WRITE_CONTACTS": ["dangerous", "write contact data", "Allows an application to modify the contact (address) data stored on your phone. Malicious applications can use this to erase or modify your contact data."],
        "READ_PROFILE": ["dangerous", "read the user's personal profile data", "Allows an application to read the user's personal profile data."],
        "WRITE_PROFILE": ["dangerous", "write the user's personal profile data", "Allows an application to write (but not read) the user's personal profile data."],
        "READ_SOCIAL_STREAM": ["dangerous", "read from the user's social stream", "Allows an application to read from the user's social stream."],
        "WRITE_SOCIAL_STREAM": ["dangerous", "write the user's social stream", "Allows an application to write (but not read) the user's social stream data."],
        "READ_CALENDAR": ["dangerous", "read calendar events", "Allows an application to read all of the calendar events stored on your phone. Malicious applications can use this to send your calendar events to other people."],

        "WRITE_CALENDAR": ["dangerous", "add or modify calendar events and send emails to guests", "Allows an application to add or change the events on your calendar, which may send emails to guests. Malicious applications can use this to erase or modify your calendar events or to send emails to guests."],
        "READ_USER_DICTIONARY": ["dangerous", "read user-defined dictionary", "Allows an application to read any private words, names and phrases that the user may have stored in the user dictionary."],
        "WRITE_USER_DICTIONARY": ["normal", "write to user-defined dictionary", "Allows an application to write new words into the user dictionary."],
        "READ_HISTORY_BOOKMARKS": ["dangerous", "read Browser\'s history and bookmarks", "Allows the application to read all the URLs that the browser has visited and all of the browser\'s bookmarks."],
        "WRITE_HISTORY_BOOKMARKS": ["dangerous", "write Browser\'s history and bookmarks", "Allows an application to modify the browser\'s history or bookmarks stored on your phone. Malicious applications can use this to erase or modify your browser\'s data."],
        "SET_ALARM": ["normal", "set alarm in alarm clock", "Allows the application to set an alarm in an installed alarm clock application. Some alarm clock applications may not implement this feature."],
        "ACCESS_FINE_LOCATION": ["dangerous", "fine (GPS) location", "Access fine location sources, such as the Global Positioning System on the phone, where available. Malicious applications can use this to determine where you are and may consume additional battery power."],
        "ACCESS_COARSE_LOCATION": ["dangerous", "coarse (network-based) location", "Access coarse location sources, such as the mobile network database, to determine an approximate phone location, where available. Malicious applications can use this to determine approximately where you are."],
        "ACCESS_MOCK_LOCATION": ["dangerous", "mock location sources for testing", "Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real-location sources such as GPS or Network providers."],
        "ACCESS_LOCATION_EXTRA_COMMANDS": ["normal", "access extra location provider commands", "Access extra location provider commands. Malicious applications could use this to interfere with the operation of the GPS or other location sources."],
        "INSTALL_LOCATION_PROVIDER": ["signatureOrSystem", "permission to install a location provider", "Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real-location sources such as GPS or Network providers, or monitor and report your location to an external source."],
        "INTERNET": ["dangerous", "full Internet access", "Allows an application to create network sockets."],
        "ACCESS_NETWORK_STATE": ["normal", "view network status", "Allows an application to view the status of all networks."],
        "ACCESS_WIFI_STATE": ["normal", "view Wi-Fi status", "Allows an application to view the information about the status of Wi-Fi."],
        "BLUETOOTH": ["dangerous", "create Bluetooth connections", "Allows an application to view configuration of the local Bluetooth phone and to make and accept connections with paired devices."],
        "NFC": ["dangerous", "control Near-Field Communication", "Allows an application to communicate with Near-Field Communication (NFC) tags, cards and readers."],
        "USE_SIP": ["dangerous", "make/receive Internet calls", "Allows an application to use the SIP service to make/receive Internet calls."],
        "ACCOUNT_MANAGER": ["signature", "act as the Account Manager Service", "Allows an application to make calls to Account Authenticators"],
        "GET_ACCOUNTS": ["normal", "discover known accounts", "Allows an application to access the list of accounts known by the phone."],
        "AUTHENTICATE_ACCOUNTS": ["dangerous", "act as an account authenticator", "Allows an application to use the account authenticator capabilities of the Account Manager, including creating accounts as well as obtaining and setting their passwords."],
        "USE_CREDENTIALS": ["dangerous", "use the authentication credentials of an account", "Allows an application to request authentication tokens."],
        "MANAGE_ACCOUNTS": ["dangerous", "manage the accounts list", "Allows an application to perform operations like adding and removing accounts and deleting their password."],
        "MODIFY_AUDIO_SETTINGS": ["dangerous", "change your audio settings", "Allows application to modify global audio settings, such as volume and routing."],
        "RECORD_AUDIO": ["dangerous", "record audio", "Allows application to access the audio record path."],
        "CAMERA": ["dangerous", "take pictures and videos", "Allows application to take pictures and videos with the camera. This allows the application to collect images that the camera is seeing at any time."],
        "VIBRATE": ["normal", "control vibrator", "Allows the application to control the vibrator."],
        "FLASHLIGHT": ["normal", "control flashlight", "Allows the application to control the flashlight."],
        "ACCESS_USB": ["signatureOrSystem", "access USB devices", "Allows the application to access USB devices."],
        "HARDWARE_TEST": ["signature", "test hardware", "Allows the application to control various peripherals for the purpose of hardware testing."],
        "PROCESS_OUTGOING_CALLS": ["dangerous", "intercept outgoing calls", "Allows application to process outgoing calls and change the number to be dialled. Malicious applications may monitor, redirect or prevent outgoing calls."],
        "MODIFY_PHONE_STATE": ["signatureOrSystem", "modify phone status", "Allows the application to control the phone features of the device. An application with this permission can switch networks, turn the phone radio on and off and the like, without ever notifying you."],
        "READ_PHONE_STATE": ["dangerous", "read phone state and identity", "Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and so on."],
        "WRITE_EXTERNAL_STORAGE": ["dangerous", "read/modify/delete SD card contents", "Allows an application to write to the SD card."],
        "READ_EXTERNAL_STORAGE": ["dangerous", "read SD card contents", "Allows an application to read from SD Card."],
        "WRITE_SETTINGS": ["dangerous", "modify global system settings", "Allows an application to modify the system\'s settings data. Malicious applications can corrupt your system\'s configuration."],
        "WRITE_SECURE_SETTINGS": ["signatureOrSystem", "modify secure system settings", "Allows an application to modify the system\'s secure settings data. Not for use by common applications."],
        "WRITE_GSERVICES": ["signatureOrSystem", "modify the Google services map", "Allows an application to modify the Google services map. Not for use by common applications."],
        "EXPAND_STATUS_BAR": ["normal", "expand/collapse status bar", "Allows application to expand or collapse the status bar."],
        "GET_TASKS": ["dangerous", "retrieve running applications", "Allows application to retrieve information about currently and recently running tasks. May allow malicious applications to discover private information about other applications."],
        "REORDER_TASKS": ["dangerous", "reorder applications running", "Allows an application to move tasks to the foreground and background. Malicious applications can force themselves to the front without your control."],
        "CHANGE_CONFIGURATION": ["dangerous", "change your UI settings", "Allows an application to change the current configuration, such as the locale or overall font size."],
        "RESTART_PACKAGES": ["normal", "kill background processes", "Allows an application to kill background processes of other applications, even if memory is not low."],
        "KILL_BACKGROUND_PROCESSES": ["normal", "kill background processes", "Allows an application to kill background processes of other applications, even if memory is not low."],
        "FORCE_STOP_PACKAGES": ["signature", "force-stop other applications", "Allows an application to stop other applications forcibly."],
        "DUMP": ["signatureOrSystem", "retrieve system internal status", "Allows application to retrieve internal status of the system. Malicious applications may retrieve a wide variety of private and secure information that they should never commonly need."],
        "SYSTEM_ALERT_WINDOW": ["dangerous", "display system-level alerts", "Allows an application to show system-alert windows. Malicious applications can take over the entire screen of the phone."],
        "SET_ANIMATION_SCALE": ["dangerous", "modify global animation speed", "Allows an application to change the global animation speed (faster or slower animations) at any time."],
        "PERSISTENT_ACTIVITY": ["dangerous", "make application always run", "Allows an application to make parts of itself persistent, so that the system can\'t use it for other applications."],
        "GET_PACKAGE_SIZE": ["normal", "measure application storage space", "Allows an application to retrieve its code, data and cache sizes"],
        "SET_PREFERRED_APPLICATIONS": ["signature", "set preferred applications", "Allows an application to modify your preferred applications. This can allow malicious applications to silently change the applications that are run, spoofing your existing applications to collect private data from you."],
        "RECEIVE_BOOT_COMPLETED": ["normal", "automatically start at boot", "Allows an application to start itself as soon as the system has finished booting. This can make it take longer to start the phone and allow the application to slow down the overall phone by always running."],
        "BROADCAST_STICKY": ["normal", "send sticky broadcast", "Allows an application to send sticky broadcasts, which remain after the broadcast ends. Malicious applications can make the phone slow or unstable by causing it to use too much memory."],
        "WAKE_LOCK": ["dangerous", "prevent phone from sleeping", "Allows an application to prevent the phone from going to sleep."],
        "SET_WALLPAPER": ["normal", "set wallpaper", "Allows the application to set the system wallpaper."],
        "SET_WALLPAPER_HINTS": ["normal", "set wallpaper size hints", "Allows the application to set the system wallpaper size hints."],
        "SET_TIME": ["signatureOrSystem", "set time", "Allows an application to change the phone\'s clock time."],
        "SET_TIME_ZONE": ["dangerous", "set time zone", "Allows an application to change the phone\'s time zone."],
        "MOUNT_UNMOUNT_FILESYSTEMS": ["dangerous", "mount and unmount file systems", "Allows the application to mount and unmount file systems for removable storage."],
        "MOUNT_FORMAT_FILESYSTEMS": ["dangerous", "format external storage", "Allows the application to format removable storage."],
        "ASEC_ACCESS": ["signature", "get information on internal storage", "Allows the application to get information on internal storage."],
        "ASEC_CREATE": ["signature", "create internal storage", "Allows the application to create internal storage."],
        "ASEC_DESTROY": ["signature", "destroy internal storage", "Allows the application to destroy internal storage."],
        "ASEC_MOUNT_UNMOUNT": ["signature", "mount/unmount internal storage", "Allows the application to mount/unmount internal storage."],
        "ASEC_RENAME": ["signature", "rename internal storage", "Allows the application to rename internal storage."],
        "DISABLE_KEYGUARD": ["dangerous", "disable key lock", "Allows an application to disable the key lock and any associated password security. A legitimate example of this is the phone disabling the key lock when receiving an incoming phone call, then re-enabling the key lock when the call is finished."],
        "READ_SYNC_SETTINGS": ["normal", "read sync settings", "Allows an application to read the sync settings, such as whether sync is enabled for Contacts."],
        "WRITE_SYNC_SETTINGS": ["dangerous", "write sync settings", "Allows an application to modify the sync settings, such as whether sync is enabled for Contacts."],
        "READ_SYNC_STATS": ["normal", "read sync statistics", "Allows an application to read the sync stats; e.g. the history of syncs that have occurred."],
        "WRITE_APN_SETTINGS": ["dangerous", "write Access Point Name settings", "Allows an application to modify the APN settings, such as Proxy and Port of any APN."],
        "SUBSCRIBED_FEEDS_READ": ["normal", "read subscribed feeds", "Allows an application to receive details about the currently synced feeds."],
        "SUBSCRIBED_FEEDS_WRITE": ["dangerous", "write subscribed feeds", "Allows an application to modify your currently synced feeds. This could allow a malicious application to change your synced feeds."],
        "CHANGE_NETWORK_STATE": ["dangerous", "change network connectivity", "Allows an application to change the state of network connectivity."],
        "CHANGE_WIFI_STATE": ["dangerous", "change Wi-Fi status", "Allows an application to connect to and disconnect from Wi-Fi access points and to make changes to configured Wi-Fi networks."],
        "CHANGE_WIFI_MULTICAST_STATE": ["dangerous", "allow Wi-Fi Multicast reception", "Allows an application to receive packets not directly addressed to your device. This can be useful when discovering services offered nearby. It uses more power than the non-multicast mode."],
        "BLUETOOTH_ADMIN": ["dangerous", "bluetooth administration", "Allows an application to configure the local Bluetooth phone and to discover and pair with remote devices."],
        "CLEAR_APP_CACHE": ["dangerous", "delete all application cache data", "Allows an application to free phone storage by deleting files in application cache directory. Access is usually very restricted to system process."],
        "READ_LOGS": ["dangerous", "read sensitive log data", "Allows an application to read from the system\'s various log files. This allows it to discover general information about what you are doing with the phone, potentially including personal or private information."],
        "SET_DEBUG_APP": ["dangerous", "enable application debugging", "Allows an application to turn on debugging for another application. Malicious applications can use this to kill other applications."],
        "SET_PROCESS_LIMIT": ["dangerous", "limit number of running processes", "Allows an application to control the maximum number of processes that will run. Never needed for common applications."],
        "SET_ALWAYS_FINISH": ["dangerous", "make all background applications close", "Allows an application to control whether activities are always finished as soon as they go to the background. Never needed for common applications."],
        "SIGNAL_PERSISTENT_PROCESSES": ["dangerous", "send Linux signals to applications", "Allows application to request that the supplied signal be sent to all persistent processes."],
        "DIAGNOSTIC": ["signature", "read/write to resources owned by diag", "Allows an application to read and write to any resource owned by the diag group; for example, files in /dev. This could potentially affect system stability and security. This should ONLY be used for hardware-specific diagnostics by the manufacturer or operator."],
        "STATUS_BAR": ["signatureOrSystem", "disable or modify status bar", "Allows application to disable the status bar or add and remove system icons."],
        "STATUS_BAR_SERVICE": ["signature", "status bar", "Allows the application to be the status bar."],
        "FORCE_BACK": ["signature", "force application to close", "Allows an application to force any activity that is in the foreground to close and go back. Should never be needed for common applications."],
        "UPDATE_DEVICE_STATS": ["signatureOrSystem", "modify battery statistics", "Allows the modification of collected battery statistics. Not for use by common applications."],
        "INTERNAL_SYSTEM_WINDOW": ["signature", "display unauthorised windows", "Allows the creation of windows that are intended to be used by the internal system user interface. Not for use by common applications."],
        "MANAGE_APP_TOKENS": ["signature", "manage application tokens", "Allows applications to create and manage their own tokens, bypassing their common Z-ordering. Should never be needed for common applications."],
        "INJECT_EVENTS": ["signature", "press keys and control buttons", "Allows an application to deliver its own input events (key presses, etc.) to other applications. Malicious applications can use this to take over the phone."],
        "SET_ACTIVITY_WATCHER": ["signature", "monitor and control all application launching", "Allows an application to monitor and control how the system launches activities. Malicious applications may compromise the system completely. This permission is needed only for development, never for common phone usage."],
        "SHUTDOWN": ["signature", "partial shutdown", "Puts the activity manager into a shut-down state. Does not perform a complete shut down."],
        "STOP_APP_SWITCHES": ["signature", "prevent app switches", "Prevents the user from switching to another application."],
        "READ_INPUT_STATE": ["signature", "record what you type and actions that you take", "Allows applications to watch the keys that you press even when interacting with another application (such as entering a password). Should never be needed for common applications."],
        "BIND_INPUT_METHOD": ["signature", "bind to an input method", "Allows the holder to bind to the top-level interface of an input method. Should never be needed for common applications."],
        "BIND_WALLPAPER": ["signatureOrSystem", "bind to wallpaper", "Allows the holder to bind to the top-level interface of wallpaper. Should never be needed for common applications."],
        "BIND_DEVICE_ADMIN": ["signature", "interact with device admin", "Allows the holder to send intents to a device administrator. Should never be needed for common applications."],
        "SET_ORIENTATION": ["signature", "change screen orientation", "Allows an application to change the rotation of the screen at any time. Should never be needed for common applications."],
        "INSTALL_PACKAGES": ["signatureOrSystem", "directly install applications", "Allows an application to install new or updated Android packages. Malicious applications can use this to add new applications with arbitrarily powerful permissions."],
        "CLEAR_APP_USER_DATA": ["signature", "delete other applications\' data", "Allows an application to clear user data."],
        "DELETE_CACHE_FILES": ["signatureOrSystem", "delete other applications\' caches", "Allows an application to delete cache files."],
        "DELETE_PACKAGES": ["signatureOrSystem", "delete applications", "Allows an application to delete Android packages. Malicious applications can use this to delete important applications."],
        "MOVE_PACKAGE": ["signatureOrSystem", "Move application resources", "Allows an application to move application resources from internal to external media and vice versa."],
        "CHANGE_COMPONENT_ENABLED_STATE": ["signatureOrSystem", "enable or disable application components", "Allows an application to change whether or not a component of another application is enabled. Malicious applications can use this to disable important phone capabilities. It is important to be careful with permission, as it is possible to bring application components into an unusable, inconsistent or unstable state."],
        "ACCESS_SURFACE_FLINGER": ["signature", "access SurfaceFlinger", "Allows application to use SurfaceFlinger low-level features."],
        "READ_FRAME_BUFFER": ["signature", "read frame buffer", "Allows application to read the content of the frame buffer."],
        "BRICK": ["signature", "permanently disable phone", "Allows the application to disable the entire phone permanently. This is very dangerous."],
        "REBOOT": ["signatureOrSystem", "force phone reboot", "Allows the application to force the phone to reboot."],
        "DEVICE_POWER": ["signature", "turn phone on or off", "Allows the application to turn the phone on or off."],
        "FACTORY_TEST": ["signature", "run in factory test mode", "Run as a low-level manufacturer test, allowing complete access to the phone hardware. Only available when a phone is running in manufacturer test mode."],
        "BROADCAST_PACKAGE_REMOVED": ["signature", "send package removed broadcast", "Allows an application to broadcast a notification that an application package has been removed. Malicious applications may use this to kill any other application running."],
        "BROADCAST_SMS": ["signature", "send SMS-received broadcast", "Allows an application to broadcast a notification that an SMS message has been received. Malicious applications may use this to forge incoming SMS messages."],
        "BROADCAST_WAP_PUSH": ["signature", "send WAP-PUSH-received broadcast", "Allows an application to broadcast a notification that a WAP-PUSH message has been received. Malicious applications may use this to forge MMS message receipt or to replace the content of any web page silently with malicious variants."],
        "MASTER_CLEAR": ["signatureOrSystem", "reset system to factory defaults", "Allows an application to completely reset the system to its factory settings, erasing all data, configuration and installed applications."],
        "CALL_PRIVILEGED": ["signatureOrSystem", "directly call any phone numbers", "Allows the application to call any phone number, including emergency numbers, without your intervention. Malicious applications may place unnecessary and illegal calls to emergency services."],
        "PERFORM_CDMA_PROVISIONING": ["signatureOrSystem", "directly start CDMA phone setup", "Allows the application to start CDMA provisioning. Malicious applications may start CDMA provisioning unnecessarily"],
        "CONTROL_LOCATION_UPDATES": ["signatureOrSystem", "control location update notifications", "Allows enabling/disabling location update notifications from the radio. Not for use by common applications."],
        "ACCESS_CHECKIN_PROPERTIES": ["signatureOrSystem", "access check-in properties", "Allows read/write access to properties uploaded by the check-in service. Not for use by common applications."],
        "PACKAGE_USAGE_STATS": ["signature", "update component usage statistics", "Allows the modification of collected component usage statistics. Not for use by common applications."],
        "BATTERY_STATS": ["normal", "modify battery statistics", "Allows the modification of collected battery statistics. Not for use by common applications."],
        "BACKUP": ["signatureOrSystem", "control system back up and restore", "Allows the application to control the system\'s back-up and restore mechanism. Not for use by common applications."],
        "BIND_APPWIDGET": ["signatureOrSystem", "choose widgets", "Allows the application to tell the system which widgets can be used by which application. With this permission, applications can give access to personal data to other applications. Not for use by common applications."],
        "CHANGE_BACKGROUND_DATA_SETTING": ["signature", "change background data usage setting", "Allows an application to change the background data usage setting."],
        "GLOBAL_SEARCH": ["signatureOrSystem", "", ""],
        "GLOBAL_SEARCH_CONTROL": ["signature", "", ""],
        "SET_WALLPAPER_COMPONENT": ["signatureOrSystem", "", ""],
        "ACCESS_CACHE_FILESYSTEM": ["signatureOrSystem", "access the cache file system", "Allows an application to read and write the cache file system."],
        "COPY_PROTECTED_DATA": ["signature", "Allows to invoke default container service to copy content. Not for use by common applications.", "Allows to invoke default container service to copy content. Not for use by common applications."],
        "C2D_MESSAGE": ["signature", "Allows cloud to device messaging", "Allows the application to receive push notifications."],
        "ADD_VOICEMAIL": ["dangerous", "add voicemails into the system", "Allows an application to add voicemails into the system."],
    },

    "MANIFEST_PERMISSION_GROUP":
        {

        "ACCOUNTS": "Permissions for direct access to the accounts managed by the Account Manager.",
        "COST_MONEY": "Used for permissions that can be used to make the user spend money without their direct involvement.",
        "DEVELOPMENT_TOOLS": "Group of permissions that are related to development features.",
        "HARDWARE_CONTROLS": "Used for permissions that provide direct access to the hardware on the device.",
        "LOCATION": "Used for permissions that allow access to the user's current location.",
        "MESSAGES": "Used for permissions that allow an application to send messages on behalf of the user or intercept messages being received by the user.",
        "NETWORK": "Used for permissions that provide access to networking services.",
        "PERSONAL_INFO": "Used for permissions that provide access to the user's private data, such as contacts, calendar events, e-mail messages, etc.",
        "PHONE_CALLS": "Used for permissions that are associated with accessing and modifyign telephony state: intercepting outgoing calls, reading and modifying the phone state.",
        "STORAGE": "Group of permissions that are related to SD card access.",
        "SYSTEM_TOOLS": "Group of permissions that are related to system APIs.",
    },
}
