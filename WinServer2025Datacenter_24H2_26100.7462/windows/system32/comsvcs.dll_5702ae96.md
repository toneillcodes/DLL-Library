# Binary Specification: comsvcs.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\comsvcs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5702ae96bb6a347f4a47c1b54473fc3b4e67e82fa72982736af3d5387b090dee`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `DllCanUnloadNow` | `0xF600` | 240 | UnwindData |  |
| 16 | `DllGetClassObject` | `0x15260` | 546 | UnwindData |  |
| 14 | `DispManGetContext` | `0x286B0` | 530 | UnwindData |  |
| 5 | `CosGetCallContext` | `0x2AB30` | 68 | UnwindData |  |
| 17 | `DllRegisterServer` | `0x323C0` | 11,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DllUnregisterServer` | `0x323C0` | 11,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | *Ordinal Only* | `0x323C0` | 11,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CoCreateActivity` | `0x35270` | 577 | UnwindData |  |
| 19 | `GetMTAThreadPoolMetrics` | `0x3CE30` | 147 | UnwindData |  |
| 12 | `ComSvcsExceptionFilter` | `0x5E150` | 354 | UnwindData |  |
| 20 | `GetManagedExtensions` | `0x5E2C0` | 193 | UnwindData |  |
| 22 | `GetTrkSvrObject` | `0x5E390` | 158 | UnwindData |  |
| 24 | `MiniDumpW` | `0x5E440` | 766 | UnwindData |  |
| 9 | `CoEnterServiceDomain` | `0x63DE0` | 288 | UnwindData |  |
| 10 | `CoLeaveServiceDomain` | `0x63F10` | 78 | UnwindData |  |
| 13 | `ComSvcsLogError` | `0x66C40` | 215 | UnwindData |  |
| 21 | `GetObjectContext` | `0x66D20` | 46 | UnwindData |  |
| 25 | `RecycleSurrogate` | `0x66D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SafeRef` | `0x66D70` | 599 | UnwindData |  |
| 7 | *Ordinal Only* | `0x6E890` | 168 | UnwindData |  |
| 23 | `MTSCreateActivity` | `0x6E940` | 231 | UnwindData |  |
| 11 | `CoLoadServices` | `0x96EF0` | 188 | UnwindData |  |
