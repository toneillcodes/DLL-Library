# Binary Specification: MSMPEG2ENC.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\MSMPEG2ENC.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16a05d7ef60914f447a89ea1f77a2531bdec7438dc769c48e546a81fe801f154`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x1E1B0` | 66 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1E200` | 49 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1E550` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1E590` | 274 | UnwindData |  |
