# Binary Specification: hpbuio32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\hponedriver_spd_v4_x64.inf_amd64_c13ce8ed6c565197\x64\hpbuio32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `909fc03c84b4d6aebb441673d65c83e3662ac63147d25388a7e94fbc3708a951`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `??1Stream@UnifiedIO@@UAE@XZ` | `0x21C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0Stream@UnifiedIO@@QAE@XZ` | `0x21E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0Stream@UnifiedIO@@QAE@ABV01@@Z` | `0x2200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??4HTTPRequest@UnifiedIO@@QAEAAV01@ABV01@@Z` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??4HTTPResponse@UnifiedIO@@QAEAAV01@ABV01@@Z` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??4MIBConnection@UnifiedIO@@QAEAAV01@ABV01@@Z` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??4Notifier@UnifiedIO@@QAEAAV01@ABV01@@Z` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??4Stream@UnifiedIO@@QAEAAV01@ABV01@@Z` | `0x2220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1Notifier@UnifiedIO@@UAE@XZ` | `0x2230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0Notifier@UnifiedIO@@QAE@XZ` | `0x2250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0Notifier@UnifiedIO@@QAE@ABV01@@Z` | `0x2270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1HTTPRequest@UnifiedIO@@UAE@XZ` | `0x2290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0HTTPRequest@UnifiedIO@@QAE@XZ` | `0x22B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0HTTPRequest@UnifiedIO@@QAE@ABV01@@Z` | `0x22D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1HTTPResponse@UnifiedIO@@UAE@XZ` | `0x22F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0HTTPResponse@UnifiedIO@@QAE@XZ` | `0x2300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0HTTPResponse@UnifiedIO@@QAE@ABV01@@Z` | `0x2310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??1MIBConnection@UnifiedIO@@UAE@XZ` | `0x2320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0MIBConnection@UnifiedIO@@QAE@XZ` | `0x2340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0MIBConnection@UnifiedIO@@QAE@ABV01@@Z` | `0x2360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1Address@UnifiedIO@@MAE@XZ` | `0x2380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0Address@UnifiedIO@@QAE@XZ` | `0x23A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0Address@UnifiedIO@@QAE@ABV01@@Z` | `0x23C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??4Address@UnifiedIO@@QAEAAV01@ABV01@@Z` | `0x23F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CreateAddressFromIPAddress` | `0x2410` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CreateAddressFromPortName` | `0x25C0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `CreateAddressFromQueueName` | `0x26B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `CreateAddressFromHostName` | `0x27A0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `GetRefreshedDeviceIPAddress` | `0x2890` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SendPrepareToPrint` | `0x2950` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetAutoSendStatus` | `0x2A30` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `EnableAutoSendStatus` | `0x2B70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ResolveWSDPortToIPAddress` | `0x2BB0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `OpenBulk` | `0x3580` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WriteBulk` | `0x3680` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `BytesAvailable` | `0x3720` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `ReadBulk` | `0x37B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `FlushBulk` | `0x3850` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `CloseBulk` | `0x3910` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `GetLastStatus` | `0x39F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `GetTimeout` | `0x3A50` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `SetTimeout` | `0x3AC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `SetOpenTimeout` | `0x3B30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `OpenInterrupt` | `0x3BA0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `WaitForInterrupt` | `0x3CA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WaitForInterruptEvent` | `0x3D30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `CancelInterrupt` | `0x3DB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CloseInterrupt` | `0x3E30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `IsConnected` | `0x3EB0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ExclusiveBulkLock` | `0x3F60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ExclusiveBulkUnlock` | `0x4040` | 88,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `GetDeviceType` | `0x19A70` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `GetCompletePayload` | `0x19E80` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `CreateCdmBearerTokenPayload` | `0x1A680` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `CreateCDMToken` | `0x1ABB0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `SendHTTPPUTRequestAndGetResponse` | `0x1B520` | 1,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SendHTTPPATCHRequestAndGetResponse` | `0x1B9E0` | 72,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `CreateHTTPRequest` | `0x2D4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `CreateHTTPRequestEx` | `0x2D4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `SetHeader` | `0x2D4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `SetURI` | `0x2D500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `SetUserName` | `0x2D510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `SetPassword` | `0x2D520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SetMethod` | `0x2D530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `CreateMIBConnection` | `0x2D540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `SetContentType` | `0x2D540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SetContent` | `0x2D550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SetAuthScheme` | `0x2D570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `GetResponse` | `0x2D580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `GetContent` | `0x2D590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `GetContentType` | `0x2D5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `GetStatusCode` | `0x2D5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `GetContentAvailable` | `0x2D5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DisposeAddress` | `0x2D5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DisposeHTTPRequest` | `0x2D5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DisposeMIBConnection` | `0x2D5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GetDeviceAttribute` | `0x2D5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `GetDeviceAttributeExt` | `0x2D610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `GetValue` | `0x2D630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `GetNextValue` | `0x2D650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SetValue` | `0x2D670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `SetTimeOut` | `0x2D690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `GetTimeOut` | `0x2D6A0` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `CreateFWUpdateProvider` | `0x2DE60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `GetDeviceConnection` | `0x2DED0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `CloseDeviceConnection` | `0x2DF90` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `WriteFirmwareUpdateData` | `0x2E010` | 811,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??_7Address@UnifiedIO@@6BIDisposable@1@@` | `0xF4140` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??_7Address@UnifiedIO@@6B01@@` | `0xF4154` | 68 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??_7MIBConnection@UnifiedIO@@6BIDisposable@1@@` | `0xF4198` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??_7MIBConnection@UnifiedIO@@6B01@@` | `0xF41AC` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??_7HTTPResponse@UnifiedIO@@6B@` | `0xF41CC` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??_7HTTPRequest@UnifiedIO@@6BIDisposable@1@@` | `0xF41F4` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??_7HTTPRequest@UnifiedIO@@6B01@@` | `0xF4208` | 92 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??_7Notifier@UnifiedIO@@6BIDisposable@1@@` | `0xF4264` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??_7Notifier@UnifiedIO@@6B01@@` | `0xF4278` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??_7Stream@UnifiedIO@@6BIDisposable@1@@` | `0xF4294` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??_7Stream@UnifiedIO@@6B01@@` | `0xF42A8` | 0 | Indeterminate |  |
