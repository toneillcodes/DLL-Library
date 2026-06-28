# Binary Specification: NetNat.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\NetNat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eb0a3c2df8ae1545081342f87e127d5a0dfd4bffcd869fb877dd1dab87043e7d`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x1B90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x1C20` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1C60` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x1CE0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1D40` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1D90` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1FB0` | 35,728 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
