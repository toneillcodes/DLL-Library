# Binary Specification: comuid.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\comuid.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `34b2b70c842fccefff2e292e2e26f69c62cb071c11e3cc8c0126bcd0fc630403`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8A90` | 109 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x8B10` | 120 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x8B90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x8BD0` | 177 | UnwindData |  |
| 1 | `CreateDCOMSecurityUIPage` | `0x72950` | 751 | UnwindData |  |
