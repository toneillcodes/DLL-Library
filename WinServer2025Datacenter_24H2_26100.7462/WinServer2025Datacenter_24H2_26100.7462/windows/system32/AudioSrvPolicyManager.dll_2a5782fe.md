# Binary Specification: AudioSrvPolicyManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AudioSrvPolicyManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2a5782fe61c9f37a8137750dd3d3ccd7a249185122056c83443f26bb28900448`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `TS_RegisterAudioProtocolNotification` | `0x70B0` | 54 | UnwindData |  |
| 26 | `TS_SessionGetAudioProtocol` | `0x7190` | 134 | UnwindData |  |
| 16 | `PbmReportHostedAppStateChange` | `0x160A0` | 133 | UnwindData |  |
| 6 | `PbmGetSoundLevel` | `0x191D0` | 254 | UnwindData |  |
| 14 | `PbmReportAppInteractivityChange` | `0x19370` | 125 | UnwindData |  |
| 11 | `PbmRegisterAppManagerNotification` | `0x1A0D0` | 99 | UnwindData |  |
| 3 | `ActivatePolicyManager` | `0x2C890` | 141 | UnwindData |  |
| 1 | `HHOSTEDAPPMANAGERCONTEXTRundown` | `0x3C4D0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PbmAllowMediaPlaybackForApp` | `0x3C900` | 271 | UnwindData |  |
| 5 | `PbmCastingAppStateChanged` | `0x3CA20` | 339 | UnwindData |  |
| 7 | `PbmIsPlaying` | `0x3CB80` | 213 | UnwindData |  |
| 8 | `PbmLaunchBackgroundTask` | `0x3CC60` | 120 | UnwindData |  |
| 9 | `PbmPlayToStreamStateChanged` | `0x3CCE0` | 253 | UnwindData |  |
| 10 | `PbmRegisterAppClosureNotification` | `0x3CDF0` | 99 | UnwindData |  |
| 12 | `PbmRegisterPlaybackManagerNotifications` | `0x3CE60` | 130 | UnwindData |  |
| 13 | `PbmReportAppClosing` | `0x3CEF0` | 100 | UnwindData |  |
| 15 | `PbmReportApplicationState` | `0x3CF60` | 304 | UnwindData |  |
| 17 | `PbmReportHostedAppStateChange_2` | `0x3D0A0` | 80 | UnwindData |  |
| 18 | `PbmSetScreenReaderState` | `0x3D100` | 229 | UnwindData |  |
| 19 | `PbmSetSmtcSubscriptionState` | `0x3D1F0` | 324 | UnwindData |  |
| 20 | `PbmSwitchSoftNonInteractiveAppsToHardNonInteractive` | `0x3D340` | 75 | UnwindData |  |
| 21 | `PbmUnregisterAppClosureNotification` | `0x3D3A0` | 157 | UnwindData |  |
| 22 | `PbmUnregisterAppManagerNotification` | `0x3D450` | 90 | UnwindData |  |
| 23 | `PbmUnregisterPlaybackManagerNotifications` | `0x3D4B0` | 240 | UnwindData |  |
| 2 | `TS_SessionChanged` | `0x403B0` | 243 | UnwindData |  |
| 24 | `TS_AudioProtocolNotifyRundown` | `0x42BA0` | 44 | UnwindData |  |
| 27 | `TS_UnregisterAudioProtocolNotification` | `0x42BE0` | 113 | UnwindData |  |
