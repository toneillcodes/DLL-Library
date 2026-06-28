# Binary Specification: WMVSDECD.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMVSDECD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8c5493b1d358c2c1f18855175f0290019dad3b21fd41cdf084b489e84f187238`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0xE6C0` | 757 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xE9C0` | 119 | UnwindData |  |
| 1 | `CreateInstance` | `0xF130` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xF220` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xF250` | 231 | UnwindData |  |
