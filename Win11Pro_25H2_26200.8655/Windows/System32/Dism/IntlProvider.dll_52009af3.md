# Binary Specification: IntlProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\IntlProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `52009af381aa501e26b760ce47b7418568ef8e2c1977af87785b7b26257f4569`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0xDF70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xDFA0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xDFD0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xE140` | 304 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xE280` | 166 | UnwindData |  |
