# Binary Specification: FfuProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\FfuProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7ca1c70d20c80970d73733bc3208e804ce4b4bd7f9dd8c8023514294e09d9a96`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x4160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x4190` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x41C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4330` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4430` | 114 | UnwindData |  |
