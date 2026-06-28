# Binary Specification: msdbg2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\F12\msdbg2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dfb481610d6f63680da8436eed0221360b2a5f2c41af7c0455614404a44e42a7`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1390` | 46 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x13E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1410` | 381,232 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
