# Binary Specification: SysprepProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\SysprepProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7703c6a0bf29130d78304ffdc8fa4bb19ab71aa3be25d2bc72b2d1af8d8b57d5`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x41B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x41E0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4210` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4380` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4480` | 114 | UnwindData |  |
