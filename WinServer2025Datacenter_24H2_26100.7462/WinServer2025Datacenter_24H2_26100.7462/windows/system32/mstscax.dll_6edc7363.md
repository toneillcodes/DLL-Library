# Binary Specification: mstscax.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mstscax.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6edc7363807a3a6a986e1ba73aea8abd1b283093f3334f0286f8ca546757a312`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xF7A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xF7A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetTscCtlVer` | `0xF7A40` | 18 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xF7A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xF7A70` | 74 | UnwindData |  |
