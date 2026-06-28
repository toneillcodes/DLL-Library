# Binary Specification: hpbuio.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\hpygid31_v4.inf_amd64_3da19defbde70baa\amd64\hpbuio.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aae6685d4b50432c62b287fa994977b7173290224470823a9002792b4e326b11`
* **Total Exported Functions:** 90

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `??1Stream@UnifiedIO@@UEAA@XZ` | `0x2760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0Stream@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0Stream@UnifiedIO@@QEAA@XZ` | `0x2780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??4HTTPRequest@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x27B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??4HTTPResponse@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x27B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??4MIBConnection@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x27B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??4Notifier@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x27B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??4Stream@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x27B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1Notifier@UnifiedIO@@UEAA@XZ` | `0x27C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0Notifier@UnifiedIO@@QEAA@AEBV01@@Z` | `0x27E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0Notifier@UnifiedIO@@QEAA@XZ` | `0x27E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1HTTPRequest@UnifiedIO@@UEAA@XZ` | `0x2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0HTTPRequest@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0HTTPRequest@UnifiedIO@@QEAA@XZ` | `0x2830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1HTTPResponse@UnifiedIO@@UEAA@XZ` | `0x2860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0HTTPResponse@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0HTTPResponse@UnifiedIO@@QEAA@XZ` | `0x2870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??1MIBConnection@UnifiedIO@@UEAA@XZ` | `0x2880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0MIBConnection@UnifiedIO@@QEAA@AEBV01@@Z` | `0x28A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0MIBConnection@UnifiedIO@@QEAA@XZ` | `0x28A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1Address@UnifiedIO@@MEAA@XZ` | `0x28D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0Address@UnifiedIO@@QEAA@XZ` | `0x28F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0Address@UnifiedIO@@QEAA@AEBV01@@Z` | `0x2920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??4Address@UnifiedIO@@QEAAAEAV01@AEBV01@@Z` | `0x2950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `CreateAddressFromIPAddress` | `0x2960` | 495 | UnwindData |  |
| 42 | `CreateAddressFromPortName` | `0x2B50` | 156 | UnwindData |  |
| 43 | `CreateAddressFromQueueName` | `0x2C80` | 156 | UnwindData |  |
| 40 | `CreateAddressFromHostName` | `0x2DB0` | 156 | UnwindData |  |
| 64 | `GetRefreshedDeviceIPAddress` | `0x2EE0` | 157 | UnwindData |  |
| 75 | `SendPrepareToPrint` | `0x2F80` | 89 | UnwindData |  |
| 54 | `GetAutoSendStatus` | `0x3070` | 99 | UnwindData |  |
| 50 | `EnableAutoSendStatus` | `0x31B0` | 89 | UnwindData |  |
| 74 | `ResolveWSDPortToIPAddress` | `0x3210` | 269 | UnwindData |  |
| 71 | `OpenBulk` | `0x3A20` | 306 | UnwindData |  |
| 90 | `WriteBulk` | `0x3B60` | 189 | UnwindData |  |
| 36 | `BytesAvailable` | `0x3C20` | 100 | UnwindData |  |
| 73 | `ReadBulk` | `0x3CF0` | 189 | UnwindData |  |
| 53 | `FlushBulk` | `0x3DB0` | 243 | UnwindData |  |
| 38 | `CloseBulk` | `0x3EB0` | 256 | UnwindData |  |
| 62 | `GetLastStatus` | `0x3FB0` | 113 | UnwindData |  |
| 68 | `GetTimeout` | `0x4030` | 135 | UnwindData |  |
| 84 | `SetTimeout` | `0x40C0` | 138 | UnwindData |  |
| 81 | `SetOpenTimeout` | `0x4150` | 138 | UnwindData |  |
| 72 | `OpenInterrupt` | `0x41E0` | 302 | UnwindData |  |
| 88 | `WaitForInterrupt` | `0x4310` | 184 | UnwindData |  |
| 89 | `WaitForInterruptEvent` | `0x43D0` | 171 | UnwindData |  |
| 37 | `CancelInterrupt` | `0x4480` | 145 | UnwindData |  |
| 39 | `CloseInterrupt` | `0x4520` | 156 | UnwindData |  |
| 70 | `IsConnected` | `0x45C0` | 220 | UnwindData |  |
| 51 | `ExclusiveBulkLock` | `0x46A0` | 236 | UnwindData |  |
| 52 | `ExclusiveBulkUnlock` | `0x4790` | 230 | UnwindData |  |
| 61 | `GetDeviceType` | `0x19B00` | 397 | UnwindData |  |
| 55 | `GetCompletePayload` | `0x19F40` | 352 | UnwindData |  |
| 44 | `CreateHTTPRequest` | `0x25B10` | 18,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `GetContentAvailable` | `0x25B10` | 18,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SetMethod` | `0x25B10` | 18,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `CreateHTTPRequestEx` | `0x2A420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `GetContent` | `0x2A420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `SetHeader` | `0x2A420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SetTimeOut` | `0x2A420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `GetStatusCode` | `0x2A430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `GetValue` | `0x2A430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `SetURI` | `0x2A430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `SetUserName` | `0x2A440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetContentType` | `0x2A450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SetPassword` | `0x2A450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `CreateMIBConnection` | `0x2A460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `GetTimeOut` | `0x2A460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `SetContentType` | `0x2A460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SetContent` | `0x2A470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `SetAuthScheme` | `0x2A480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `GetResponse` | `0x2A490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `DisposeAddress` | `0x2A4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `DisposeHTTPRequest` | `0x2A4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `DisposeMIBConnection` | `0x2A4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `GetDeviceAttribute` | `0x2A4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `GetDeviceAttributeExt` | `0x2A4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GetNextValue` | `0x2A4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SetValue` | `0x2A4F0` | 41 | UnwindData |  |
| 26 | `??_7Address@UnifiedIO@@6BIDisposable@1@@` | `0x105F48` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??_7Address@UnifiedIO@@6B01@@` | `0x105F70` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??_7MIBConnection@UnifiedIO@@6BIDisposable@1@@` | `0x105FF8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??_7MIBConnection@UnifiedIO@@6B01@@` | `0x106020` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??_7HTTPResponse@UnifiedIO@@6B@` | `0x106060` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??_7HTTPRequest@UnifiedIO@@6BIDisposable@1@@` | `0x1060B0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??_7HTTPRequest@UnifiedIO@@6B01@@` | `0x1060D8` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??_7Notifier@UnifiedIO@@6BIDisposable@1@@` | `0x106190` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??_7Notifier@UnifiedIO@@6B01@@` | `0x1061B8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??_7Stream@UnifiedIO@@6BIDisposable@1@@` | `0x1061F0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??_7Stream@UnifiedIO@@6B01@@` | `0x106218` | 0 | Indeterminate |  |
