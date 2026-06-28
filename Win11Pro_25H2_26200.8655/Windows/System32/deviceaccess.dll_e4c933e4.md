# Binary Specification: deviceaccess.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\deviceaccess.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e4c933e4c14f51db4de0753049559e6431cef9fde3fe7d8f64a55c795f6a6e05`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllGetClassObject` | `0x38D0` | 75 | UnwindData |  |
| 6 | `DllGetActivationFactory` | `0x4750` | 146 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x6EE0` | 46 | UnwindData |  |
| 3 | `BrokeredOpenCommPort` | `0xEF10` | 596 | UnwindData |  |
| 1 | `ServiceMain` | `0x118C0` | 44 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x11BD0` | 7,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateDeviceAccessInstance` | `0x13870` | 36 | UnwindData |  |
| 8 | `ProcessTrackerInsertOrWait` | `0x23130` | 57 | UnwindData |  |
| 9 | `ProcessTrackerRemove` | `0x23170` | 40 | UnwindData |  |
