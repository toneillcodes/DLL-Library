# Binary Specification: deviceaccess.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\deviceaccess.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c9c4112067d2929bfc143035f05fdee08450e0ca2c600e474c58d23807621f21`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllGetClassObject` | `0x38C0` | 75 | UnwindData |  |
| 6 | `DllGetActivationFactory` | `0x4710` | 146 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x6EA0` | 46 | UnwindData |  |
| 3 | `BrokeredOpenCommPort` | `0xEE10` | 596 | UnwindData |  |
| 1 | `ServiceMain` | `0x117C0` | 44 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x11AD0` | 7,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateDeviceAccessInstance` | `0x13770` | 36 | UnwindData |  |
| 8 | `ProcessTrackerInsertOrWait` | `0x244F0` | 57 | UnwindData |  |
| 9 | `ProcessTrackerRemove` | `0x24530` | 40 | UnwindData |  |
