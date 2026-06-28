# Binary Specification: LogProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\LogProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f3f15fd48d50c711444ba788212aaaadad43a368c39bb36de4e01ad37f2c1cbe`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3870` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x38A0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x38D0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3A40` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3B40` | 114 | UnwindData |  |
