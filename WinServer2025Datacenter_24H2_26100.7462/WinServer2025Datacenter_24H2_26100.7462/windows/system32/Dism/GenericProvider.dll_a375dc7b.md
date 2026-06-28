# Binary Specification: GenericProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\GenericProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a375dc7b050382469b8e12fe4f7642db90d1f4e0b24be10491e4af9550f34da5`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3AA0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3AD0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3C40` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3D40` | 114 | UnwindData |  |
