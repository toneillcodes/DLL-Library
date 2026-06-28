# Binary Specification: WUDFPlatform.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WUDFPlatform.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `90fa28b8651829ca69c017b8baa40b183dd129c883c18f9d075860acd7da826d`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `ClearPlatformTestingCallbacks` | `0x7D10` | 198 | UnwindData |  |
| 4 | `DllMain` | `0x9100` | 306 | UnwindData |  |
| 5 | `GetAndInitializePlatformObject` | `0xC160` | 300 | UnwindData |  |
| 6 | `InitializePlatformLibrary` | `0xC630` | 62 | UnwindData |  |
| 12 | `WdfGetLpcInterface` | `0xC7B0` | 63 | UnwindData |  |
| 9 | `SetPlatformErrorReportingCallbacks` | `0xCA10` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xCB10` | 171 | UnwindData |  |
| 11 | `ShutdownPlatformLibrary` | `0xD060` | 69 | UnwindData |  |
| 1 | `GetPlatformObject` | `0xDFD0` | 28,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WudfDebugBreakPoint` | `0x15010` | 78 | UnwindData |  |
| 14 | `WudfIsAnyDebuggerPresent` | `0x15070` | 24 | UnwindData |  |
| 15 | `WudfIsKernelDebuggerPresent` | `0x15120` | 32 | UnwindData |  |
| 16 | `WudfIsUserDebuggerPresent` | `0x15150` | 32 | UnwindData |  |
| 17 | `WudfWaitForDebugger` | `0x15180` | 455 | UnwindData |  |
| 7 | `PlatformSimulateUnhandledException` | `0x1BD50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PlatformUnhandledExceptionFilter` | `0x1BDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SetPlatformTestingCallbacks` | `0x1BDC0` | 254 | UnwindData |  |
