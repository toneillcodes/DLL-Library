# Binary Specification: PlaySndSrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PlaySndSrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9b52be4c70ce490414337728b1c088c99a42bd280ef6204b6ab456984c5ed610`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `PlaySoundServerInitialize` | `0x1910` | 805 | UnwindData |  |
| 4 | `PlaySoundServerTerminate` | `0x2C30` | 305 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4730` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x5AC0` | 42 | UnwindData |  |
