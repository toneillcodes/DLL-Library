# Binary Specification: iscsium.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iscsium.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3409e674b65ecf3cac2bfa97ebf89621a6b20d81a08df92b4b02bdaa536775d1`
* **Total Exported Functions:** 70

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DiscpAnsiToUnicode` | `0x18E0` | 295 | UnwindData |  |
| 7 | `DiscpAnsiToUnicodeSize` | `0x1A10` | 88 | UnwindData |  |
| 8 | `DiscpCopyString` | `0x1A70` | 252 | UnwindData |  |
| 9 | `DiscpCopyStringToAnsi` | `0x1B80` | 153 | UnwindData |  |
| 27 | `DiscpExecuteMethod` | `0x1C20` | 486 | UnwindData |  |
| 34 | `DiscpGetStringFromDataBlock` | `0x1E10` | 86 | UnwindData |  |
| 42 | `DiscpPadDataBlock` | `0x1E70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `DiscpParseAllData` | `0x1EB0` | 776 | UnwindData |  |
| 45 | `DiscpParseSingleInstance` | `0x21C0` | 118 | UnwindData |  |
| 46 | `DiscpPnpDeviceInterfaceToInstanceName` | `0x2240` | 472 | UnwindData |  |
| 47 | `DiscpQueryAllData` | `0x2420` | 334 | UnwindData |  |
| 48 | `DiscpQuerySingleInstance` | `0x2580` | 345 | UnwindData |  |
| 64 | `DiscpUnicodeToAnsi` | `0x26E0` | 278 | UnwindData |  |
| 65 | `DiscpUnicodeToAnsiSize` | `0x2800` | 99 | UnwindData |  |
| 1 | `DiscpAddStringToMultiSzList` | `0x2870` | 337 | UnwindData |  |
| 2 | `DiscpAlignDataStruct` | `0x29D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DiscpAllocMemory` | `0x2A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DiscpAllocProcessMemory` | `0x2A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DiscpAnsiCharsToString` | `0x2A60` | 167 | UnwindData |  |
| 10 | `DiscpCopyToCountedString` | `0x2B10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DiscpCopyUnicodeString` | `0x2B90` | 187 | UnwindData |  |
| 13 | `DiscpDecryptBuffer` | `0x2C60` | 233 | UnwindData |  |
| 14 | `DiscpDisableEventlog` | `0x2D50` | 42 | UnwindData |  |
| 16 | `DiscpDisableWinsock` | `0x2D80` | 61 | UnwindData |  |
| 17 | `DiscpDisestablishIrpPump` | `0x2DD0` | 335 | UnwindData |  |
| 18 | `DiscpDuplicateString` | `0x2F30` | 184 | UnwindData |  |
| 19 | `DiscpEnableEventlog` | `0x2FF0` | 57 | UnwindData |  |
| 21 | `DiscpEnableWinsock` | `0x3030` | 97 | UnwindData |  |
| 22 | `DiscpEncryptBuffer` | `0x30A0` | 275 | UnwindData |  |
| 23 | `DiscpEnumerateDeviceInterfaces` | `0x31C0` | 804 | UnwindData |  |
| 24 | `DiscpEnumerateRegistryValues` | `0x34F0` | 611 | UnwindData |  |
| 25 | `DiscpEstablishIrpPump` | `0x3760` | 655 | UnwindData |  |
| 26 | `DiscpEstablishTCPSocket` | `0x3A00` | 442 | UnwindData |  |
| 28 | `DiscpFreeDeviceInterfaceList` | `0x3BF0` | 131 | UnwindData |  |
| 29 | `DiscpFreeMemory` | `0x3C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DiscpFreeProcessMemory` | `0x3CA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DiscpGenerateiScsiNameFromComputerName` | `0x3CD0` | 370 | UnwindData |  |
| 32 | `DiscpGetPnpDeviceId` | `0x3E50` | 205 | UnwindData |  |
| 33 | `DiscpGetRegistryValue` | `0x3F30` | 390 | UnwindData |  |
| 37 | `DiscpIsDNSAddress` | `0x42B0` | 30 | UnwindData |  |
| 38 | `DiscpIsStringInList` | `0x42E0` | 100 | UnwindData |  |
| 39 | `DiscpLoadSystemLibrary` | `0x4350` | 365 | UnwindData |  |
| 41 | `DiscpOpenRegistryKey` | `0x44D0` | 211 | UnwindData |  |
| 44 | `DiscpParseKeyValue` | `0x45B0` | 334 | UnwindData |  |
| 49 | `DiscpRegCloseKey` | `0x4710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DiscpRegisterDeviceInterfaceNotification` | `0x4730` | 130 | UnwindData |  |
| 52 | `DiscpRegisterForDeviceInterfaceNotfication` | `0x4730` | 130 | UnwindData |  |
| 53 | `DiscpRegisterHeap` | `0x47C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `DiscpRemoveStringFromMultiSzList` | `0x47D0` | 143 | UnwindData |  |
| 55 | `DiscpReportEventlog` | `0x4870` | 284 | UnwindData |  |
| 56 | `DiscpReportEventlogWithStatus` | `0x49A0` | 310 | UnwindData |  |
| 57 | `DiscpSendIrpRequest` | `0x4BD0` | 90 | UnwindData |  |
| 58 | `DiscpSetRegistryValue` | `0x4C30` | 295 | UnwindData |  |
| 60 | `DiscpTextAddrToBinary` | `0x4D60` | 282 | UnwindData |  |
| 61 | `DiscpTimebomb` | `0x4E80` | 79 | UnwindData |  |
| 62 | `DiscpULongAddList` | `0x4EE0` | 77 | UnwindData |  |
| 63 | `DiscpUTF8ToUnicode` | `0x4F40` | 339 | UnwindData |  |
| 66 | `DiscpUnicodeToUTF8` | `0x50A0` | 383 | UnwindData |  |
| 68 | `DiscpXtoI` | `0x5230` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `Discpxtoi` | `0x5230` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `DllMain` | `0x52B0` | 32 | UnwindData |  |
| 40 | `DiscpMapiSCSIString` | `0x5360` | 730 | UnwindData |  |
| 67 | `DiscpValidateiSCSIString` | `0x5640` | 487 | UnwindData |  |
| 12 | `DiscpDebugPrintX` | `0x5830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DiscpDisableLogToFile` | `0x5850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `DiscpRegisterDebugMask` | `0x5850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `DiscpEnableLogToFile` | `0x5860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DiscpGuidToString` | `0x5870` | 232 | UnwindData |  |
| 36 | `DiscpIdKeyToString` | `0x5960` | 57 | UnwindData |  |
| 59 | `DiscpSockAddrToText` | `0x59A0` | 0 | Indeterminate |  |
