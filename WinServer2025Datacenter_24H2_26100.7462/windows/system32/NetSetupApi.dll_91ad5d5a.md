# Binary Specification: NetSetupApi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NetSetupApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `91ad5d5a7037329b7711a30517d1731998aa919a2729f4d2a944d5ba819da1e4`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1021 | `NetSetupGetObjectProperties` | `0x1230` | 379 | UnwindData |  |
| 1023 | `NetSetupGetObjects` | `0x13C0` | 385 | UnwindData |  |
| 1014 | `NetSetupCommit` | `0x1550` | 63 | UnwindData |  |
| 1029 | `NetSetupSetObjectProperties` | `0x1630` | 201 | UnwindData |  |
| 1012 | `NetSetupClose` | `0x1790` | 78 | UnwindData |  |
| 1018 | `NetSetupFreeObjectProperties` | `0x1930` | 119 | UnwindData |  |
| 1019 | `NetSetupFreeObjects` | `0x1B90` | 119 | UnwindData |  |
| 1024 | `NetSetupInitialize` | `0x3B60` | 568 | UnwindData |  |
| 1017 | `NetSetupDeleteObject` | `0x5A70` | 109 | UnwindData |  |
| 1009 | `NetSetupGetFilterClassBottomDriver` | `0xEF20` | 280 | UnwindData |  |
| 1007 | `NetSetupGetFilterClassTopDriver` | `0xF040` | 280 | UnwindData |  |
| 1011 | `NetSetupResetFilterClassBottomDriver` | `0xF160` | 140 | UnwindData |  |
| 1010 | `NetSetupResetFilterClassTopDriver` | `0xF200` | 140 | UnwindData |  |
| 1008 | `NetSetupSetFilterClassBottomDriver` | `0xF2A0` | 187 | UnwindData |  |
| 1006 | `NetSetupSetFilterClassTopDriver` | `0xF370` | 187 | UnwindData |  |
| 1013 | `NetSetupCloseObjectQuery` | `0x14C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `NetSetupCreateObject` | `0x14C20` | 183 | UnwindData |  |
| 1016 | `NetSetupCreateObjectQuery` | `0x14CE0` | 270 | UnwindData |  |
| 1020 | `NetSetupFreeSerializedFilter` | `0x14E00` | 42 | UnwindData |  |
| 1022 | `NetSetupGetObjectPropertyKeys` | `0x14E30` | 212 | UnwindData |  |
| 1025 | `NetSetupOpenAdvancedPropertyKey` | `0x14F10` | 146 | UnwindData |  |
| 1026 | `NetSetupRollback` | `0x14FB0` | 48 | UnwindData |  |
| 1027 | `NetSetupSerializeFilter` | `0x14FF0` | 147 | UnwindData |  |
| 1028 | `NetSetupSetKeywordValue` | `0x15090` | 164 | UnwindData |  |
| 1030 | `NetSetupSynchronizeDevices` | `0x15140` | 66 | UnwindData |  |
| 1031 | `NetSetupValidateTransaction` | `0x15190` | 63 | UnwindData |  |
| 1032 | `OnMachineUILanguageInit` | `0x15650` | 205 | UnwindData |  |
| 1033 | `OnMachineUILanguageSwitch` | `0x15730` | 254 | UnwindData |  |
