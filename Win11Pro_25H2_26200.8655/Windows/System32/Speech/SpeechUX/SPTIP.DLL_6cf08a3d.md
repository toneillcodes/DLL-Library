# Binary Specification: SPTIP.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Speech\SpeechUX\SPTIP.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cf08a3d053986df5de61632d208c0a5705a143c937d1ecec90beacacd5e1fb9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x12DC0` | 104 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x12E30` | 173 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x131C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x131D0` | 127 | UnwindData |  |
