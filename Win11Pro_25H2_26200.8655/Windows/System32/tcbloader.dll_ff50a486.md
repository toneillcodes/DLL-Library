# Binary Specification: tcbloader.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tcbloader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ff50a486a6e552aa3e4960a91eb342eb47c812383a392156965cf3cef9c9dd93`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `OslGetFirmwarePayload` | `0x7360` | 69 | UnwindData |  |
| 2 | `OslGetControlSubkeyCell` | `0x1BFE0` | 146 | UnwindData |  |
| 6 | `OslGetStringValue` | `0x1C6C0` | 255 | UnwindData |  |
| 7 | `OslGetSubkey` | `0x1C7D0` | 85 | UnwindData |  |
| 8 | `OslGetValue` | `0x1CA60` | 294 | UnwindData |  |
| 1 | `OslGenRandomBytes` | `0x20A40` | 35 | UnwindData |  |
| 5 | `OslGetHotPatchPath` | `0x21100` | 204 | UnwindData |  |
| 9 | `OslIsRunningInSecureKernel` | `0x22E80` | 12 | UnwindData |  |
| 10 | `TcbLoadEntry` | `0x23510` | 456 | UnwindData |  |
| 11 | `TcbResumeEntry` | `0x236E0` | 364 | UnwindData |  |
| 3 | `OslGetExportRoutineInModule` | `0x23860` | 7 | UnwindData |  |
