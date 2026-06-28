# Binary Specification: msctfui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msctfui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `46e80c8f7eb56ad16b5ac1a5a6ba48c0cc70d8904b3f2c8d79cac94f5c9a703a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x28B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x28C0` | 253 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x29D0` | 153 | UnwindData |  |
