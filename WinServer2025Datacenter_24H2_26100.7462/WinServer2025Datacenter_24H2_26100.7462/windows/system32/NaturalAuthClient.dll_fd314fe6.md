# Binary Specification: NaturalAuthClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NaturalAuthClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd314fe67fc22b944552dadda3d0abea16b919bcad7555b649de6c949e03e9fd`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `NaDeviceUnlockStart` | `0x2B80` | 34 | UnwindData |  |
| 5 | `NaDeviceUnlockStop` | `0x2BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NaDynamicLockForceEvaluate` | `0x2BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NaDynamicLockShouldIgnoreDisplayRequestActivity` | `0x2BD0` | 30 | UnwindData |  |
| 8 | `NaDynamicLockShouldIgnoreUserActivity` | `0x2C00` | 30 | UnwindData |  |
| 9 | `NaDynamicLockShouldSkipGracePeriod` | `0x2C30` | 30 | UnwindData |  |
| 10 | `NaDynamicLockStart` | `0x2C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `NaDynamicLockStop` | `0x2C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `NaRuleQuery` | `0x2C80` | 34 | UnwindData |  |
| 13 | `NaRuleRegister` | `0x2CB0` | 38 | UnwindData |  |
| 14 | `NaRuleUnregister` | `0x2CE0` | 30 | UnwindData |  |
| 15 | `NaRuleValidate` | `0x2D10` | 30 | UnwindData |  |
| 1 | `CdfPluginRegisterDevice` | `0x3010` | 40 | UnwindData |  |
| 2 | `CdfPluginUnregisterDevice` | `0x3040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CdfPluginUpdatePresenceState` | `0x3050` | 40 | UnwindData |  |
