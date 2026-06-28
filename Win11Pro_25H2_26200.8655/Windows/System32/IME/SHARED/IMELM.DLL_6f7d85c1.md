# Binary Specification: IMELM.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\SHARED\IMELM.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f7d85c1ae3716491a3df92d68943f4b3f25d09aa8057d957484b2390252c3ac`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7BE0` | 36,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x10B40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x10B90` | 138 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x10C20` | 24 | UnwindData |  |
