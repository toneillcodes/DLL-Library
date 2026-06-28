# Binary Specification: tcbloader.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tcbloader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `818b6a72e4240b3bb3dd236fb03ab676cfdedf240959b8add9e99b2b011bbd3e`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `OslGetFirmwarePayload` | `0x6E90` | 69 | UnwindData |  |
| 2 | `OslGetControlSubkeyCell` | `0x1BA60` | 146 | UnwindData |  |
| 6 | `OslGetStringValue` | `0x1C140` | 255 | UnwindData |  |
| 7 | `OslGetSubkey` | `0x1C250` | 85 | UnwindData |  |
| 8 | `OslGetValue` | `0x1C4E0` | 294 | UnwindData |  |
| 1 | `OslGenRandomBytes` | `0x204B0` | 35 | UnwindData |  |
| 5 | `OslGetHotPatchPath` | `0x20B70` | 204 | UnwindData |  |
| 9 | `OslIsRunningInSecureKernel` | `0x228F0` | 12 | UnwindData |  |
| 10 | `TcbLoadEntry` | `0x22F80` | 456 | UnwindData |  |
| 11 | `TcbResumeEntry` | `0x23150` | 335 | UnwindData |  |
| 3 | `OslGetExportRoutineInModule` | `0x232C0` | 7 | UnwindData |  |
