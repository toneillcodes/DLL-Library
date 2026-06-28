# Binary Specification: wdc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wdc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d6dd644d5837e9dfc275e5a16ca5fe1d9ec9ef02c46bc33f5b3aa003c0123b03`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x2CE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x2CE40` | 205 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x2D030` | 246,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x2D030` | 246,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WdcParseLegacyFile` | `0x69290` | 201 | UnwindData |  |
| 2 | `WdcRunTaskAsInteractiveUser` | `0x699E0` | 1,303 | UnwindData |  |
