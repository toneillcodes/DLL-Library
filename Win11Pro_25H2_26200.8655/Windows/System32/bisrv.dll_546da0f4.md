# Binary Specification: bisrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bisrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `546da0f49310ec1667d0622a2af9b84e1cf18e6048ebdd9caf10a986ba3fa091`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PsmBiExtInitialize` | `0x6EAB0` | 23,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PsmBiExtNotifyAppState` | `0x6EAB0` | 23,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PsmBiExtNotifySessionStateChange` | `0x747E0` | 3,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PsmBiExtNotifySessionUserStateChange` | `0x75700` | 70,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PsmBiExtNotifyRmInitializationComplete` | `0x86940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PsmBiExtNotifyWerReportProgress` | `0x86950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PsmBiExtPrepareToSuspendPackage` | `0x86960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PsmBiExtResumePackage` | `0x86970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PsmBiExtServerCleanup` | `0x86980` | 18 | UnwindData |  |
| 10 | `PsmBiExtServerInitialize` | `0x869A0` | 197 | UnwindData |  |
| 11 | `PsmBiExtServerStart` | `0x86A70` | 132,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
