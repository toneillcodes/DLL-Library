# Binary Specification: NPSM.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NPSM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6e0b432d3d9b462573ee2a53743a128aea34c0d1765e27a9e6aacc38b14166bc`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x4C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetActivationFactory` | `0x4C60` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4CA0` | 65 | UnwindData |  |
| 4 | `ServiceMain` | `0x7190` | 423 | UnwindData |  |
| 5 | `SvchostPushServiceGlobals` | `0x7340` | 101,838 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
