# Binary Specification: smartscreenps.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\smartscreenps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e5e5cd14037d2dad4a3a932ff98f15a19e0ebfefdf984d55ede73af24630a944`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xBB00` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xBB40` | 255 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xBC50` | 53 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xBCB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xBCE0` | 1,388 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
