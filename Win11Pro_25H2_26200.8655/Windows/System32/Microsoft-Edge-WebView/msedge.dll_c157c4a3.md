# Binary Specification: msedge.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\msedge.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c157c4a3d0ad31dab18a9abbcc6029814e272cc1987db065699e4e8c8c341962`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `ChromeMain` | `0x15AF4A0` | 1,052 | UnwindData |  |
| 13 | `GetHandleVerifier` | `0x17B9840` | 33 | UnwindData |  |
| 14 | `IsSandboxedProcess` | `0x17D2490` | 21,078,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CreateSmartScreenClient` | `0x2BEC4E0` | 3,338 | UnwindData |  |
| 15 | `RelaunchChromeBrowserWithNewCommandLineIfNeeded` | `0x3094C40` | 98 | UnwindData |  |
| 3 | `??1IDataFieldVisitor@telemetry_client@@UEAA@XZ` | `0x5157BD0` | 758,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??4IDataFieldVisitor@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x5210D70` | 15,856,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0IDataFieldVisitor@telemetry_client@@QEAA@AEBV01@@Z` | `0x6130210` | 6,958,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0IDataFieldVisitor@telemetry_client@@QEAA@XZ` | `0x6130210` | 6,958,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CrashForExceptionInNonABICompliantCodeRange` | `0x67D2FD0` | 98 | UnwindData |  |
| 12 | `ExportSpartanCookies` | `0xA09C7D0` | 311 | UnwindData |  |
| 11 | `EdgeLaunchBrowserToHandleBackgroundTaskEvent` | `0xA09C910` | 198 | UnwindData |  |
| 10 | `EdgeGetPasskeyAuthenticatorPluginClassFactory` | `0xA09C9E0` | 258 | UnwindData |  |
| 38 | `sqlite3_dbdata_init` | `0xA975CC0` | 73 | UnwindData |  |
| 20 | `argon2_type2string` | `0xC188030` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `argon2_ctx` | `0xC188080` | 253 | UnwindData |  |
| 19 | `argon2_hash` | `0xC188180` | 505 | UnwindData |  |
| 29 | `argon2i_hash_encoded` | `0xC188380` | 92 | UnwindData |  |
| 30 | `argon2i_hash_raw` | `0xC1883E0` | 78 | UnwindData |  |
| 24 | `argon2d_hash_encoded` | `0xC188430` | 92 | UnwindData |  |
| 25 | `argon2d_hash_raw` | `0xC188490` | 78 | UnwindData |  |
| 34 | `argon2id_hash_encoded` | `0xC1884E0` | 92 | UnwindData |  |
| 35 | `argon2id_hash_raw` | `0xC188540` | 78 | UnwindData |  |
| 21 | `argon2_verify` | `0xC188590` | 367 | UnwindData |  |
| 22 | `argon2_verify_ctx` | `0xC188700` | 91 | UnwindData |  |
| 31 | `argon2i_verify` | `0xC188760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `argon2d_verify` | `0xC188770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `argon2id_verify` | `0xC188780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `argon2d_ctx` | `0xC188790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `argon2i_ctx` | `0xC1887A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `argon2id_ctx` | `0xC1887B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `argon2d_verify_ctx` | `0xC1887C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `argon2i_verify_ctx` | `0xC1887D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `argon2id_verify_ctx` | `0xC1887E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `argon2_error_message` | `0xC1887F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `argon2_encodedlen` | `0xC188810` | 170 | UnwindData |  |
| 9 | `CreateTestWebClientProxy` | `0xC4A8550` | 2,839 | UnwindData |  |
| 5 | `??_7IDataFieldVisitor@telemetry_client@@6B@` | `0xF907820` | 0 | Indeterminate |  |
