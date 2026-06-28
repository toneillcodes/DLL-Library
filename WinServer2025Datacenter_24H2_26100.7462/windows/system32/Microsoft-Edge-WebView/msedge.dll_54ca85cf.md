# Binary Specification: msedge.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\msedge.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `54ca85cf95c8798bf7ca21814eb039b56151497a74ec0b1fef91c5480e7e4d35`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `ChromeMain` | `0x327850` | 1,067 | UnwindData |  |
| 12 | `GetHandleVerifier` | `0x4E6610` | 33 | UnwindData |  |
| 13 | `IsSandboxedProcess` | `0x4FE400` | 31,481,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CreateSmartScreenClient` | `0x2304240` | 3,045 | UnwindData |  |
| 14 | `RelaunchChromeBrowserWithNewCommandLineIfNeeded` | `0x2B0AB70` | 94 | UnwindData |  |
| 3 | `??1IDataFieldVisitor@telemetry_client@@UEAA@XZ` | `0x36DF1A0` | 599,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??4IDataFieldVisitor@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x3771640` | 14,327,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0IDataFieldVisitor@telemetry_client@@QEAA@AEBV01@@Z` | `0x451B460` | 5,525,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0IDataFieldVisitor@telemetry_client@@QEAA@XZ` | `0x451B460` | 5,525,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CrashForExceptionInNonABICompliantCodeRange` | `0x4A604B0` | 98 | UnwindData |  |
| 11 | `ExportSpartanCookies` | `0x7F4A0B0` | 328 | UnwindData |  |
| 10 | `EdgeLaunchBrowserToHandleBackgroundTaskEvent` | `0x7F4A200` | 166 | UnwindData |  |
| 37 | `sqlite3_dbdata_init` | `0x87C3270` | 73 | UnwindData |  |
| 19 | `argon2_type2string` | `0x9DC8110` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `argon2_ctx` | `0x9DC8160` | 257 | UnwindData |  |
| 18 | `argon2_hash` | `0x9DC8270` | 520 | UnwindData |  |
| 28 | `argon2i_hash_encoded` | `0x9DC8480` | 92 | UnwindData |  |
| 29 | `argon2i_hash_raw` | `0x9DC84E0` | 78 | UnwindData |  |
| 23 | `argon2d_hash_encoded` | `0x9DC8530` | 92 | UnwindData |  |
| 24 | `argon2d_hash_raw` | `0x9DC8590` | 78 | UnwindData |  |
| 33 | `argon2id_hash_encoded` | `0x9DC85E0` | 92 | UnwindData |  |
| 34 | `argon2id_hash_raw` | `0x9DC8640` | 78 | UnwindData |  |
| 20 | `argon2_verify` | `0x9DC8690` | 371 | UnwindData |  |
| 21 | `argon2_verify_ctx` | `0x9DC8810` | 91 | UnwindData |  |
| 30 | `argon2i_verify` | `0x9DC8870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `argon2d_verify` | `0x9DC8880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `argon2id_verify` | `0x9DC8890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `argon2d_ctx` | `0x9DC88A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `argon2i_ctx` | `0x9DC88B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `argon2id_ctx` | `0x9DC88C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `argon2d_verify_ctx` | `0x9DC88D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `argon2i_verify_ctx` | `0x9DC88E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `argon2id_verify_ctx` | `0x9DC88F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `argon2_error_message` | `0x9DC8900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `argon2_encodedlen` | `0x9DC8920` | 170 | UnwindData |  |
| 9 | `CreateTestWebClientProxy` | `0xA0EF930` | 2,459 | UnwindData |  |
| 5 | `??_7IDataFieldVisitor@telemetry_client@@6B@` | `0xEC488F0` | 0 | Indeterminate |  |
