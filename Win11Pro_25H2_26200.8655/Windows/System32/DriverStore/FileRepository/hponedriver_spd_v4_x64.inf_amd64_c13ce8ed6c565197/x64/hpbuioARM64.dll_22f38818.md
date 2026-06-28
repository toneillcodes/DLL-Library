# Binary Specification: hpbuioARM64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\hponedriver_spd_v4_x64.inf_amd64_c13ce8ed6c565197\x64\hpbuioARM64.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `22f38818aa1f84883b5fbe4625ee64be016574bcecb1ed3c1991818a634a9653`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `??0Stream@UnifiedIO@@QEAA@AEBV01@@Z` | `0x37E0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0Stream@UnifiedIO@@QEAA@XZ` | `0x37E0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??1Stream@UnifiedIO@@UEAA@XZ` | `0x37E0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??4HTTPRequest@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x3808` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??4HTTPResponse@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x3808` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??4MIBConnection@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x3808` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??4Notifier@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x3808` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??4Stream@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x3808` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0Notifier@UnifiedIO@@QEAA@AEBV01@@Z` | `0x3810` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0Notifier@UnifiedIO@@QEAA@XZ` | `0x3810` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1Notifier@UnifiedIO@@UEAA@XZ` | `0x3810` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0HTTPRequest@UnifiedIO@@QEAA@AEBV01@@Z` | `0x3838` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0HTTPRequest@UnifiedIO@@QEAA@XZ` | `0x3838` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1HTTPRequest@UnifiedIO@@UEAA@XZ` | `0x3838` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0HTTPResponse@UnifiedIO@@QEAA@AEBV01@@Z` | `0x3860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0HTTPResponse@UnifiedIO@@QEAA@XZ` | `0x3860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1HTTPResponse@UnifiedIO@@UEAA@XZ` | `0x3860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0MIBConnection@UnifiedIO@@QEAA@AEBV01@@Z` | `0x3870` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0MIBConnection@UnifiedIO@@QEAA@XZ` | `0x3870` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??1MIBConnection@UnifiedIO@@UEAA@XZ` | `0x3870` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0Address@UnifiedIO@@QEAA@XZ` | `0x3898` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1Address@UnifiedIO@@MEAA@XZ` | `0x3898` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0Address@UnifiedIO@@QEAA@AEBV01@@Z` | `0x38C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??4Address@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x38F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CreateAddressFromIPAddress` | `0x3900` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CreateAddressFromPortName` | `0x3968` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `CreateAddressFromQueueName` | `0x3A58` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `CreateAddressFromHostName` | `0x3B48` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `GetRefreshedDeviceIPAddress` | `0x3C38` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SendPrepareToPrint` | `0x3CF0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetAutoSendStatus` | `0x3E20` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `EnableAutoSendStatus` | `0x3F70` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ResolveWSDPortToIPAddress` | `0x3FD8` | 1,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `OpenBulk` | `0x4630` | 312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WriteBulk` | `0x4768` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `BytesAvailable` | `0x4818` | 424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `ReadBulk` | `0x49C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `FlushBulk` | `0x4A70` | 200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `CloseBulk` | `0x4B38` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `GetLastStatus` | `0x4C28` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `GetTimeout` | `0x4C78` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `SetTimeout` | `0x4D18` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `SetOpenTimeout` | `0x4DB0` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `OpenInterrupt` | `0x4E48` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `WaitForInterrupt` | `0x4F98` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WaitForInterruptEvent` | `0x5098` | 248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `CancelInterrupt` | `0x5190` | 232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CloseInterrupt` | `0x5278` | 232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `IsConnected` | `0x5360` | 232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ExclusiveBulkLock` | `0x5448` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ExclusiveBulkUnlock` | `0x55C8` | 106,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `GetDeviceType` | `0x1F4A0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `GetCompletePayload` | `0x1F980` | 2,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `CreateCdmBearerTokenPayload` | `0x203B8` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `CreateCDMToken` | `0x20AB8` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `SendHTTPPUTRequestAndGetResponse` | `0x21338` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SendHTTPPATCHRequestAndGetResponse` | `0x21938` | 93,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `CreateHTTPRequest` | `0x38750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SetMethod` | `0x38750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `CreateHTTPRequestEx` | `0x38760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `SetHeader` | `0x38760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `SetTimeOut` | `0x38760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `GetValue` | `0x38770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `SetURI` | `0x38770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `SetUserName` | `0x38780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `GetNextValue` | `0x38790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `SetPassword` | `0x38790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `CreateMIBConnection` | `0x387A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `GetTimeOut` | `0x387A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `SetContentType` | `0x387A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SetContent` | `0x387B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SetAuthScheme` | `0x387C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `GetDeviceAttributeExt` | `0x387D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `GetResponse` | `0x387D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `GetContent` | `0x387E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `GetContentType` | `0x387F0` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `GetStatusCode` | `0x38888` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `GetContentAvailable` | `0x38920` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DisposeAddress` | `0x389C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DisposeHTTPRequest` | `0x389C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DisposeMIBConnection` | `0x389C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GetDeviceAttribute` | `0x389E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SetValue` | `0x389F0` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `CreateFWUpdateProvider` | `0x39370` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `GetDeviceConnection` | `0x393E8` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `CloseDeviceConnection` | `0x394A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `WriteFirmwareUpdateData` | `0x39530` | 1,049,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??_7Address@UnifiedIO@@6BIDisposable@1@@` | `0x1397F8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??_7Address@UnifiedIO@@6B01@@` | `0x139828` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??_7MIBConnection@UnifiedIO@@6BIDisposable@1@@` | `0x1398B0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??_7MIBConnection@UnifiedIO@@6B01@@` | `0x1398D8` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??_7HTTPResponse@UnifiedIO@@6B@` | `0x139918` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??_7HTTPRequest@UnifiedIO@@6BIDisposable@1@@` | `0x139968` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??_7HTTPRequest@UnifiedIO@@6B01@@` | `0x139998` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??_7Notifier@UnifiedIO@@6BIDisposable@1@@` | `0x139A50` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??_7Notifier@UnifiedIO@@6B01@@` | `0x139A78` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??_7Stream@UnifiedIO@@6BIDisposable@1@@` | `0x139AB0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??_7Stream@UnifiedIO@@6B01@@` | `0x139AD8` | 0 | Indeterminate |  |
