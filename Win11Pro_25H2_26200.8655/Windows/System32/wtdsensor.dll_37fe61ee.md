# Binary Specification: wtdsensor.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wtdsensor.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `37fe61ee2153fb4de3f587cbea7dd4b5c91df9f3eb3557fbdd7de40796cb38ff`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WtdsAllocateEvent` | `0x2170` | 605 | UnwindData |  |
| 2 | `WtdsFreeEvent` | `0x23E0` | 355 | UnwindData |  |
| 3 | `WtdsGetEventData` | `0x2550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WtdsGetProcessId` | `0x2580` | 214 | UnwindData |  |
| 5 | `WtdsRegisterSensor` | `0x2660` | 740 | UnwindData |  |
| 6 | `WtdsSendEvent` | `0x2950` | 669 | UnwindData |  |
| 7 | `WtdsUnregisterSensor` | `0x2C00` | 545 | UnwindData |  |
