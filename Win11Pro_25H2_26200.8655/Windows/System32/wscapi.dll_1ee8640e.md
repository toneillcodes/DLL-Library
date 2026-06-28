# Binary Specification: wscapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wscapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1ee8640e9ec36fd4be6304f38a034f86d2f958ff18022ace20d5bd89962a66de`
* **Total Exported Functions:** 41

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `WscGetSecurityProviderHealth` | `0x1ED0` | 446 | UnwindData |  |
| 36 | `wscRegisterSecurityProduct` | `0x2A40` | 122 | UnwindData |  |
| 39 | `wscUnregisterSecurityProduct` | `0x2AC0` | 104 | UnwindData |  |
| 33 | `wscPing` | `0x2CD0` | 83 | UnwindData |  |
| 40 | `wscUpdateProductStatus` | `0x3200` | 138 | UnwindData |  |
| 41 | `wscUpdateProductSubStatus` | `0x3290` | 121 | UnwindData |  |
| 23 | `wscGeneralSecurityGetStatus` | `0x3310` | 142 | UnwindData |  |
| 19 | `wscAntiVirusGetStatus` | `0x43E0` | 110 | UnwindData |  |
| 22 | `wscFirewallGetStatus` | `0x45C0` | 110 | UnwindData |  |
| 34 | `wscProductInfoFree` | `0x5AE0` | 25 | UnwindData |  |
| 6 | `DllGetClassObject` | `0x5FE0` | 163 | UnwindData |  |
| 24 | `wscGetAlertStatus` | `0x6820` | 123 | UnwindData |  |
| 16 | `WscUnRegisterChanges` | `0x7330` | 564 | UnwindData |  |
| 38 | `wscUnRegisterChangeNotification` | `0x75E0` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllCanUnloadNow` | `0x7B80` | 82 | UnwindData |  |
| 14 | `WscRegisterForChanges` | `0x8070` | 884 | UnwindData |  |
| 15 | `WscRegisterForUserNotifications` | `0x8F50` | 224 | UnwindData |  |
| 35 | `wscRegisterChangeNotification` | `0x98C0` | 11,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `wscAntiSpywareGetStatus` | `0xC750` | 110 | UnwindData |  |
| 18 | `wscAntiVirusExpiredBeyondThreshold` | `0xC7D0` | 110 | UnwindData |  |
| 20 | `wscAutoUpdatesEnableScheduledMode` | `0xC990` | 85 | UnwindData |  |
| 21 | `wscAutoUpdatesGetStatus` | `0xC9F0` | 93 | UnwindData |  |
| 25 | `wscIcfEnable` | `0xCA60` | 85 | UnwindData |  |
| 26 | `wscIeSettingsFix` | `0xCAC0` | 27 | UnwindData |  |
| 27 | `wscInitiateOfflineCleaning` | `0xCAF0` | 286 | UnwindData |  |
| 28 | `wscIsDefenderAntivirusSupported` | `0xCC20` | 106 | UnwindData |  |
| 29 | `wscLuaSettingsFix` | `0xCC90` | 93 | UnwindData |  |
| 30 | `wscMakeDefaultProductRequest` | `0xCD00` | 104 | UnwindData |  |
| 31 | `wscNotifyUserForNearExpiration` | `0xCD70` | 104 | UnwindData |  |
| 32 | `wscOverrideComponentStatus` | `0xCDE0` | 106 | UnwindData |  |
| 37 | `wscSetDefaultProduct` | `0xCE50` | 121 | UnwindData |  |
| 11 | `WscGetAntiMalwareUri` | `0xF8C0` | 13,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WscQueryAntiMalwareUri` | `0xF8C0` | 13,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `wscLaunchAdminMakeDefaultUI` | `0x12C30` | 74 | UnwindData |  |
| 2 | `wscShowAMSCN` | `0x12DD0` | 99,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `IID_IWscProduct` | `0x2B1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `IID_IWSCProductList` | `0x2B1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `IID_IWSCDefaultProduct` | `0x2B1F0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `LIBID_wscAPILib` | `0x2B248` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CLSID_WSCDefaultProduct` | `0x2C588` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CLSID_WSCProductList` | `0x2C598` | 0 | Indeterminate |  |
