# Binary Specification: VhdProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\VhdProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3f50efd92abce7421d5d10e966bc0c95c10a9ead3455dad914af3beac6b50ca8`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0xB3E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xB410` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xB440` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xB5B0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xB6B0` | 114 | UnwindData |  |
