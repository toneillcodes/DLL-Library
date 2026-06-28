# Binary Specification: devinv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\devinv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6babac8452bbc6f2f34bab4aed22aabc863505a518b0b174da5a643c8d835e78`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `ReportDeviceRemove` | `0x112F0` | 90,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateDeviceInventoryTC2` | `0x272D0` | 626 | UnwindData |  |
| 3 | `CreateDeviceInventoryTC` | `0x27550` | 9,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetDevInventory` | `0x29A40` | 1,119 | UnwindData |  |
| 5 | `RunDeviceInventoryW` | `0x2E800` | 292 | UnwindData |  |
| 6 | `CreateDeviceInventory` | `0x315B0` | 1,003 | UnwindData |  |
| 7 | `GetAndSendSigningInfo` | `0x319B0` | 340 | UnwindData |  |
| 8 | `ReportDeviceAdd` | `0x31B10` | 806 | UnwindData |  |
| 1 | `SetDevInvDebugCorrelationVector` | `0x31E40` | 110 | UnwindData |  |
