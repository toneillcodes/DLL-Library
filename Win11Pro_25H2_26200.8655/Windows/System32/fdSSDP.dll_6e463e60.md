# Binary Specification: fdSSDP.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fdSSDP.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6e463e60fbfcc7495a1b6884c633de286c2a2a3c9299f16fe66eb498fb607ae1`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xC820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xC840` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xCAA0` | 166 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xCB50` | 127 | UnwindData |  |
| 5 | `FdphostSessionChange` | `0xCBE0` | 20 | UnwindData |  |
| 6 | `FdphostSetComContext` | `0xCC00` | 69 | UnwindData |  |
| 7 | `FdphostSetSharedService` | `0xCC50` | 59 | UnwindData |  |
