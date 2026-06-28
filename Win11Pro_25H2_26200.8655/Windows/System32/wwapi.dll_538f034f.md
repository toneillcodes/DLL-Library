# Binary Specification: wwapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wwapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `538f034facbe5d10a3c44a530a07a66984d96780eceab2b71f7cbd68bbd57edf`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 43 | `WwanOpenHandle` | `0x1010` | 620 | UnwindData |  |
| 16 | `WwanAllocateMemory` | `0x20C0` | 108 | UnwindData |  |
| 45 | `WwanQueryInterface` | `0x2140` | 886 | UnwindData |  |
| 18 | `WwanCloseHandle` | `0x2980` | 619 | UnwindData |  |
| 37 | `WwanGetProfileList` | `0x2FE0` | 627 | UnwindData |  |
| 26 | `WwanEnumerateInterfaces` | `0x3260` | 602 | UnwindData |  |
| 27 | `WwanFreeMemory` | `0x34C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `Wwan2RegisterNotification` | `0x34E0` | 109 | UnwindData |  |
| 3 | `Wwan2CloseHandle` | `0x36B0` | 580 | UnwindData |  |
| 7 | `Wwan2OpenHandle` | `0x3900` | 575 | UnwindData |  |
| 4 | `Wwan2EnumerateDeviceServices` | `0x3B50` | 480 | UnwindData |  |
| 39 | `WwanGetProfileMetaData` | `0x3DB0` | 585 | UnwindData |  |
| 48 | `WwanRegisterNotification` | `0x4190` | 124 | UnwindData |  |
| 1 | `Wwan2CloseDeviceServiceCommandSession` | `0x4380` | 342 | UnwindData |  |
| 35 | `WwanGetProfileIndex` | `0x4540` | 308 | UnwindData |  |
| 9 | `Wwan2QueryInterfaces` | `0x4680` | 302 | UnwindData |  |
| 36 | `WwanGetProfileIstream` | `0x47C0` | 452 | UnwindData |  |
| 33 | `WwanGetProfile` | `0x4990` | 605 | UnwindData |  |
| 11 | `Wwan2SendDeviceServiceCommand` | `0x4C00` | 346 | UnwindData |  |
| 46 | `WwanQueryInterfaceEx` | `0x4D60` | 512 | UnwindData |  |
| 5 | `Wwan2OpenDeviceServiceCommandSession` | `0x4F70` | 342 | UnwindData |  |
| 40 | `WwanGetProfileState` | `0x50D0` | 573 | UnwindData |  |
| 30 | `WwanGetDMConfigProfileList` | `0x5320` | 530 | UnwindData |  |
| 29 | `WwanGetDMConfigProfile` | `0x55B0` | 463 | UnwindData |  |
| 56 | `WwanSetNetworkQuietMode` | `0x5790` | 352 | UnwindData |  |
| 55 | `WwanSetInterface` | `0x5900` | 478 | UnwindData |  |
| 64 | `WwanUiccOpenChannel` | `0x5BB0` | 358 | UnwindData |  |
| 2 | `Wwan2CloseDeviceServiceDataSession` | `0x78E0` | 325 | UnwindData |  |
| 6 | `Wwan2OpenDeviceServiceDataSession` | `0x7A30` | 338 | UnwindData |  |
| 8 | `Wwan2QueryDeviceServiceSupportedCommands` | `0x7B90` | 325 | UnwindData |  |
| 12 | `Wwan2SubscribePowerStateEvents` | `0x7CE0` | 280 | UnwindData |  |
| 13 | `Wwan2WriteDeviceServiceData` | `0x7E00` | 350 | UnwindData |  |
| 14 | `WwanAcquireOnDemandConnection` | `0x7F70` | 460 | UnwindData |  |
| 15 | `WwanActivateNotification` | `0x8150` | 304 | UnwindData |  |
| 17 | `WwanAuthChallenge` | `0x8290` | 487 | UnwindData |  |
| 19 | `WwanConnect` | `0x8480` | 52 | UnwindData |  |
| 20 | `WwanConnectAdditionalPdpContext` | `0x84C0` | 481 | UnwindData |  |
| 21 | `WwanConnectByActivityId` | `0x86B0` | 603 | UnwindData |  |
| 23 | `WwanDeleteDMConfigProfile` | `0x8920` | 335 | UnwindData |  |
| 24 | `WwanDeleteProfile` | `0x8A80` | 417 | UnwindData |  |
| 25 | `WwanDisconnect` | `0x8C30` | 465 | UnwindData |  |
| 28 | `WwanGetDMConfigBinary` | `0x8E10` | 345 | UnwindData |  |
| 31 | `WwanGetInfGuidAndProfileByProfileIndex` | `0x8F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `WwanGetInterfaceGuid` | `0x8F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `WwanGetProfileHomeProviderName` | `0x8F80` | 448 | UnwindData |  |
| 38 | `WwanGetProfileListByPurpose` | `0x9150` | 595 | UnwindData |  |
| 41 | `WwanGetTrafficDescriptorList` | `0x93B0` | 429 | UnwindData |  |
| 42 | `WwanModemLogging` | `0x9570` | 478 | UnwindData |  |
| 44 | `WwanQueryIPv6eHRPDControl` | `0x9760` | 345 | UnwindData |  |
| 47 | `WwanRegister` | `0x98C0` | 528 | UnwindData |  |
| 49 | `WwanReleaseOnDemandConnection` | `0x9AE0` | 441 | UnwindData |  |
| 50 | `WwanScan` | `0x9CA0` | 462 | UnwindData |  |
| 51 | `WwanSearchProfile` | `0x9E80` | 449 | UnwindData |  |
| 52 | `WwanSetDMConfigBinary` | `0xA050` | 392 | UnwindData |  |
| 53 | `WwanSetDMConfigProfile` | `0xA1E0` | 468 | UnwindData |  |
| 54 | `WwanSetIPv6eHRPDControl` | `0xA3C0` | 393 | UnwindData |  |
| 57 | `WwanSetProfile` | `0xA550` | 535 | UnwindData |  |
| 58 | `WwanSetProfileMetaData` | `0xA770` | 512 | UnwindData |  |
| 59 | `WwanSetSmsConfiguration` | `0xA980` | 388 | UnwindData |  |
| 60 | `WwanSmsDelete` | `0xAB10` | 388 | UnwindData |  |
| 61 | `WwanSmsRead` | `0xACA0` | 388 | UnwindData |  |
| 62 | `WwanSmsSend` | `0xAE30` | 418 | UnwindData |  |
| 63 | `WwanUiccCloseChannel` | `0xAFE0` | 389 | UnwindData |  |
| 65 | `WwanUiccSendApdu` | `0xB170` | 413 | UnwindData |  |
| 66 | `WwanUiccSetTerminalCapability` | `0xB320` | 378 | UnwindData |  |
| 67 | `WwanUssdRequest` | `0xB4A0` | 450 | UnwindData |  |
| 22 | `WwanConvertToInterfaceObject` | `0xC0A0` | 97 | UnwindData |  |
