# Binary Specification: mssecuser.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mssecuser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9804d6e8d277dee6e40237f1e5f5234c543856249a90773480ad924dedaa6c3f`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `SecRegisterConsumer` | `0x27A0` | 322 | UnwindData |  |
| 24 | `SecUninitializeDriver` | `0x28F0` | 81 | UnwindData |  |
| 25 | `SecUnregisterConsumer` | `0x2950` | 271 | UnwindData |  |
| 3 | `SecCreateSessionFilter` | `0x32A0` | 145 | UnwindData |  |
| 4 | `SecDeleteSessionFilter` | `0x3340` | 69 | UnwindData |  |
| 5 | `SecGetCiInformation` | `0x3390` | 321 | UnwindData |  |
| 6 | `SecGetDriverVersion` | `0x34E0` | 162 | UnwindData |  |
| 7 | `SecGetFileHashes` | `0x3590` | 618 | UnwindData |  |
| 8 | `SecGetProcessInfo` | `0x3800` | 524 | UnwindData |  |
| 9 | `SecGetUserLibVersion` | `0x3A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SecOpenFileAndRequestOplock` | `0x3A30` | 476 | UnwindData |  |
| 12 | `SecRequestOplock` | `0x3C10` | 279 | UnwindData |  |
| 13 | `SecSetCiInformation` | `0x3D30` | 244 | UnwindData |  |
| 26 | `SecWriteExtendedFileHashEA` | `0x3E30` | 362 | UnwindData |  |
| 27 | `SecWriteFileDlpEA` | `0x3FA0` | 426 | UnwindData |  |
| 28 | `SecWriteFileHashEA` | `0x4150` | 415 | UnwindData |  |
| 29 | `SecWriteFileMarkOfTheWebEA` | `0x42F0` | 422 | UnwindData |  |
| 1 | `SecClearKseRegistryOperations` | `0x5590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SecSetKseConfiguration` | `0x5590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SecSetKseFileMonitorOperations` | `0x5590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SecSetKseRegistryOperations` | `0x5590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SecClearRegistryOperations` | `0x55A0` | 836 | UnwindData |  |
| 23 | `SecSetRegistryOperations` | `0x58F0` | 851 | UnwindData |  |
| 14 | `SecSetConfiguration` | `0x104D0` | 2,033 | UnwindData |  |
| 15 | `SecSetDlpConfiguration` | `0x10CD0` | 497 | UnwindData |  |
| 20 | `SecSetLmfConfiguration` | `0x10ED0` | 627 | UnwindData |  |
| 21 | `SecSetLmfNetworkShareConfiguration` | `0x11150` | 1,347 | UnwindData |  |
| 22 | `SecSetLmfSysvolAccessConfiguration` | `0x116A0` | 851 | UnwindData |  |
| 16 | `SecSetFileMonitorOperations` | `0x14090` | 747 | UnwindData |  |
