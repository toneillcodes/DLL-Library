# Binary Specification: gpprefcl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gpprefcl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `40916ac7e1f007a3df8bd48e3a6474b49cbb5649ce5b46a59745f156839c5c4d`
* **Total Exported Functions:** 69

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x38C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x38CA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x38D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x38D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GenerateGroupPolicyApplications` | `0x38D50` | 184 | UnwindData |  |
| 8 | `GenerateGroupPolicyDataSources` | `0x38E10` | 184 | UnwindData |  |
| 9 | `GenerateGroupPolicyDevices` | `0x38ED0` | 184 | UnwindData |  |
| 10 | `GenerateGroupPolicyDrives` | `0x38F90` | 184 | UnwindData |  |
| 11 | `GenerateGroupPolicyEnviron` | `0x39050` | 184 | UnwindData |  |
| 12 | `GenerateGroupPolicyFiles` | `0x39110` | 184 | UnwindData |  |
| 13 | `GenerateGroupPolicyFolderOptions` | `0x391D0` | 184 | UnwindData |  |
| 14 | `GenerateGroupPolicyFolders` | `0x39290` | 184 | UnwindData |  |
| 15 | `GenerateGroupPolicyIniFile` | `0x39350` | 184 | UnwindData |  |
| 16 | `GenerateGroupPolicyInternet` | `0x39410` | 184 | UnwindData |  |
| 17 | `GenerateGroupPolicyLocUsAndGroups` | `0x394D0` | 184 | UnwindData |  |
| 18 | `GenerateGroupPolicyNetShares` | `0x39590` | 184 | UnwindData |  |
| 19 | `GenerateGroupPolicyNetworkOptions` | `0x39650` | 184 | UnwindData |  |
| 20 | `GenerateGroupPolicyPowerOptions` | `0x39710` | 184 | UnwindData |  |
| 21 | `GenerateGroupPolicyPrinters` | `0x397D0` | 184 | UnwindData |  |
| 22 | `GenerateGroupPolicyRegionOptions` | `0x39890` | 184 | UnwindData |  |
| 23 | `GenerateGroupPolicyRegistry` | `0x39950` | 184 | UnwindData |  |
| 24 | `GenerateGroupPolicySchedTasks` | `0x39A10` | 184 | UnwindData |  |
| 25 | `GenerateGroupPolicyServices` | `0x39AD0` | 184 | UnwindData |  |
| 26 | `GenerateGroupPolicyShortcuts` | `0x39B90` | 184 | UnwindData |  |
| 27 | `GenerateGroupPolicyStartMenu` | `0x39C50` | 184 | UnwindData |  |
| 28 | `ProcessGroupPolicyApplications` | `0x39D10` | 209 | UnwindData |  |
| 29 | `ProcessGroupPolicyDataSources` | `0x39DF0` | 209 | UnwindData |  |
| 30 | `ProcessGroupPolicyDevices` | `0x39ED0` | 209 | UnwindData |  |
| 31 | `ProcessGroupPolicyDrives` | `0x39FB0` | 209 | UnwindData |  |
| 32 | `ProcessGroupPolicyEnviron` | `0x3A090` | 209 | UnwindData |  |
| 33 | `ProcessGroupPolicyExApplications` | `0x3A170` | 225 | UnwindData |  |
| 34 | `ProcessGroupPolicyExDataSources` | `0x3A260` | 225 | UnwindData |  |
| 35 | `ProcessGroupPolicyExDevices` | `0x3A350` | 225 | UnwindData |  |
| 36 | `ProcessGroupPolicyExDrives` | `0x3A440` | 225 | UnwindData |  |
| 37 | `ProcessGroupPolicyExEnviron` | `0x3A530` | 225 | UnwindData |  |
| 38 | `ProcessGroupPolicyExFiles` | `0x3A620` | 225 | UnwindData |  |
| 39 | `ProcessGroupPolicyExFolderOptions` | `0x3A710` | 225 | UnwindData |  |
| 40 | `ProcessGroupPolicyExFolders` | `0x3A800` | 225 | UnwindData |  |
| 41 | `ProcessGroupPolicyExIniFile` | `0x3A8F0` | 225 | UnwindData |  |
| 42 | `ProcessGroupPolicyExInternet` | `0x3A9E0` | 225 | UnwindData |  |
| 43 | `ProcessGroupPolicyExLocUsAndGroups` | `0x3AAD0` | 225 | UnwindData |  |
| 44 | `ProcessGroupPolicyExNetShares` | `0x3ABC0` | 225 | UnwindData |  |
| 45 | `ProcessGroupPolicyExNetworkOptions` | `0x3ACB0` | 225 | UnwindData |  |
| 46 | `ProcessGroupPolicyExPowerOptions` | `0x3ADA0` | 225 | UnwindData |  |
| 47 | `ProcessGroupPolicyExPrinters` | `0x3AE90` | 225 | UnwindData |  |
| 48 | `ProcessGroupPolicyExRegionOptions` | `0x3AF80` | 225 | UnwindData |  |
| 49 | `ProcessGroupPolicyExRegistry` | `0x3B070` | 225 | UnwindData |  |
| 50 | `ProcessGroupPolicyExSchedTasks` | `0x3B160` | 225 | UnwindData |  |
| 51 | `ProcessGroupPolicyExServices` | `0x3B250` | 225 | UnwindData |  |
| 52 | `ProcessGroupPolicyExShortcuts` | `0x3B340` | 225 | UnwindData |  |
| 53 | `ProcessGroupPolicyExStartMenu` | `0x3B430` | 225 | UnwindData |  |
| 54 | `ProcessGroupPolicyFiles` | `0x3B520` | 209 | UnwindData |  |
| 55 | `ProcessGroupPolicyFolderOptions` | `0x3B600` | 209 | UnwindData |  |
| 56 | `ProcessGroupPolicyFolders` | `0x3B6E0` | 209 | UnwindData |  |
| 57 | `ProcessGroupPolicyIniFile` | `0x3B7C0` | 209 | UnwindData |  |
| 58 | `ProcessGroupPolicyInternet` | `0x3B8A0` | 209 | UnwindData |  |
| 59 | `ProcessGroupPolicyLocUsAndGroups` | `0x3B980` | 209 | UnwindData |  |
| 60 | `ProcessGroupPolicyNetShares` | `0x3BA60` | 209 | UnwindData |  |
| 61 | `ProcessGroupPolicyNetworkOptions` | `0x3BB40` | 209 | UnwindData |  |
| 62 | `ProcessGroupPolicyPowerOptions` | `0x3BC20` | 209 | UnwindData |  |
| 63 | `ProcessGroupPolicyPrinters` | `0x3BD00` | 209 | UnwindData |  |
| 64 | `ProcessGroupPolicyRegionOptions` | `0x3BDE0` | 209 | UnwindData |  |
| 65 | `ProcessGroupPolicyRegistry` | `0x3BEC0` | 209 | UnwindData |  |
| 66 | `ProcessGroupPolicySchedTasks` | `0x3BFA0` | 209 | UnwindData |  |
| 67 | `ProcessGroupPolicyServices` | `0x3C080` | 209 | UnwindData |  |
| 68 | `ProcessGroupPolicyShortcuts` | `0x3C160` | 209 | UnwindData |  |
| 69 | `ProcessGroupPolicyStartMenu` | `0x3C240` | 209 | UnwindData |  |
| 1 | `ProcessGroupPolicyMitigationOptions` | `0x4AFF0` | 455 | UnwindData |  |
| 2 | `ProcessGroupPolicyProcessMitigationOptions` | `0x4B7F0` | 685 | UnwindData |  |
