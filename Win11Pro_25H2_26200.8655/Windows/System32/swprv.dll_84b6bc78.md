# Binary Specification: swprv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\swprv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `84b6bc78afd473d9e78809bc56b22600d89eb968e323b6db820964167089fcf8`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0xC800` | 37 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xD400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xD420` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xD4C0` | 184 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xD580` | 127 | UnwindData |  |
