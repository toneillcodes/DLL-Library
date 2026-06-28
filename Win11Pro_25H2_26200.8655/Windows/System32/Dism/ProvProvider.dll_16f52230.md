# Binary Specification: ProvProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\ProvProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16f52230fc20912476fc09ab63e1f1e31196a81e05abd8f039e297dbd96132b9`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x6260` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x6290` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x62C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x6430` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6530` | 114 | UnwindData |  |
