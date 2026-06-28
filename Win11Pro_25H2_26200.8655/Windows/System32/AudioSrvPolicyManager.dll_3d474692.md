# Binary Specification: AudioSrvPolicyManager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AudioSrvPolicyManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3d4746920b67dc23afe66cf8d2ccb2968355386310784ee5ae20e16b26f4d1b9`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `TS_RegisterAudioProtocolNotification` | `0x4EB0` | 54 | UnwindData |  |
| 26 | `TS_SessionGetAudioProtocol` | `0x4F90` | 134 | UnwindData |  |
| 16 | `PbmReportHostedAppStateChange` | `0x162C0` | 133 | UnwindData |  |
| 6 | `PbmGetSoundLevel` | `0x19300` | 254 | UnwindData |  |
| 14 | `PbmReportAppInteractivityChange` | `0x194A0` | 125 | UnwindData |  |
| 11 | `PbmRegisterAppManagerNotification` | `0x1A200` | 99 | UnwindData |  |
| 3 | `ActivatePolicyManager` | `0x2B210` | 141 | UnwindData |  |
| 1 | `HHOSTEDAPPMANAGERCONTEXTRundown` | `0x3AC40` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PbmAllowMediaPlaybackForApp` | `0x3B070` | 271 | UnwindData |  |
| 5 | `PbmCastingAppStateChanged` | `0x3B190` | 339 | UnwindData |  |
| 7 | `PbmIsPlaying` | `0x3B2F0` | 213 | UnwindData |  |
| 8 | `PbmLaunchBackgroundTask` | `0x3B3D0` | 120 | UnwindData |  |
| 9 | `PbmPlayToStreamStateChanged` | `0x3B450` | 253 | UnwindData |  |
| 10 | `PbmRegisterAppClosureNotification` | `0x3B560` | 99 | UnwindData |  |
| 12 | `PbmRegisterPlaybackManagerNotifications` | `0x3B5D0` | 130 | UnwindData |  |
| 13 | `PbmReportAppClosing` | `0x3B660` | 100 | UnwindData |  |
| 15 | `PbmReportApplicationState` | `0x3B6D0` | 304 | UnwindData |  |
| 17 | `PbmReportHostedAppStateChange_2` | `0x3B810` | 80 | UnwindData |  |
| 18 | `PbmSetScreenReaderState` | `0x3B870` | 229 | UnwindData |  |
| 19 | `PbmSetSmtcSubscriptionState` | `0x3B960` | 324 | UnwindData |  |
| 20 | `PbmSwitchSoftNonInteractiveAppsToHardNonInteractive` | `0x3BAB0` | 75 | UnwindData |  |
| 21 | `PbmUnregisterAppClosureNotification` | `0x3BB10` | 157 | UnwindData |  |
| 22 | `PbmUnregisterAppManagerNotification` | `0x3BBC0` | 90 | UnwindData |  |
| 23 | `PbmUnregisterPlaybackManagerNotifications` | `0x3BC20` | 240 | UnwindData |  |
| 2 | `TS_SessionChanged` | `0x3EB20` | 243 | UnwindData |  |
| 24 | `TS_AudioProtocolNotifyRundown` | `0x41310` | 44 | UnwindData |  |
| 27 | `TS_UnregisterAudioProtocolNotification` | `0x41350` | 113 | UnwindData |  |
