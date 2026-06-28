# Binary Specification: CbmrProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\CbmrProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bc75740947e85f7106ed81e9e7738dc187938bdd9799bb46f55164fc1a8c768b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3460` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3490` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x34C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3630` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3730` | 114 | UnwindData |  |
