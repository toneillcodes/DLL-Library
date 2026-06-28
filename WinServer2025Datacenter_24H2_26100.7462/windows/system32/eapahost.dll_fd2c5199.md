# Binary Specification: eapahost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\eapahost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fd2c51991bbdf03bb7181c9ac2a84dcdde0d96b8eb0ef2e56d8f463623eb6209`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x5980` | 96 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x5A40` | 72 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x5A90` | 64 | UnwindData |  |
| 5 | `InitializeEapHost` | `0x5AE0` | 31 | UnwindData |  |
| 6 | `UninitializeEapHost` | `0x5CF0` | 18 | UnwindData |  |
