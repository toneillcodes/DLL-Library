# Binary Specification: WinSATAPI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WinSATAPI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d2b70e34c45961708fa65572e15f495f814e73cc000b8772eb428e1dd4e844bc`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xB700` | 53 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xD540` | 274 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1A780` | 100 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1A7F0` | 94,684 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
