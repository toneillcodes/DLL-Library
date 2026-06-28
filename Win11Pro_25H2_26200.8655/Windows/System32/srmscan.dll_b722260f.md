# Binary Specification: srmscan.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\srmscan.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b722260f138af912033cf9eac4f34f68d54c807546ac049c6f4d6981006c451c`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `SrmCalculateCrcHash` | `0x4AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SrmCreateOrDeleteNotificationScheduledTask` | `0x4AD0` | 619 | UnwindData |  |
| 3 | `SrmEnsureSystemVolumeInformationFolder` | `0x4D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SrmIsInCluster` | `0x4D60` | 243 | UnwindData |  |
| 8 | `SrmLocalFileTimeToUtcFileTime` | `0x4E60` | 74 | UnwindData |  |
| 7 | `SrmUtcFileTimeToLocalFileTime` | `0x52B0` | 74 | UnwindData |  |
| 5 | `SrmValidateNamespaceRoots` | `0x5300` | 312 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x6400` | 26 | UnwindData |  |
| 10 | `DllGetClassObject` | `0x6420` | 72 | UnwindData |  |
| 1 | `SrmIsNameInExpression` | `0x6A20` | 411 | UnwindData |  |
