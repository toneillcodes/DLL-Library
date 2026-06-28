# Binary Specification: dot3gpui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dot3gpui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `972ef558ec96eb50a34c819a5f00c751c481d38c66b9aae0610091a4dfa5ce30`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x111A0` | 94 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x11210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x11240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x11260` | 62,755 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
