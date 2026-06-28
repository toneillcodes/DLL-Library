# Binary Specification: mssecuser.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mssecuser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `024184136a2f29a5ff00605d32892dbd607b00bffb2382014441d906a9c8bcc2`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `SecRegisterConsumer` | `0x12F0` | 315 | UnwindData |  |
| 24 | `SecUninitializeDriver` | `0x1430` | 81 | UnwindData |  |
| 25 | `SecUnregisterConsumer` | `0x1490` | 264 | UnwindData |  |
| 3 | `SecCreateSessionFilter` | `0x6DC0` | 145 | UnwindData |  |
| 4 | `SecDeleteSessionFilter` | `0x6E60` | 69 | UnwindData |  |
| 5 | `SecGetCiInformation` | `0x6EB0` | 314 | UnwindData |  |
| 6 | `SecGetDriverVersion` | `0x6FF0` | 162 | UnwindData |  |
| 7 | `SecGetFileHashes` | `0x70A0` | 612 | UnwindData |  |
| 8 | `SecGetProcessInfo` | `0x7310` | 517 | UnwindData |  |
| 9 | `SecGetUserLibVersion` | `0x7520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SecOpenFileAndRequestOplock` | `0x7540` | 470 | UnwindData |  |
| 12 | `SecRequestOplock` | `0x7720` | 272 | UnwindData |  |
| 13 | `SecSetCiInformation` | `0x7830` | 237 | UnwindData |  |
| 26 | `SecWriteExtendedFileHashEA` | `0x7920` | 356 | UnwindData |  |
| 27 | `SecWriteFileDlpEA` | `0x7A90` | 420 | UnwindData |  |
| 28 | `SecWriteFileHashEA` | `0x7C40` | 409 | UnwindData |  |
| 29 | `SecWriteFileMarkOfTheWebEA` | `0x7DE0` | 416 | UnwindData |  |
| 1 | `SecClearKseRegistryOperations` | `0x85F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SecSetKseConfiguration` | `0x85F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SecSetKseFileMonitorOperations` | `0x85F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SecSetKseRegistryOperations` | `0x85F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SecClearRegistryOperations` | `0x8600` | 856 | UnwindData |  |
| 23 | `SecSetRegistryOperations` | `0x8960` | 858 | UnwindData |  |
| 14 | `SecSetConfiguration` | `0xFE40` | 2,026 | UnwindData |  |
| 15 | `SecSetDlpConfiguration` | `0x10630` | 491 | UnwindData |  |
| 20 | `SecSetLmfConfiguration` | `0x10820` | 588 | UnwindData |  |
| 21 | `SecSetLmfNetworkShareConfiguration` | `0x10A70` | 1,242 | UnwindData |  |
| 22 | `SecSetLmfSysvolAccessConfiguration` | `0x10F50` | 768 | UnwindData |  |
| 16 | `SecSetFileMonitorOperations` | `0x13AB0` | 742 | UnwindData |  |
