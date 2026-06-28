# Binary Specification: devinv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\devinv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8169cf6e8dfb8654d292afbe014aa5a2a36112ae47bfcc698885ec1b0f236543`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `ReportDeviceRemove` | `0x15410` | 88,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateDeviceInventoryTC2` | `0x2AEC0` | 974 | UnwindData |  |
| 3 | `CreateDeviceInventoryTC` | `0x2B2A0` | 7,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetDevInventory` | `0x2CF20` | 1,115 | UnwindData |  |
| 5 | `RunDeviceInventoryW` | `0x31650` | 292 | UnwindData |  |
| 6 | `CreateDeviceInventory` | `0x34010` | 1,003 | UnwindData |  |
| 7 | `GetAndSendSigningInfo` | `0x34410` | 340 | UnwindData |  |
| 8 | `ReportDeviceAdd` | `0x34570` | 806 | UnwindData |  |
| 1 | `SetDevInvDebugCorrelationVector` | `0x348A0` | 110 | UnwindData |  |
