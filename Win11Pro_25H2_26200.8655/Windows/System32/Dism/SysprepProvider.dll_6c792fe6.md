# Binary Specification: SysprepProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\SysprepProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6c792fe681afb882a79130d0e1cff4ef25432a357d1fca9a8f94e65b3f1a6fa7`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x4560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x4590` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x45C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4730` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4830` | 114 | UnwindData |  |
