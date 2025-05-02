/* Custom 'about:config' settings. Disable unneccesary animations, stop countdown timers while installing extensions, 
remove built-in add-ons and, optionally, stop preloading web pages (on slow internet connections). */

user_pref("browser.download.animateNotifications", false);
user_pref("security.dialog_enable_delay", 0);
// user_pref("network.prefetch-next", false); // (Only for slow internet connections)
user_pref("browser.newtabpage.activity-stream.feeds.telemetry", false);
user_pref("browser.newtabpage.activity-stream.telemetry", false);
user_pref("browser.ping-centre.telemetry", false);
user_pref("toolkit.telemetry.archive.enabled", false);
user_pref("toolkit.telemetry.enabled", false);
user_pref("toolkit.telemetry.firstShutdownPing.enabled", false);
user_pref("toolkit.telemetry.hybridContent.enabled", false);
user_pref("toolkit.telemetry.newProfilePing.enabled", false);
user_pref("toolkit.telemetry.reportingpolicy.firstRun", false);
user_pref("toolkit.telemetry.shutdownPingSender.enabled", false);
user_pref("toolkit.telemetry.unified", false);
user_pref("toolkit.telemetry.updatePing.enabled", false);
user_pref("reader.parse-on-load.enabled", false);
user_pref("reader.parse-on-load.force-enabled", false);
user_pref("browser.pocket.enabled", false);
user_pref("loop.enabled", false);
