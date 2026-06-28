# Binary Specification: AssocProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\AssocProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `21c8ddc0742aa015e64314c775edad48f4db83d277bb3c5b63f9f2e71efd249e`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x38E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3910` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3940` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3AB0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3BB0` | 114 | UnwindData |  |
