# Binary Specification: ProvProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\ProvProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `282f5eb39413d04e033a5e442f58fcd71642a8a66f67b7b0e0b893f4b77f319c`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x6260` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x6290` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x62C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x6430` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6530` | 114 | UnwindData |  |
