# Binary Specification: inseng.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\inseng.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d45b4bc33d8702991098f8ac2926f42a860808dec8910afe62107a8281dad2a2`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `GetICifFileFromFile` | `0x6090` | 127 | UnwindData |  |
| 8 | `GetICifRWFileFromFile` | `0x6120` | 168 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xEA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0xEA90` | 143 | UnwindData |  |
| 9 | `PurgeDownloadDirectory` | `0xEBE0` | 10,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckForVersionConflict` | `0x11340` | 37 | UnwindData |  |
| 2 | `CheckTrust` | `0x11370` | 31 | UnwindData |  |
| 3 | `CheckTrustEx` | `0x113A0` | 549 | UnwindData |  |
| 6 | `DownloadFile` | `0x115D0` | 333 | UnwindData |  |
