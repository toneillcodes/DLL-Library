# Binary Specification: bisrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\bisrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c35506841282ce5fa2a88ac8e809e92f29beb4622c07ca9f797395c86de7d60e`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PsmBiExtInitialize` | `0x6F300` | 22,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PsmBiExtNotifyAppState` | `0x6F300` | 22,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PsmBiExtNotifySessionStateChange` | `0x749C0` | 3,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PsmBiExtNotifySessionUserStateChange` | `0x75950` | 72,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PsmBiExtNotifyRmInitializationComplete` | `0x874C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PsmBiExtNotifyWerReportProgress` | `0x874D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PsmBiExtPrepareToSuspendPackage` | `0x874E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PsmBiExtResumePackage` | `0x874F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PsmBiExtServerCleanup` | `0x87500` | 18 | UnwindData |  |
| 10 | `PsmBiExtServerInitialize` | `0x87520` | 197 | UnwindData |  |
| 11 | `PsmBiExtServerStart` | `0x875F0` | 140,668 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
