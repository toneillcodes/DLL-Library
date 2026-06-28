# Binary Specification: WUDFPlatform.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WUDFPlatform.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `51186d860e52ef7dafa66b940bc16cc7eabafc015810ea0e42ccc15f6dfc71ba`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `ClearPlatformTestingCallbacks` | `0x7D60` | 198 | UnwindData |  |
| 4 | `DllMain` | `0x9150` | 306 | UnwindData |  |
| 5 | `GetAndInitializePlatformObject` | `0xC150` | 300 | UnwindData |  |
| 6 | `InitializePlatformLibrary` | `0xC620` | 62 | UnwindData |  |
| 12 | `WdfGetLpcInterface` | `0xC7A0` | 63 | UnwindData |  |
| 9 | `SetPlatformErrorReportingCallbacks` | `0xCA00` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xCB00` | 171 | UnwindData |  |
| 11 | `ShutdownPlatformLibrary` | `0xD050` | 69 | UnwindData |  |
| 1 | `GetPlatformObject` | `0xDFC0` | 28,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WudfDebugBreakPoint` | `0x15020` | 78 | UnwindData |  |
| 14 | `WudfIsAnyDebuggerPresent` | `0x15080` | 24 | UnwindData |  |
| 15 | `WudfIsKernelDebuggerPresent` | `0x15130` | 32 | UnwindData |  |
| 16 | `WudfIsUserDebuggerPresent` | `0x15160` | 32 | UnwindData |  |
| 17 | `WudfWaitForDebugger` | `0x15190` | 455 | UnwindData |  |
| 7 | `PlatformSimulateUnhandledException` | `0x1BD60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PlatformUnhandledExceptionFilter` | `0x1BDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SetPlatformTestingCallbacks` | `0x1BDD0` | 254 | UnwindData |  |
