# Binary Specification: tetheringclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tetheringclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ac90bf364e0d39daed047833c10ccc2887abea57e38debf0c5c490c9508cff0a`
* **Total Exported Functions:** 50

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `IsTetheringGPAllowed` | `0x4E80` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `TetheringGetSimIccidForInterfaceGuid` | `0x54E0` | 29 | UnwindData |  |
| 3 | `TetheringSettingsFreeAutoLoadSettings` | `0x5510` | 175 | UnwindData |  |
| 4 | `TetheringSettingsFreeSettingValue` | `0x55D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `TetheringSettingsGenerateDefaultPrivateConnectionSettings` | `0x55E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `TetheringSettingsGenerateDefaultPublicConnectionSettings` | `0x55F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `TetheringSettingsLoadAutoLoadSettings` | `0x5600` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `TetheringAuthorize` | `0x5690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `TetheringDeinitApi` | `0x56B0` | 56 | UnwindData |  |
| 10 | `TetheringFreeMemory` | `0x56F0` | 27 | UnwindData |  |
| 11 | `TetheringFreePeerList` | `0x56F0` | 27 | UnwindData |  |
| 12 | `TetheringGetClientCount` | `0x5720` | 119 | UnwindData |  |
| 13 | `TetheringGetDefaultInterface` | `0x57A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `TetheringGetErrorString` | `0x57B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `TetheringGetIsPeerlessTimeoutEnabled` | `0x57D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `TetheringGetLastApiError` | `0x57F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `TetheringGetMaxClientCount` | `0x5800` | 56 | UnwindData |  |
| 18 | `TetheringGetPeerList` | `0x5840` | 53 | UnwindData |  |
| 19 | `TetheringGetPreferredInterface` | `0x5880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `TetheringGetPrivateConnectionSettings` | `0x58A0` | 302 | UnwindData |  |
| 21 | `TetheringGetPublicConnectionSettings` | `0x59E0` | 233 | UnwindData |  |
| 22 | `TetheringGetSharedInterfaceIndices` | `0x5AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `TetheringGetSharingState` | `0x5AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `TetheringInitApi` | `0x5AF0` | 58 | UnwindData |  |
| 25 | `TetheringIsAllowed` | `0x5B30` | 32 | UnwindData |  |
| 26 | `TetheringIsAuthSupported` | `0x5B60` | 126 | UnwindData |  |
| 27 | `TetheringIsFrequencySupported` | `0x5BF0` | 126 | UnwindData |  |
| 28 | `TetheringRegisterNotification` | `0x5C80` | 229 | UnwindData |  |
| 29 | `TetheringSetIsPeerlessTimeoutEnabled` | `0x5D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `TetheringSetPreferredInterface` | `0x5D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `TetheringSetPrivateConnectionSettings` | `0x5DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `TetheringSetPrivateConnectionSettingsAsync` | `0x5DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `TetheringSetPublicConnectionSettings` | `0x5DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `TetheringSetSharingState` | `0x5E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `TetheringSetSharingStateAsync` | `0x5E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `TetheringSettingsGetSettingValueGlobal` | `0x5E10` | 230 | UnwindData |  |
| 37 | `TetheringSettingsGetSettingValueWithGuid` | `0x5F00` | 299 | UnwindData |  |
| 38 | `TetheringSettingsGetSettingValueWithIccid` | `0x6040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `TetheringSettingsResetSettingToDefaultGlobal` | `0x6050` | 230 | UnwindData |  |
| 40 | `TetheringSettingsResetSettingToDefaultWithGuid` | `0x6140` | 365 | UnwindData |  |
| 41 | `TetheringSettingsResetSettingToDefaultWithIccid` | `0x62C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `TetheringSettingsSaveSettingGlobal` | `0x62D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `TetheringSettingsSaveSettingWithGuid` | `0x62E0` | 369 | UnwindData |  |
| 44 | `TetheringSettingsSaveSettingWithIccid` | `0x6460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `TetheringStartSharing` | `0x6470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `TetheringStartSharingAsync` | `0x6490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `TetheringStartSharingWithSessionSettingsAsync` | `0x64B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `TetheringStopSharing` | `0x64C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `TetheringStopSharingAsync` | `0x64D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `TetheringUnregisterNotification` | `0x64E0` | 312 | UnwindData |  |
