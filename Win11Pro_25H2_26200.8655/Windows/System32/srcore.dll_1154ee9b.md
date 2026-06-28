# Binary Specification: srcore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\srcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1154ee9b84c34e3b994e541b823e17381ddcb232cc88afebdd76e5a4c1042017`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xABB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xABD0` | 170 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xADD0` | 110 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xAE50` | 215 | UnwindData |  |
| 6 | `SrFreeRestoreStatus` | `0xAF30` | 41 | UnwindData |  |
| 7 | `SrFreeRpPropArray` | `0xAF60` | 97 | UnwindData |  |
| 5 | `ShutdownContinuation` | `0x112B0` | 557 | UnwindData |  |
