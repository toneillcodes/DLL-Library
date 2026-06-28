# Binary Specification: gpprefcl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\gpprefcl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `92f0e9ca04a970e39f37438277bda55d83bd3f226b5c6ca03b1b45ba81fb4cf5`
* **Total Exported Functions:** 69

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x370F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x37110` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x371A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x371B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GenerateGroupPolicyApplications` | `0x371C0` | 184 | UnwindData |  |
| 8 | `GenerateGroupPolicyDataSources` | `0x37280` | 184 | UnwindData |  |
| 9 | `GenerateGroupPolicyDevices` | `0x37340` | 184 | UnwindData |  |
| 10 | `GenerateGroupPolicyDrives` | `0x37400` | 184 | UnwindData |  |
| 11 | `GenerateGroupPolicyEnviron` | `0x374C0` | 184 | UnwindData |  |
| 12 | `GenerateGroupPolicyFiles` | `0x37580` | 184 | UnwindData |  |
| 13 | `GenerateGroupPolicyFolderOptions` | `0x37640` | 184 | UnwindData |  |
| 14 | `GenerateGroupPolicyFolders` | `0x37700` | 184 | UnwindData |  |
| 15 | `GenerateGroupPolicyIniFile` | `0x377C0` | 184 | UnwindData |  |
| 16 | `GenerateGroupPolicyInternet` | `0x37880` | 184 | UnwindData |  |
| 17 | `GenerateGroupPolicyLocUsAndGroups` | `0x37940` | 184 | UnwindData |  |
| 18 | `GenerateGroupPolicyNetShares` | `0x37A00` | 184 | UnwindData |  |
| 19 | `GenerateGroupPolicyNetworkOptions` | `0x37AC0` | 184 | UnwindData |  |
| 20 | `GenerateGroupPolicyPowerOptions` | `0x37B80` | 184 | UnwindData |  |
| 21 | `GenerateGroupPolicyPrinters` | `0x37C40` | 184 | UnwindData |  |
| 22 | `GenerateGroupPolicyRegionOptions` | `0x37D00` | 184 | UnwindData |  |
| 23 | `GenerateGroupPolicyRegistry` | `0x37DC0` | 184 | UnwindData |  |
| 24 | `GenerateGroupPolicySchedTasks` | `0x37E80` | 184 | UnwindData |  |
| 25 | `GenerateGroupPolicyServices` | `0x37F40` | 184 | UnwindData |  |
| 26 | `GenerateGroupPolicyShortcuts` | `0x38000` | 184 | UnwindData |  |
| 27 | `GenerateGroupPolicyStartMenu` | `0x380C0` | 184 | UnwindData |  |
| 28 | `ProcessGroupPolicyApplications` | `0x38180` | 209 | UnwindData |  |
| 29 | `ProcessGroupPolicyDataSources` | `0x38260` | 209 | UnwindData |  |
| 30 | `ProcessGroupPolicyDevices` | `0x38340` | 209 | UnwindData |  |
| 31 | `ProcessGroupPolicyDrives` | `0x38420` | 209 | UnwindData |  |
| 32 | `ProcessGroupPolicyEnviron` | `0x38500` | 209 | UnwindData |  |
| 33 | `ProcessGroupPolicyExApplications` | `0x385E0` | 225 | UnwindData |  |
| 34 | `ProcessGroupPolicyExDataSources` | `0x386D0` | 225 | UnwindData |  |
| 35 | `ProcessGroupPolicyExDevices` | `0x387C0` | 225 | UnwindData |  |
| 36 | `ProcessGroupPolicyExDrives` | `0x388B0` | 225 | UnwindData |  |
| 37 | `ProcessGroupPolicyExEnviron` | `0x389A0` | 225 | UnwindData |  |
| 38 | `ProcessGroupPolicyExFiles` | `0x38A90` | 225 | UnwindData |  |
| 39 | `ProcessGroupPolicyExFolderOptions` | `0x38B80` | 225 | UnwindData |  |
| 40 | `ProcessGroupPolicyExFolders` | `0x38C70` | 225 | UnwindData |  |
| 41 | `ProcessGroupPolicyExIniFile` | `0x38D60` | 225 | UnwindData |  |
| 42 | `ProcessGroupPolicyExInternet` | `0x38E50` | 225 | UnwindData |  |
| 43 | `ProcessGroupPolicyExLocUsAndGroups` | `0x38F40` | 225 | UnwindData |  |
| 44 | `ProcessGroupPolicyExNetShares` | `0x39030` | 225 | UnwindData |  |
| 45 | `ProcessGroupPolicyExNetworkOptions` | `0x39120` | 225 | UnwindData |  |
| 46 | `ProcessGroupPolicyExPowerOptions` | `0x39210` | 225 | UnwindData |  |
| 47 | `ProcessGroupPolicyExPrinters` | `0x39300` | 225 | UnwindData |  |
| 48 | `ProcessGroupPolicyExRegionOptions` | `0x393F0` | 225 | UnwindData |  |
| 49 | `ProcessGroupPolicyExRegistry` | `0x394E0` | 225 | UnwindData |  |
| 50 | `ProcessGroupPolicyExSchedTasks` | `0x395D0` | 225 | UnwindData |  |
| 51 | `ProcessGroupPolicyExServices` | `0x396C0` | 225 | UnwindData |  |
| 52 | `ProcessGroupPolicyExShortcuts` | `0x397B0` | 225 | UnwindData |  |
| 53 | `ProcessGroupPolicyExStartMenu` | `0x398A0` | 225 | UnwindData |  |
| 54 | `ProcessGroupPolicyFiles` | `0x39990` | 209 | UnwindData |  |
| 55 | `ProcessGroupPolicyFolderOptions` | `0x39A70` | 209 | UnwindData |  |
| 56 | `ProcessGroupPolicyFolders` | `0x39B50` | 209 | UnwindData |  |
| 57 | `ProcessGroupPolicyIniFile` | `0x39C30` | 209 | UnwindData |  |
| 58 | `ProcessGroupPolicyInternet` | `0x39D10` | 209 | UnwindData |  |
| 59 | `ProcessGroupPolicyLocUsAndGroups` | `0x39DF0` | 209 | UnwindData |  |
| 60 | `ProcessGroupPolicyNetShares` | `0x39ED0` | 209 | UnwindData |  |
| 61 | `ProcessGroupPolicyNetworkOptions` | `0x39FB0` | 209 | UnwindData |  |
| 62 | `ProcessGroupPolicyPowerOptions` | `0x3A090` | 209 | UnwindData |  |
| 63 | `ProcessGroupPolicyPrinters` | `0x3A170` | 209 | UnwindData |  |
| 64 | `ProcessGroupPolicyRegionOptions` | `0x3A250` | 209 | UnwindData |  |
| 65 | `ProcessGroupPolicyRegistry` | `0x3A330` | 209 | UnwindData |  |
| 66 | `ProcessGroupPolicySchedTasks` | `0x3A410` | 209 | UnwindData |  |
| 67 | `ProcessGroupPolicyServices` | `0x3A4F0` | 209 | UnwindData |  |
| 68 | `ProcessGroupPolicyShortcuts` | `0x3A5D0` | 209 | UnwindData |  |
| 69 | `ProcessGroupPolicyStartMenu` | `0x3A6B0` | 209 | UnwindData |  |
| 1 | `ProcessGroupPolicyMitigationOptions` | `0x49460` | 455 | UnwindData |  |
| 2 | `ProcessGroupPolicyProcessMitigationOptions` | `0x4A1F0` | 685 | UnwindData |  |
