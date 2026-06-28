# Binary Specification: comsvcs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\comsvcs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8232579b54893b442e3ed4b4e05ae523bc5e82fa9ea25d66c34209e51bd4ca1b`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `DllCanUnloadNow` | `0xF610` | 240 | UnwindData |  |
| 16 | `DllGetClassObject` | `0x15270` | 546 | UnwindData |  |
| 14 | `DispManGetContext` | `0x286C0` | 530 | UnwindData |  |
| 5 | `CosGetCallContext` | `0x2AB40` | 68 | UnwindData |  |
| 17 | `DllRegisterServer` | `0x323D0` | 11,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DllUnregisterServer` | `0x323D0` | 11,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | *Ordinal Only* | `0x323D0` | 11,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CoCreateActivity` | `0x35280` | 577 | UnwindData |  |
| 19 | `GetMTAThreadPoolMetrics` | `0x3CE40` | 147 | UnwindData |  |
| 12 | `ComSvcsExceptionFilter` | `0x5E160` | 354 | UnwindData |  |
| 20 | `GetManagedExtensions` | `0x5E2D0` | 193 | UnwindData |  |
| 22 | `GetTrkSvrObject` | `0x5E3A0` | 158 | UnwindData |  |
| 24 | `MiniDumpW` | `0x5E450` | 766 | UnwindData |  |
| 9 | `CoEnterServiceDomain` | `0x63DF0` | 288 | UnwindData |  |
| 10 | `CoLeaveServiceDomain` | `0x63F20` | 78 | UnwindData |  |
| 13 | `ComSvcsLogError` | `0x66C50` | 215 | UnwindData |  |
| 21 | `GetObjectContext` | `0x66D30` | 46 | UnwindData |  |
| 25 | `RecycleSurrogate` | `0x66D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SafeRef` | `0x66D80` | 599 | UnwindData |  |
| 7 | *Ordinal Only* | `0x6E8A0` | 168 | UnwindData |  |
| 23 | `MTSCreateActivity` | `0x6E950` | 231 | UnwindData |  |
| 11 | `CoLoadServices` | `0x96F00` | 188 | UnwindData |  |
