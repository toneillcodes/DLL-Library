# Binary Specification: hpbuio64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\hponedriver_spd_v4_x64.inf_amd64_c13ce8ed6c565197\x64\hpbuio64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cb7ff7fca6301e319a00fad4121d331bfddf32590a1983c173ef0cd6d0dd9316`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `??1Stream@UnifiedIO@@UEAA@XZ` | `0x2870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0Stream@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0Stream@UnifiedIO@@QEAA@XZ` | `0x2890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??4HTTPRequest@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??4HTTPResponse@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??4MIBConnection@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??4Notifier@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??4Stream@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1Notifier@UnifiedIO@@UEAA@XZ` | `0x28D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0Notifier@UnifiedIO@@QEAA@AEBV01@@Z` | `0x28F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0Notifier@UnifiedIO@@QEAA@XZ` | `0x28F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1HTTPRequest@UnifiedIO@@UEAA@XZ` | `0x2920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0HTTPRequest@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0HTTPRequest@UnifiedIO@@QEAA@XZ` | `0x2940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1HTTPResponse@UnifiedIO@@UEAA@XZ` | `0x2970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0HTTPResponse@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0HTTPResponse@UnifiedIO@@QEAA@XZ` | `0x2980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??1MIBConnection@UnifiedIO@@UEAA@XZ` | `0x2990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0MIBConnection@UnifiedIO@@QEAA@AEBV01@@Z` | `0x29B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0MIBConnection@UnifiedIO@@QEAA@XZ` | `0x29B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1Address@UnifiedIO@@MEAA@XZ` | `0x29E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0Address@UnifiedIO@@QEAA@XZ` | `0x2A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0Address@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??4Address@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x2A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CreateAddressFromIPAddress` | `0x2A70` | 495 | UnwindData |  |
| 43 | `CreateAddressFromPortName` | `0x2C60` | 156 | UnwindData |  |
| 44 | `CreateAddressFromQueueName` | `0x2D90` | 156 | UnwindData |  |
| 41 | `CreateAddressFromHostName` | `0x2EC0` | 156 | UnwindData |  |
| 69 | `GetRefreshedDeviceIPAddress` | `0x2FF0` | 157 | UnwindData |  |
| 82 | `SendPrepareToPrint` | `0x3090` | 89 | UnwindData |  |
| 58 | `GetAutoSendStatus` | `0x3180` | 99 | UnwindData |  |
| 54 | `EnableAutoSendStatus` | `0x32C0` | 89 | UnwindData |  |
| 79 | `ResolveWSDPortToIPAddress` | `0x3320` | 269 | UnwindData |  |
| 76 | `OpenBulk` | `0x3B30` | 306 | UnwindData |  |
| 97 | `WriteBulk` | `0x3C70` | 189 | UnwindData |  |
| 36 | `BytesAvailable` | `0x3D30` | 100 | UnwindData |  |
| 78 | `ReadBulk` | `0x3E00` | 189 | UnwindData |  |
| 57 | `FlushBulk` | `0x3EC0` | 243 | UnwindData |  |
| 38 | `CloseBulk` | `0x3FC0` | 256 | UnwindData |  |
| 67 | `GetLastStatus` | `0x40C0` | 113 | UnwindData |  |
| 73 | `GetTimeout` | `0x4140` | 135 | UnwindData |  |
| 91 | `SetTimeout` | `0x41D0` | 138 | UnwindData |  |
| 88 | `SetOpenTimeout` | `0x4260` | 138 | UnwindData |  |
| 77 | `OpenInterrupt` | `0x42F0` | 302 | UnwindData |  |
| 95 | `WaitForInterrupt` | `0x4420` | 184 | UnwindData |  |
| 96 | `WaitForInterruptEvent` | `0x44E0` | 171 | UnwindData |  |
| 37 | `CancelInterrupt` | `0x4590` | 145 | UnwindData |  |
| 40 | `CloseInterrupt` | `0x4630` | 156 | UnwindData |  |
| 75 | `IsConnected` | `0x46D0` | 220 | UnwindData |  |
| 55 | `ExclusiveBulkLock` | `0x47B0` | 236 | UnwindData |  |
| 56 | `ExclusiveBulkUnlock` | `0x48A0` | 230 | UnwindData |  |
| 66 | `GetDeviceType` | `0x1B180` | 397 | UnwindData |  |
| 59 | `GetCompletePayload` | `0x1B5C0` | 2,078 | UnwindData |  |
| 46 | `CreateCdmBearerTokenPayload` | `0x1BF00` | 1,404 | UnwindData |  |
| 45 | `CreateCDMToken` | `0x1C480` | 1,826 | UnwindData |  |
| 81 | `SendHTTPPUTRequestAndGetResponse` | `0x1CBB0` | 397 | UnwindData |  |
| 80 | `SendHTTPPATCHRequestAndGetResponse` | `0x1D1A0` | 397 | UnwindData |  |
| 48 | `CreateHTTPRequest` | `0x2D150` | 18,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `GetContentAvailable` | `0x2D150` | 18,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SetMethod` | `0x2D150` | 18,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `CreateHTTPRequestEx` | `0x31A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `GetContent` | `0x31A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `SetHeader` | `0x31A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `SetTimeOut` | `0x31A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `GetStatusCode` | `0x31A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `GetValue` | `0x31A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `SetURI` | `0x31A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `SetUserName` | `0x31A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `GetContentType` | `0x31A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `SetPassword` | `0x31A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `CreateMIBConnection` | `0x31A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `GetTimeOut` | `0x31A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `SetContentType` | `0x31A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SetContent` | `0x31A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SetAuthScheme` | `0x31AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `GetResponse` | `0x31AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DisposeAddress` | `0x31AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DisposeHTTPRequest` | `0x31AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DisposeMIBConnection` | `0x31AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GetDeviceAttribute` | `0x31AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `GetDeviceAttributeExt` | `0x31AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `GetNextValue` | `0x31B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SetValue` | `0x31B10` | 41 | UnwindData |  |
| 47 | `CreateFWUpdateProvider` | `0x32360` | 137 | UnwindData |  |
| 65 | `GetDeviceConnection` | `0x323F0` | 177 | UnwindData |  |
| 39 | `CloseDeviceConnection` | `0x324B0` | 176 | UnwindData |  |
| 98 | `WriteFirmwareUpdateData` | `0x32560` | 218 | UnwindData |  |
| 26 | `??_7Address@UnifiedIO@@6BIDisposable@1@@` | `0x130468` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??_7Address@UnifiedIO@@6B01@@` | `0x130490` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??_7MIBConnection@UnifiedIO@@6BIDisposable@1@@` | `0x130518` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??_7MIBConnection@UnifiedIO@@6B01@@` | `0x130540` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??_7HTTPResponse@UnifiedIO@@6B@` | `0x130580` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??_7HTTPRequest@UnifiedIO@@6BIDisposable@1@@` | `0x1305D0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??_7HTTPRequest@UnifiedIO@@6B01@@` | `0x1305F8` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??_7Notifier@UnifiedIO@@6BIDisposable@1@@` | `0x1306B0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??_7Notifier@UnifiedIO@@6B01@@` | `0x1306D8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??_7Stream@UnifiedIO@@6BIDisposable@1@@` | `0x130710` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??_7Stream@UnifiedIO@@6B01@@` | `0x130738` | 0 | Indeterminate |  |
