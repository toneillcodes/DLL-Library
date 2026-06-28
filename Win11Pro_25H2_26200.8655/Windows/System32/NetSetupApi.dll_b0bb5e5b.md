# Binary Specification: NetSetupApi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\NetSetupApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b0bb5e5b129f4836eb9e9179754c7517b2b1d0ee377fa1f8f89172f9a6865309`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1021 | `NetSetupGetObjectProperties` | `0x1130` | 379 | UnwindData |  |
| 1023 | `NetSetupGetObjects` | `0x12C0` | 385 | UnwindData |  |
| 1014 | `NetSetupCommit` | `0x1450` | 63 | UnwindData |  |
| 1029 | `NetSetupSetObjectProperties` | `0x1530` | 201 | UnwindData |  |
| 1012 | `NetSetupClose` | `0x1690` | 78 | UnwindData |  |
| 1018 | `NetSetupFreeObjectProperties` | `0x1830` | 119 | UnwindData |  |
| 1019 | `NetSetupFreeObjects` | `0x1A90` | 119 | UnwindData |  |
| 1024 | `NetSetupInitialize` | `0x39E0` | 568 | UnwindData |  |
| 1017 | `NetSetupDeleteObject` | `0x5880` | 109 | UnwindData |  |
| 1009 | `NetSetupGetFilterClassBottomDriver` | `0xAA10` | 248 | UnwindData |  |
| 1007 | `NetSetupGetFilterClassTopDriver` | `0xAB10` | 248 | UnwindData |  |
| 1011 | `NetSetupResetFilterClassBottomDriver` | `0xAC10` | 117 | UnwindData |  |
| 1010 | `NetSetupResetFilterClassTopDriver` | `0xAC90` | 117 | UnwindData |  |
| 1008 | `NetSetupSetFilterClassBottomDriver` | `0xAD10` | 158 | UnwindData |  |
| 1006 | `NetSetupSetFilterClassTopDriver` | `0xADC0` | 158 | UnwindData |  |
| 1013 | `NetSetupCloseObjectQuery` | `0xFDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `NetSetupCreateObject` | `0xFDB0` | 183 | UnwindData |  |
| 1016 | `NetSetupCreateObjectQuery` | `0xFE70` | 270 | UnwindData |  |
| 1020 | `NetSetupFreeSerializedFilter` | `0xFF90` | 42 | UnwindData |  |
| 1022 | `NetSetupGetObjectPropertyKeys` | `0xFFC0` | 212 | UnwindData |  |
| 1025 | `NetSetupOpenAdvancedPropertyKey` | `0x100A0` | 146 | UnwindData |  |
| 1026 | `NetSetupRollback` | `0x10140` | 48 | UnwindData |  |
| 1027 | `NetSetupSerializeFilter` | `0x10180` | 147 | UnwindData |  |
| 1028 | `NetSetupSetKeywordValue` | `0x10220` | 164 | UnwindData |  |
| 1030 | `NetSetupSynchronizeDevices` | `0x102D0` | 66 | UnwindData |  |
| 1031 | `NetSetupValidateTransaction` | `0x10320` | 63 | UnwindData |  |
| 1032 | `OnMachineUILanguageInit` | `0x107E0` | 205 | UnwindData |  |
| 1033 | `OnMachineUILanguageSwitch` | `0x108C0` | 254 | UnwindData |  |
