# Binary Specification: PlaySndSrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PlaySndSrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `181f5b88fe9ad7f2fd62b7ab1e8b06dba27615ecd7db2dd7aa1577d4844cd64a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `PlaySoundServerInitialize` | `0x1910` | 805 | UnwindData |  |
| 4 | `PlaySoundServerTerminate` | `0x2C30` | 305 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4730` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x5AC0` | 42 | UnwindData |  |
