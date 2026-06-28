# Binary Specification: IMELM.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\SHARED\IMELM.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7822db03ba9cfbec73c0222b911f1a5b03b3b2efef1e1a6d4af46e35607fbeb2`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7BE0` | 36,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x10B10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x10B60` | 138 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x10BF0` | 24 | UnwindData |  |
